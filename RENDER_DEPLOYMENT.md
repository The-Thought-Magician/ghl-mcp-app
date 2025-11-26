# Render.com Deployment Guide

## 🚀 Quick Deploy to Render

### Method 1: One-Click Deploy (Recommended)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/your-username/ghl-mcp-app)

### Method 2: Manual Deployment

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service** on Render.com:
   - Connect your GitHub account
   - Select your forked repository
   - Choose "Web Service"

3. **Configure the service:**
   ```
   Name: ghl-mcp-server
   Environment: Python
   Build Command: (leave empty - dependencies auto-installed)
   Start Command: ./start-render.sh
   ```

4. **Set Environment Variables** in Render dashboard:
   ```
   GHL_API_KEY=your-actual-gohighlevel-api-key
   GHL_LOCATION_ID=your-actual-location-id
   GHL_BASE_URL=https://services.leadconnectorhq.com
   PYTHON_VERSION=3.11
   ```

5. **Deploy** - Render will automatically build and deploy your service

## 📋 Environment Variables

Required environment variables for Render deployment:

| Variable | Description | Required |
|----------|-------------|----------|
| `GHL_API_KEY` | Your GoHighLevel API key | ✅ Yes |
| `GHL_LOCATION_ID` | Your GoHighLevel location ID | ✅ Yes |
| `GHL_BASE_URL` | GoHighLevel API base URL | ❌ No (defaults to official API) |
| `PYTHON_VERSION` | Python version for Render | ❌ No (defaults to 3.11) |

## 🔧 How It Works on Render

1. **Automatic Setup**: The `start-render.sh` script detects Render environment
2. **Documentation Clone**: Automatically clones GoHighLevel API docs
3. **Dependency Installation**: Render installs Python packages from `requirements.txt`
4. **Health Endpoints**: Provides `/health` and `/` endpoints for Render monitoring
5. **Service Ready**: Your MCP server is accessible via the Render URL

## 🌐 Accessing Your Deployed Server

After deployment, your server will be available at:
```
https://your-service-name.onrender.com
```

### Endpoints:
- `GET /` - Service information
- `GET /health` - Health check (for Render monitoring)
- `POST /mcp` - MCP protocol endpoint (if using HTTP transport)

## 🔗 Integrating with MCP Clients

### For Claude Desktop:
```json
{
  "mcpServers": {
    "gohighlevel": {
      "command": "python",
      "args": ["path/to/local/ghl-mcp-app/src/main.py"],
      "env": {
        "GHL_API_KEY": "your-api-key",
        "GHL_LOCATION_ID": "your-location-id"
      }
    }
  }
}
```

### For LibreChat (HTTP):
```yaml
mcpServers:
  gohighlevel:
    name: "GoHighLevel CRM"
    url: "https://your-service-name.onrender.com/mcp"
    env:
      GHL_API_KEY: "your-api-key"
      GHL_LOCATION_ID: "your-location-id"
```

## 🚨 Important Notes

1. **Free Tier Limitations**: 
   - Render free tier may have cold start delays
   - Service may sleep after 15 minutes of inactivity
   - Consider upgrading for production use

2. **API Keys Security**:
   - Always set API keys as environment variables in Render dashboard
   - Never commit API keys to your repository

3. **Documentation Updates**:
   - The server automatically clones/updates GoHighLevel API docs on startup
   - No manual intervention needed for API updates

## 🐛 Troubleshooting

### Common Issues:

**Build Fails:**
- Check that `requirements.txt` is in the root directory
- Verify Python version compatibility
- Check Render build logs for specific errors

**Service Won't Start:**
- Verify `start-render.sh` is executable
- Check environment variables are set correctly
- Review Render service logs

**API Calls Fail:**
- Verify `GHL_API_KEY` is correct and valid
- Check `GHL_LOCATION_ID` is properly set
- Ensure GoHighLevel API permissions are sufficient

### Debug Mode:

Add these environment variables for verbose logging:
```
FASTMCP_LOG_LEVEL=DEBUG
PYTHONUNBUFFERED=1
```

## 📈 Monitoring

Render provides built-in monitoring for:
- Service health (via `/health` endpoint)
- CPU and memory usage
- Request logs and metrics
- Automatic restarts on failures

## 🔄 Updates and Maintenance

### Automatic Updates:
- Push to your main branch triggers automatic redeployment
- GoHighLevel API docs are updated on each restart

### Manual Updates:
- Update environment variables in Render dashboard
- Redeploy from Render dashboard if needed
- Monitor service logs for any issues

Your GoHighLevel MCP server is now ready for production use on Render! 🎉
