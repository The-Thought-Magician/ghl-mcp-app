#!/bin/bash

# Render.com deployment startup script for GoHighLevel MCP Server

echo "🚀 GoHighLevel MCP Server - Render Deployment"
echo "=============================================="

# Check if we're running on Render (Render sets these environment variables)
if [ -n "$RENDER_SERVICE_ID" ]; then
    echo "✅ Running on Render.com"
    DEPLOYMENT_ENV="render"
else
    echo "🏠 Running locally"
    DEPLOYMENT_ENV="local"
fi

echo ""

# Step 1: Clone/Update GoHighLevel API Documentation
echo "📚 Step 1: Setting up GoHighLevel API Documentation..."

if [ ! -d "docs" ]; then
    echo "   Cloning GoHighLevel API documentation..."
    git clone https://github.com/GoHighLevel/highlevel-api-docs.git docs
    if [ $? -ne 0 ]; then
        echo "❌ Failed to clone documentation repository"
        exit 1
    fi
    echo "✅ Documentation cloned successfully"
else
    echo "   Documentation exists, updating..."
    cd docs
    git pull origin main
    if [ $? -ne 0 ]; then
        echo "⚠️  Failed to update documentation (continuing anyway)"
    else
        echo "✅ Documentation updated successfully"
    fi
    cd ..
fi

echo ""

# Step 2: Environment Setup
echo "⚙️  Step 2: Environment configuration..."

if [ "$DEPLOYMENT_ENV" = "render" ]; then
    echo "   Using Render environment variables"
    echo "   - Dependencies: Already installed by Render"
    echo "   - Python: $(python --version 2>&1 || python3 --version 2>&1)"
    
    # Set Python command for Render
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD="python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD="python"
    else
        echo "❌ Error: No Python found!"
        exit 1
    fi
else
    # Local development setup
    echo "   Setting up local development environment..."
    
    # Check for Python
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD="python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD="python"
    else
        echo "❌ Error: Python is required but not found!"
        exit 1
    fi
    
    # Setup virtual environment for local development
    if [ ! -d ".venv" ]; then
        echo "   Creating virtual environment..."
        $PYTHON_CMD -m venv .venv
        if [ $? -ne 0 ]; then
            echo "❌ Failed to create virtual environment"
            exit 1
        fi
    fi
    
    # Activate virtual environment
    if [ -f ".venv/bin/activate" ]; then
        echo "   Activating virtual environment..."
        source .venv/bin/activate
    fi
    
    # Install dependencies locally
    echo "   Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
fi

echo "✅ Environment ready"
echo ""

# Step 3: Validate Setup
echo "🔧 Step 3: Validating setup..."

# Check if main.py exists
if [ ! -f "src/main.py" ]; then
    echo "❌ Error: src/main.py not found!"
    exit 1
fi

# Check if docs contain API specifications
if [ ! -d "docs" ] || [ -z "$(find docs -name '*.json' -type f)" ]; then
    echo "❌ Error: No API documentation found in docs directory!"
    exit 1
fi

API_FILES=$(find docs -name '*.json' -type f | wc -l)
echo "✅ Found $API_FILES API specification files"

echo ""

# Step 4: Start the Server
echo "🎯 Step 4: Starting GoHighLevel MCP Server..."
echo "============================================="

if [ "$DEPLOYMENT_ENV" = "render" ]; then
    echo "🌐 Starting server for Render deployment..."
    echo "   Environment: Production"
    echo "   Transport: HTTP (for web service)"
    
    # Set environment variables for Render
    export MCP_TRANSPORT=http
    export MCP_HOST=0.0.0.0
    export MCP_PORT=${PORT:-8000}
    
    echo "   Binding to: $MCP_HOST:$MCP_PORT"
    
    # For Render, we'll run the health server since it needs HTTP endpoints
    echo "   Starting health check server for Render..."
    exec $PYTHON_CMD health_server.py
else
    echo "🏠 Starting server for local development..."
    echo "   Environment: Development"
    echo "   Transport: STDIO (default)"
    
    echo ""
    echo "🔑 Configure your MCP client with these credentials:"
    echo "   - GHL_API_KEY: Your GoHighLevel API key"
    echo "   - GHL_LOCATION_ID: Your GoHighLevel location ID"
    
    echo ""
    echo "🏁 Starting server now..."
    echo ""
    
    # Start the actual MCP server for local development
    exec $PYTHON_CMD src/main.py
fi
