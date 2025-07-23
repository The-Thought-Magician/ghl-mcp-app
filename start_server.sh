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
    echo ""
fi

# Activate virtual environment and run server
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

echo "📡 Starting MCP server..."
python src/main.py
