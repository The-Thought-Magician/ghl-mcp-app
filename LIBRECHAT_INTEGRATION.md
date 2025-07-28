# GoHighLevel MCP Server - LibreChat Integration

## 🚀 Quick Setup (2 Steps)

### Step 1: Configure LibreChat
Copy the configuration file to your LibreChat installation:
```bash
cp librechat.example.yaml /path/to/your/librechat/librechat.yaml
```

Edit `librechat.yaml` and update the paths and credentials:
```yaml
mcpServers:
  gohighlevel:
    name: "GoHighLevel CRM"
    command: "python"
    args: ["/full/path/to/ghl-mcp-app/src/main.py"]
    env:
      GHL_API_KEY: "your-actual-ghl-api-key"
      GHL_LOCATION_ID: "your-actual-location-id"
```

### Step 2: Restart LibreChat
Restart LibreChat to load the new MCP server configuration.

## ✅ That's it!

LibreChat will automatically start the MCP server when needed using STDIO transport (the standard MCP protocol).

## 📋 What You Get

- **Complete GoHighLevel Integration**: All API endpoints available as tools
- **STDIO Transport**: Standard MCP protocol, fully compatible with LibreChat
- **Automatic Server Management**: LibreChat starts/stops the server as needed
- **327 Generated Tools**: From contacts to campaigns to workflows

## 🔧 Getting Your GoHighLevel Credentials

1. **API Key**: Go to GoHighLevel → Settings → Integrations → API → Create Private App
2. **Location ID**: Found in your GoHighLevel account URL or settings

## 🧪 Testing (Optional)

Test the server independently:
```bash
./start.sh
```

The server will run with STDIO transport and wait for MCP commands.

## 🔧 Configuration Details

### MCP Server Features
- **327 Generated Routes** from 223 GoHighLevel API endpoints
- **32 API Modules** fully supported
- **Automatic Schema Fixing** for OpenAPI compatibility
- **Smart Route Mapping** for optimal tool organization

### GoHighLevel API Coverage
- ✅ Contacts Management
- ✅ Campaign Management  
- ✅ Opportunity Pipeline
- ✅ Calendar & Appointments
- ✅ Email Marketing
- ✅ Workflow Automation
- ✅ Payment Processing
- ✅ Social Media Posting
- ✅ Form Management
- ✅ Survey Tools
- ✅ And 22 more modules...

### LibreChat Configuration Options
- **Tool Access Control**: Whitelist/blacklist specific tools
- **Model Integration**: Works with GPT-4, Claude, and other models  
- **Timeout Settings**: Configurable request timeouts
- **Retry Logic**: Automatic retry for failed requests
- **Interface Customization**: Custom presets and model specs

## 🎯 Next Steps

1. **Start the server** with HTTP transport
2. **Copy and configure** the LibreChat YAML file
3. **Test the integration** using the provided test script
4. **Customize tool access** based on your needs
5. **Enjoy seamless GoHighLevel access** from LibreChat!

## 📚 Additional Resources

- **Main Server**: `src/main.py` - Core MCP server implementation
- **Configuration**: `.env` - Environment variables
- **Documentation**: `README.md` - Complete setup guide
- **Testing**: `test_server.py`, `test_http_server.py` - Validation scripts
- **LibreChat Config**: `librechat.example.yaml` - Integration template

The server is now ready for production use with LibreChat! 🎉
