#!/bin/bash

# GoHighLevel MCP Server Startup Script

echo "🚀 Starting GoHighLevel MCP Server..."
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first:"
    echo "   uv venv"
    echo "   source .venv/bin/activate"
    echo "   uv pip install fastmcp aiohttp pydantic python-dotenv"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Creating from template..."
    cp .env.example .env
    echo "📝 Please edit .env and add your GoHighLevel API key:"
    echo "   GHL_API_KEY=your-api-key-here"
    echo "   GHL_LOCATION_ID=your-location-id-here"
    echo ""
fi

# Load environment variables
set -a
source .env
set +a

# Check required variables
if [ -z "$GHL_API_KEY" ] || [ "$GHL_API_KEY" = "your-api-key-here" ]; then
    echo "⚠️  Warning: GHL_API_KEY not properly configured in .env file"
fi

if [ -z "$GHL_LOCATION_ID" ] || [ "$GHL_LOCATION_ID" = "your-location-id-here" ]; then
    echo "⚠️  Warning: GHL_LOCATION_ID not properly configured in .env file"
fi

# Set default transport if not specified
MCP_TRANSPORT=${MCP_TRANSPORT:-stdio}
MCP_HOST=${MCP_HOST:-127.0.0.1}
MCP_PORT=${MCP_PORT:-8000}

echo "📋 Configuration:"
echo "   Transport: $MCP_TRANSPORT"
if [ "$MCP_TRANSPORT" != "stdio" ]; then
    echo "   Host: $MCP_HOST"
    echo "   Port: $MCP_PORT"
    echo "   URL: http://$MCP_HOST:$MCP_PORT/mcp"
fi
echo "   API Key: ${GHL_API_KEY:0:10}..." 
echo "   Location ID: ${GHL_LOCATION_ID:0:10}..."
echo ""

# Activate virtual environment and run server
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Show transport-specific information
case "$MCP_TRANSPORT" in
    "http"|"streamable-http"|"http-streamable")
        echo "🌐 Starting with Streamable HTTP transport (recommended for LibreChat)"
        echo "   LibreChat integration URL: http://$MCP_HOST:$MCP_PORT/mcp"
        echo "   Test with: python test_http_server.py"
        ;;
    "sse")
        echo "📡 Starting with SSE transport (legacy)"
        echo "   SSE endpoint: http://$MCP_HOST:$MCP_PORT/sse"
        ;;
    "stdio"|*)
        echo "💻 Starting with STDIO transport (default)"
        echo "   Use for direct MCP client integration"
        ;;
esac

echo ""
echo "🏁 Starting server..."
echo "   Press Ctrl+C to stop"
echo ""

echo "📡 Starting MCP server..."
python src/main.py
