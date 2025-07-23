# GoHighLevel MCP Server

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
├── plan.md
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