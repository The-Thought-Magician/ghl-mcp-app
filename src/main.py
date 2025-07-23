#!/usr/bin/env python3
"""
GoHighLevel MCP Server

This server provides access to GoHighLevel API endpoints through the Model Context Protocol (MCP).
It automatically generates tools from the GoHighLevel OpenAPI specifications.
"""

import os
import json
import asyncio
from pathlib import Path
from typing import Dict, Any
import httpx
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def load_openapi_specs(docs_path: Path) -> Dict[str, Dict[str, Any]]:
    """Load all OpenAPI specifications from the docs directory."""
    specs = {}
    
    # Find all JSON files that contain OpenAPI specifications
    json_files = [
        f for f in docs_path.glob("**/*.json")
        if f.name not in ["toc.json", "highlevel-teams.json"]
    ]
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                spec = json.load(f)
                
            # Verify it's an OpenAPI spec
            if "openapi" in spec and "paths" in spec:
                specs[json_file.stem] = spec
                print(f"Loaded OpenAPI spec: {json_file.name}")
        except Exception as e:
            print(f"Error loading {json_file.name}: {e}")
    
    return specs


def fix_openapi_schema(spec: Dict[str, Any]) -> Dict[str, Any]:
    """Fix common OpenAPI schema issues in the GoHighLevel specifications."""
    
    def fix_parameter_schema(param: Dict[str, Any]) -> Dict[str, Any]:
        """Fix parameter schema issues."""
        if "schema" in param:
            schema = param["schema"]
            # Fix invalid 'any' type
            if isinstance(schema, dict) and schema.get("type") == "any":
                schema["type"] = "string"  # Default to string
                
            # Remove invalid schema properties that should be references
            if isinstance(schema, dict) and "type" in schema and "$ref" not in schema:
                # Keep only valid schema properties
                valid_schema = {}
                for key, value in schema.items():
                    if key in ["type", "format", "example", "description", "enum", "items", "properties", "required"]:
                        valid_schema[key] = value
                param["schema"] = valid_schema
        
        # Handle anyOf with schema conflicts
        if "anyOf" in param and "schema" in param:
            # Remove the conflicting schema, keep anyOf
            del param["schema"]
            
        return param
    
    def traverse_and_fix(obj: Any) -> Any:
        """Recursively traverse and fix the OpenAPI spec."""
        if isinstance(obj, dict):
            # Fix parameters
            if "parameters" in obj:
                obj["parameters"] = [fix_parameter_schema(param) for param in obj["parameters"]]
            
            # Recursively process nested objects
            return {key: traverse_and_fix(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [traverse_and_fix(item) for item in obj]
        else:
            return obj
    
    return traverse_and_fix(spec)


def merge_openapi_specs(specs: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Merge multiple OpenAPI specifications into a single spec."""
    merged_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "GoHighLevel API",
            "description": "Unified GoHighLevel API endpoints",
            "version": "1.0.0"
        },
        "paths": {},
        "components": {
            "schemas": {},
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [
            {"bearerAuth": []}
        ]
    }
    
    # Merge all paths and components
    for spec_name, spec in specs.items():
        # Merge paths
        for path, methods in spec.get("paths", {}).items():
            if path not in merged_spec["paths"]:
                merged_spec["paths"][path] = {}
            merged_spec["paths"][path].update(methods)
        
        # Merge components/schemas if they exist
        if "components" in spec and "schemas" in spec["components"]:
            merged_spec["components"]["schemas"].update(spec["components"]["schemas"])
    
    return merged_spec


async def create_ghl_server():
    """Create the GoHighLevel MCP server."""
    
    # Get configuration from environment variables
    api_key = os.getenv("GHL_API_KEY")
    base_url = os.getenv("GHL_BASE_URL", "https://services.leadconnectorhq.com")
    
    if not api_key:
        print("Warning: GHL_API_KEY environment variable not set. Server will run with placeholder authentication.")
        api_key = "your-api-key-here"
    
    # Set up the HTTP client with authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Version": "2021-07-28",  # GoHighLevel API version
        "Content-Type": "application/json"
    }
    
    client = httpx.AsyncClient(
        base_url=base_url,
        headers=headers,
        timeout=30.0
    )
    
    # Load and merge OpenAPI specifications
    project_root = Path(__file__).parents[1]
    docs_path = project_root / "docs"
    
    print("Loading GoHighLevel OpenAPI specifications...")
    specs = load_openapi_specs(docs_path)
    
    if not specs:
        raise RuntimeError("No valid OpenAPI specifications found in docs directory")
    
    print(f"Found {len(specs)} OpenAPI specifications")
    merged_spec = merge_openapi_specs(specs)
    
    # Fix schema issues
    print("Fixing OpenAPI schema issues...")
    merged_spec = fix_openapi_schema(merged_spec)
    
    print(f"Merged into single specification with {len(merged_spec['paths'])} endpoints")
    
    # Define custom route mappings for better organization
    route_maps = [
        # Convert all GET endpoints with path parameters to resource templates
        # RouteMap(
        #     methods=["GET"],
        #     pattern=r".*\{.*\}.*",
        #     mcp_type=MCPType.RESOURCE_TEMPLATE,
        #     mcp_tags={"ghl", "resource-template"}
        # ),
        
        # Convert all other GET endpoints to resources
        # RouteMap(
        #     methods=["GET"],
        #     pattern=r".*",
        #     mcp_type=MCPType.RESOURCE,
        #     mcp_tags={"ghl", "resource"}
        # ),
        
        # Convert all non-GET endpoints to tools
        RouteMap(
            methods=["POST", "PUT", "PATCH", "DELETE"],
            pattern=r".*",
            mcp_type=MCPType.TOOL,
            mcp_tags={"ghl", "api"}
        ),
        
        # Convert all GET endpoints to tools for better compatibility
        RouteMap(
            methods=["GET"],
            pattern=r".*",
            mcp_type=MCPType.TOOL,
            mcp_tags={"ghl", "api", "read"}
        ),
        
        # Exclude any admin or internal endpoints if they exist
        RouteMap(
            pattern=r".*/admin/.*",
            mcp_type=MCPType.EXCLUDE
        ),
        
        RouteMap(
            tags={"internal"},
            mcp_type=MCPType.EXCLUDE
        )
    ]
    
    # Create the MCP server from the merged OpenAPI specification
    mcp = FastMCP.from_openapi(
        openapi_spec=merged_spec,
        client=client,
        name="GoHighLevel MCP Server",
        route_maps=route_maps,
        tags={"ghl", "crm", "marketing"}
    )
    
    print(f"Created MCP server successfully!")
    return mcp


async def main():
    """Main entry point for the MCP server."""
    try:
        server = await create_ghl_server()
        print("Starting GoHighLevel MCP Server...")
        print("Environment variables:")
        print(f"  GHL_API_KEY: {'Set' if os.getenv('GHL_API_KEY') else 'Not set'}")
        print(f"  GHL_BASE_URL: {os.getenv('GHL_BASE_URL', 'https://services.leadconnectorhq.com')}")
        print("\nServer is ready to accept connections.")
        
        # Run the server
        await server.run()
        
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Error starting server: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
