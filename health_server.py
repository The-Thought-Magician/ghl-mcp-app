#!/usr/bin/env python3
"""
Simple health check server for Render deployment.
This runs alongside the MCP server to provide health endpoints.
"""

import asyncio
import json
from aiohttp import web
import os

async def health_check(request):
    """Health check endpoint for Render."""
    return web.json_response({
        "status": "healthy",
        "service": "GoHighLevel MCP Server",
        "version": "1.0.0",
        "transport": os.getenv("MCP_TRANSPORT", "stdio"),
        "timestamp": str(asyncio.get_event_loop().time())
    })

async def root(request):
    """Root endpoint with service information."""
    return web.json_response({
        "service": "GoHighLevel MCP Server",
        "description": "Model Context Protocol server for GoHighLevel API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "mcp": "/mcp" if os.getenv("MCP_TRANSPORT") == "http" else "stdio"
        },
        "documentation": "https://github.com/your-org/ghl-mcp-app"
    })

async def init_app():
    """Initialize the health check web application."""
    app = web.Application()
    app.router.add_get('/', root)
    app.router.add_get('/health', health_check)
    return app

async def run_health_server():
    """Run the health check server."""
    app = await init_app()
    
    host = os.getenv("HEALTH_HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    print(f"Starting health check server on {host}:{port}")
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, host, port)
    await site.start()
    
    print(f"Health check server running at http://{host}:{port}")
    print("Endpoints:")
    print(f"  - GET {host}:{port}/ (service info)")
    print(f"  - GET {host}:{port}/health (health check)")
    
    # Keep the server running
    try:
        while True:
            await asyncio.sleep(3600)  # Sleep for 1 hour
    except KeyboardInterrupt:
        print("Shutting down health check server...")
    finally:
        await runner.cleanup()

if __name__ == "__main__":
    asyncio.run(run_health_server())
