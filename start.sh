#!/bin/bash

# Complete GoHighLevel MCP Server setup and startup script

echo "🚀 GoHighLevel MCP Server - Complete Setup & Start"
echo "=================================================="

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required tools
echo "🔍 Checking prerequisites..."

# Check for Python
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python is required but not found!"
    echo "   Please install Python 3.11+ and try again."
    exit 1
fi

echo "✅ Python found: $($PYTHON_CMD --version)"

# Check for git
if ! command_exists git; then
    echo "❌ Error: Git is required but not found!"
    echo "   Please install Git and try again."
    exit 1
fi

echo "✅ Git found: $(git --version)"

# Check for uv (optional but recommended)
if command_exists uv; then
    UV_AVAILABLE=true
    echo "✅ uv found: $(uv --version)"
else
    UV_AVAILABLE=false
    echo "⚠️  uv not found - will use pip instead"
    echo "   Install uv for faster dependency management: pip install uv"
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

# Step 2: Setup Python Virtual Environment
echo "🐍 Step 2: Setting up Python environment..."

if [ ! -d ".venv" ]; then
    echo "   Creating virtual environment..."
    if [ "$UV_AVAILABLE" = true ]; then
        uv venv
    else
        $PYTHON_CMD -m venv .venv
    fi
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "   Activating virtual environment..."
source .venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

echo "✅ Virtual environment activated"
echo ""

# Step 3: Install Dependencies
echo "📦 Step 3: Installing dependencies..."

# Check if requirements file exists, create if not
if [ ! -f "requirements.txt" ]; then
    echo "   Creating requirements.txt..."
    cat > requirements.txt << EOF
fastmcp>=2.0.0
httpx>=0.25.0
pydantic>=2.0.0
python-dotenv>=1.0.0
aiohttp>=3.8.0
EOF
    echo "✅ requirements.txt created"
fi

# Install dependencies
echo "   Installing Python packages..."
if [ "$UV_AVAILABLE" = true ]; then
    uv pip install -r requirements.txt
else
    pip install -r requirements.txt
fi

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully"
echo ""

# Step 4: Setup Environment File
echo "⚙️  Step 4: Checking environment configuration..."

if [ ! -f ".env" ]; then
    echo "   Creating .env file from template..."
    cat > .env << 'EOF'
# GoHighLevel MCP Server Configuration

# MCP Server Transport Configuration
# stdio = Standard MCP transport (recommended)
# http = HTTP transport (for specific integrations)
MCP_TRANSPORT=stdio
MCP_HOST=127.0.0.1
MCP_PORT=8000

# Note: GoHighLevel API credentials (GHL_API_KEY, GHL_LOCATION_ID) 
# should be configured in your MCP client (Claude Desktop, LibreChat, etc.)

# Optional: Set to true to enable FastMCP's experimental OpenAPI parser
# FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true
EOF
    echo "✅ .env file created"
    echo "   📝 Remember to configure your GoHighLevel API credentials in your MCP client!"
else
    echo "✅ .env file already exists"
fi

echo ""

# Step 5: Validate Setup
echo "🔧 Step 5: Validating setup..."

# Check if main.py exists
if [ ! -f "src/main.py" ]; then
    echo "❌ Error: src/main.py not found!"
    echo "   Make sure you're in the correct directory with the MCP server code."
    exit 1
fi

# Check if docs contain API specifications
if [ ! -d "docs" ] || [ -z "$(find docs -name '*.json' -type f)" ]; then
    echo "❌ Error: No API documentation found in docs directory!"
    echo "   The documentation cloning may have failed."
    exit 1
fi

API_FILES=$(find docs -name '*.json' -type f | wc -l)
echo "✅ Found $API_FILES API specification files"

echo ""

# Step 6: Start the Server
echo "🎯 Step 6: Starting GoHighLevel MCP Server..."
echo "============================================="
echo ""
echo "🔑 IMPORTANT: Make sure to configure your GoHighLevel credentials in your MCP client:"
echo "   - GHL_API_KEY: Your GoHighLevel API key"
echo "   - GHL_LOCATION_ID: Your GoHighLevel location ID"
echo ""
echo "📱 For Claude Desktop, add this to claude_desktop_config.json:"
echo '   {'
echo '     "mcpServers": {'
echo '       "gohighlevel": {'
echo '         "command": "python",'
echo '         "args": ["'$(pwd)'/src/main.py"],'
echo '         "env": {'
echo '           "GHL_API_KEY": "your-api-key",'
echo '           "GHL_LOCATION_ID": "your-location-id"'
echo '         }'
echo '       }'
echo '     }'
echo '   }'
echo ""
echo "🏁 Starting server now..."
echo ""

# Start the server
$PYTHON_CMD src/main.py
