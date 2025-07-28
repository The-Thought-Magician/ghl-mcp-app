# GoHighLevel MCP Server

A Model Context Protocol (MCP) server that provides access to the complete GoHighLevel API through intelligent tool generation. This server automatically converts GoHighLevel's OpenAPI specifications into MCP tools, enabling seamless integration with AI assistants and LLM clients.

## 🌟 Features

- **Automatic Tool Generation**: Dynamically generates MCP tools from GoHighLevel OpenAPI specifications
- **Complete API Coverage**: Supports all 223+ GoHighLevel API endpoints across 32 modules
- **Smart Authentication**: Built-in support for GoHighLevel's Bearer token authentication
- **Schema Validation**: Automatic fixing of OpenAPI schema issues for reliable operation
- **FastMCP Integration**: Built on the modern FastMCP framework for optimal performance
- **Easy Updates**: Simply update the docs folder to get the latest API changes

## 📋 Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) for dependency management
- GoHighLevel API access token

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <repository-url>
cd ghl-mcp-app
```

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv pip install fastmcp aiohttp pydantic python-dotenv
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your GoHighLevel API key
```

### 5. Run the Server

```bash
python src/main.py
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Required: Your GoHighLevel API key
GHL_API_KEY=your-api-key-here

# Optional: GoHighLevel API base URL (defaults to official API)
GHL_BASE_URL=https://services.leadconnectorhq.com

# Optional: Enable experimental OpenAPI parser
FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true
```

### Getting Your API Key

1. Log into your GoHighLevel account
2. Go to Settings → Integrations → API
3. Create a new private application
4. Copy the API key to your `.env` file

## 🏗️ Architecture

### Project Structure

```
ghl-mcp-app/
├── src/
│   └── main.py              # Main MCP server implementation
├── docs/                    # GoHighLevel API documentation
│   ├── contacts/
│   ├── campaigns/
│   ├── opportunities/
│   └── ... (32 API modules)
├── scripts/
│   └── generate_tools.py    # Legacy tool generation script (reference only)
├── test_server.py           # Server validation script
├── .env.example             # Environment configuration template
└── README.md               # This file
```

### How It Works

1. **Documentation Loading**: The server scans the `docs/` directory for OpenAPI JSON specifications
2. **Schema Merging**: All individual API modules are merged into a unified OpenAPI specification
3. **Schema Fixing**: Common GoHighLevel schema issues are automatically corrected
4. **Tool Generation**: FastMCP converts each API endpoint into an MCP tool
5. **Route Mapping**: Custom route mappings organize tools by HTTP method and functionality

## 🔧 API Coverage

The server provides access to all major GoHighLevel API modules:

### Core CRM
- **Contacts**: Create, search, update, and manage contacts
- **Companies**: Company management and relationships
- **Opportunities**: Sales pipeline and deal management

### Marketing & Communication
- **Campaigns**: Marketing campaign management
- **Emails**: Email marketing and automation
- **Conversations**: Chat and messaging
- **Social Media**: Social media posting and management

### Business Operations
- **Calendars**: Appointment scheduling and management
- **Workflows**: Automation and workflow management
- **Forms**: Lead capture and form management
- **Surveys**: Customer feedback and surveys

### E-commerce & Payments
- **Products**: Product catalog management
- **Invoices**: Billing and invoice management
- **Payments**: Payment processing

### Platform & Integration
- **OAuth**: Authentication and authorization
- **Webhooks**: Event-driven integrations
- **Locations**: Multi-location management
- **Users**: User management and permissions

## 🧪 Testing

Test the server setup:

```bash
python test_server.py
```

This will validate that:
- All OpenAPI specifications load correctly
- Schema issues are resolved
- The MCP server creates successfully
- Tools are generated from API endpoints

## 🔄 Updating API Documentation

To get the latest GoHighLevel API changes:

1. Update the documentation:
   ```bash
   cd docs
   git pull origin main
   ```

2. Restart the server:
   ```bash
   python src/main.py
   ```

The server will automatically detect and incorporate any new or updated API endpoints.

## 🎯 Usage with AI Clients

Once running, the MCP server exposes all GoHighLevel API endpoints as tools that can be used by compatible AI clients:

### Example Tool Categories

- **Search Tools**: `search-contacts-advanced`, `search-opportunities`, etc.
- **Creation Tools**: `create-contact`, `create-opportunity`, etc.
- **Management Tools**: `update-contact`, `delete-campaign`, etc.
- **Retrieval Tools**: `get-contact`, `get-campaign-details`, etc.

### Tool Organization

All tools are tagged with:
- `ghl`: Identifies GoHighLevel tools
- `api`: Marks as API tools
- `read`: Added to GET endpoints
- `crm`, `marketing`: Category tags

## 🛡️ Security & Authentication

- API keys are handled securely through environment variables
- All requests include proper authentication headers
- The server validates API key presence before making requests
- No API keys are logged or exposed in error messages

## 🐛 Troubleshooting

### Common Issues

**Server won't start**: 
- Check that all dependencies are installed
- Verify Python 3.11+ is being used
- Ensure virtual environment is activated

**API authentication errors**:
- Verify your GHL_API_KEY is correct
- Check that your GoHighLevel app has the necessary permissions
- Ensure the API key hasn't expired

**Missing tools**:
- Check that all JSON files in docs/ are valid OpenAPI specs
- Review server logs for schema validation errors
- Try enabling the experimental parser

### Debug Mode

Enable verbose logging by setting:
```bash
export FASTMCP_LOG_LEVEL=DEBUG
```

## 📈 Performance

- **Cold Start**: ~3-5 seconds (loads 32 API modules)
- **Tool Generation**: 327 tools from 223 endpoints
- **Memory Usage**: ~50-100MB depending on client connections
- **Request Latency**: Depends on GoHighLevel API response times

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `python test_server.py`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Resources

- [GoHighLevel API Documentation](https://highlevel.stoplight.io/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://gofastmcp.com/)
- [GoHighLevel Developer Portal](https://developers.gohighlevel.com/)

---

**Note**: This is an unofficial tool and is not affiliated with or endorsed by GoHighLevel. Use in accordance with GoHighLevel's API terms of service.

This project aims to create a Multi-Channel Platform (MCP) server using the `fastmcp` Python library. The server will expose GoHighLevel API endpoints as `fastmcp` tools, with the unique capability of dynamically generating these tools directly from the official GoHighLevel API documentation. This ensures that the server's API tools remain up-to-date with any changes in the GoHighLevel API.

## Features

- **Dynamic Tool Generation:** Automatically generates `fastmcp` tools from the GoHighLevel API documentation, ensuring up-to-date API integration.
- **Private Integration Key Authentication:** Securely handles authentication using GoHighLevel's private integration keys.
- **`fastmcp` Powered:** Leverages the `fastmcp` library for efficient and scalable MCP server implementation.
- **`uv` for Environment Management:** Utilizes `uv` for fast and reliable virtual environment and dependency management.

## Project Structure

```
./
├── .gitignore
├── LICENSE
├── README.md
├── .venv/                # Python virtual environment (managed by uv)
├── docs/                 # Cloned GoHighLevel API documentation
│   └── highlevel-api-docs/
│       └── ...
├── scripts/              # Scripts for tool generation and other utilities
│   └── generate_tools.py
└── src/                  # Main application source code
    └── main.py
    └── mcp_tools/        # Dynamically generated fastmcp tools
        └── __init__.py
        └── ...
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- `uv` (can be installed globally via `pip install uv` or `brew install uv`)

### Steps

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate the virtual environment:**

    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    uv pip install fastmcp
    ```

4.  **Clone GoHighLevel API Documentation:**

    The project relies on the official GoHighLevel API documentation to generate its tools. Clone it into the `docs/` directory:

    ```bash
    git clone https://github.com/GoHighLevel/highlevel-api-docs.git docs/
    ```

## Usage

### Generating API Tools

Before running the server, you need to generate the `fastmcp` tools from the GoHighLevel API documentation. This is done via a script:

```bash
python scripts/generate_tools.py
```

*(Note: This script is yet to be implemented.)*

### Running the MCP Server

To start the `fastmcp` server:

```bash
python src/main.py
```

*(Note: The server implementation is yet to be completed.)*

### Authentication

Authentication with the GoHighLevel API will be handled using a **Private Integration Key**. You will need to set this key as an environment variable (e.g., `GOHIGHLEVEL_PRIVATE_KEY`) before running the server.

```bash
export GOHIGHLEVEL_PRIVATE_KEY="your_private_integration_key"
```

## Updating API Tools

To ensure your MCP server's tools are always up-to-date with the latest GoHighLevel API changes, simply pull the latest changes from the `highlevel-api-docs` repository and re-run the tool generation script:

```bash
cd docs/highlevel-api-docs
git pull origin main
cd ../..
python scripts/generate_tools.py
```

## Contributing

(To be added later)

## License

(To be added later)