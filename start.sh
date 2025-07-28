#!/bin/bash

# Simple GoHighLevel MCP Server startup

echo "🚀 Starting GoHighLevel MCP Server..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
    python src/main.py
else
    # Try python3 if no virtual environment
    python3 src/main.py
fi
