#!/usr/bin/env python3
"""
Test script for GoHighLevel MCP Server HTTP transport.
This script tests the server when running with HTTP/Streamable HTTP transport.
"""

import asyncio
import aiohttp
import json
import os
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

async def test_http_server():
    """Test the MCP server running with HTTP transport."""
    
    # Server configuration
    host = os.getenv("MCP_HOST", "127.0.0.1")
    port = int(os.getenv("MCP_PORT", "8000"))
    base_url = f"http://{host}:{port}"
    
    print(f"Testing MCP server at {base_url}")
    
    try:
        async with aiohttp.ClientSession() as session:
            # Test the health/status endpoint
            print("1. Testing server status...")
            async with session.get(f"{base_url}/health") as response:
                if response.status == 200:
                    print("   ✅ Server is healthy")
                else:
                    print(f"   ❌ Server health check failed: {response.status}")
            
            # Test the MCP endpoint
            print("2. Testing MCP endpoint...")
            mcp_url = f"{base_url}/mcp"
            
            # Test with a simple MCP request
            mcp_request = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/list",
                "params": {}
            }
            
            async with session.post(
                mcp_url,
                json=mcp_request,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if "result" in data and "tools" in data["result"]:
                        tools_count = len(data["result"]["tools"])
                        print(f"   ✅ MCP endpoint working - {tools_count} tools available")
                        
                        # Show first few tools
                        if tools_count > 0:
                            print("   First 5 tools:")
                            for i, tool in enumerate(data["result"]["tools"][:5]):
                                print(f"     - {tool['name']}: {tool.get('description', 'No description')}")
                    else:
                        print("   ❌ Invalid MCP response format")
                        print(f"   Response: {data}")
                else:
                    print(f"   ❌ MCP endpoint failed: {response.status}")
                    text = await response.text()
                    print(f"   Response: {text}")
            
            # Test a specific tool if available
            print("3. Testing tool execution...")
            tool_request = {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "get_locations",  # This should be available in most GHL setups
                    "arguments": {}
                }
            }
            
            async with session.post(
                mcp_url,
                json=tool_request,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if "result" in data:
                        print("   ✅ Tool execution successful")
                    elif "error" in data:
                        print(f"   ⚠️  Tool execution returned error: {data['error']}")
                    else:
                        print("   ❌ Invalid tool response format")
                else:
                    print(f"   ❌ Tool execution failed: {response.status}")
            
    except aiohttp.ClientConnectorError:
        print(f"❌ Could not connect to server at {base_url}")
        print("   Make sure the server is running with HTTP transport:")
        print("   MCP_TRANSPORT=http python src/main.py")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main entry point."""
    print("GoHighLevel MCP Server HTTP Transport Test")
    print("=" * 50)
    
    # Check environment variables
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport.lower() not in ["http", "streamable-http", "http-streamable"]:
        print("⚠️  Warning: MCP_TRANSPORT is not set to 'http'")
        print("   Current value:", transport)
        print("   Set MCP_TRANSPORT=http to test HTTP transport")
        print()
    
    asyncio.run(test_http_server())

if __name__ == "__main__":
    main()
