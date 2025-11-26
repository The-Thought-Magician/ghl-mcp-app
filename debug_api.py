#!/usr/bin/env python3
"""
Debug GoHighLevel API authentication and test different endpoints.
"""

import asyncio
import httpx
import json

# Test credentials
TEST_API_KEY = "pit-8b61a361-d737-428a-940f-84d7154993ce"
TEST_LOCATION_ID = "9BxwBFwrflBscrRO9k20"

async def test_different_auth_methods():
    """Test different authentication methods and endpoints."""
    
    print("🔍 Debugging GoHighLevel API Authentication")
    print("=" * 50)
    
    # Different base URLs to try
    base_urls = [
        "https://services.leadconnectorhq.com",
        "https://rest.gohighlevel.com/v1",
        "https://api.gohighlevel.com/v1"
    ]
    
    # Different authentication header combinations
    auth_methods = [
        {
            "name": "Bearer token only",
            "headers": {
                "Authorization": f"Bearer {TEST_API_KEY}",
                "Content-Type": "application/json"
            }
        },
        {
            "name": "X-API-KEY only", 
            "headers": {
                "X-API-KEY": TEST_API_KEY,
                "Content-Type": "application/json"
            }
        },
        {
            "name": "Both Bearer and X-API-KEY",
            "headers": {
                "Authorization": f"Bearer {TEST_API_KEY}",
                "X-API-KEY": TEST_API_KEY,
                "Content-Type": "application/json"
            }
        },
        {
            "name": "API-KEY header",
            "headers": {
                "API-KEY": TEST_API_KEY,
                "Content-Type": "application/json"
            }
        }
    ]
    
    # Different endpoints to try
    endpoints = [
        f"/locations/{TEST_LOCATION_ID}",
        "/locations/",
        f"/locations/{TEST_LOCATION_ID}/contacts",
        "/contacts/",
        "/users/",
        "/oauth/token/info"
    ]
    
    print(f"🔑 Testing API Key: {TEST_API_KEY[:20]}...")
    print(f"📍 Testing Location ID: {TEST_LOCATION_ID}")
    print()
    
    successful_calls = []
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        
        for base_url in base_urls:
            print(f"🌐 Testing base URL: {base_url}")
            
            for auth_method in auth_methods:
                print(f"  🔐 {auth_method['name']}")
                
                for endpoint in endpoints:
                    url = f"{base_url}{endpoint}"
                    
                    try:
                        response = await client.get(url, headers=auth_method['headers'])
                        status_code = response.status_code
                        
                        if status_code == 200:
                            print(f"    ✅ {endpoint} - SUCCESS (200)")
                            successful_calls.append({
                                'url': url,
                                'auth': auth_method['name'],
                                'endpoint': endpoint,
                                'response': response.text[:200]
                            })
                        elif status_code == 401:
                            print(f"    🔑 {endpoint} - AUTH FAILED (401)")
                        elif status_code == 403:
                            print(f"    🚫 {endpoint} - FORBIDDEN (403)")
                        elif status_code == 404:
                            print(f"    🔍 {endpoint} - NOT FOUND (404)")
                        elif status_code == 429:
                            print(f"    ⏰ {endpoint} - RATE LIMITED (429)")
                        else:
                            print(f"    ❓ {endpoint} - STATUS {status_code}")
                            
                    except Exception as e:
                        print(f"    ❌ {endpoint} - ERROR: {str(e)[:50]}")
                
                print()  # Space between auth methods
            
            print()  # Space between base URLs
    
    # Show results
    print("=" * 50)
    print("📊 AUTHENTICATION TEST RESULTS")
    print("=" * 50)
    
    if successful_calls:
        print(f"✅ Found {len(successful_calls)} successful API calls!")
        print()
        for call in successful_calls:
            print(f"🎉 SUCCESS: {call['auth']}")
            print(f"   URL: {call['url']}")
            print(f"   Response: {call['response'][:100]}...")
            print()
            
        return True
    else:
        print("❌ No successful API calls found")
        print()
        print("🔍 Possible issues:")
        print("   • API key is invalid or expired")
        print("   • API key doesn't have required permissions")
        print("   • Location ID is incorrect")
        print("   • API endpoint URLs have changed")
        print("   • Account restrictions or suspension")
        print()
        print("💡 Recommendations:")
        print("   • Check your GoHighLevel account dashboard")
        print("   • Verify API key permissions and scopes")
        print("   • Try generating a new API key")
        print("   • Check if the location ID is correct")
        
        return False

async def test_token_info():
    """Test the token info endpoint to verify API key."""
    
    print("🔍 Testing API Token Information")
    print("=" * 40)
    
    # Common token info endpoints
    token_endpoints = [
        "https://services.leadconnectorhq.com/oauth/token/info",
        "https://rest.gohighlevel.com/v1/oauth/token/info", 
        "https://api.gohighlevel.com/v1/oauth/token/info",
        "https://services.leadconnectorhq.com/oauth/userinfo",
        "https://rest.gohighlevel.com/v1/oauth/userinfo"
    ]
    
    headers = {
        "Authorization": f"Bearer {TEST_API_KEY}",
        "X-API-KEY": TEST_API_KEY,
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        for endpoint in token_endpoints:
            try:
                print(f"🔍 Testing: {endpoint}")
                response = await client.get(endpoint, headers=headers)
                
                if response.status_code == 200:
                    print(f"✅ Token info retrieved successfully!")
                    try:
                        data = response.json()
                        print(f"📊 Token data: {json.dumps(data, indent=2)}")
                    except:
                        print(f"📄 Raw response: {response.text}")
                    return True
                else:
                    print(f"❌ Status: {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
            
            print()
    
    return False

def main():
    """Main debug function."""
    print("🐛 GoHighLevel API Authentication Debug")
    print("=" * 60)
    
    auth_success = asyncio.run(test_different_auth_methods())
    token_success = asyncio.run(test_token_info())
    
    print("=" * 60)
    print("🎯 DEBUG SUMMARY")
    print("=" * 60)
    
    if auth_success or token_success:
        print("✅ Found working authentication method!")
        print("   Your MCP server should work with the correct API setup.")
    else:
        print("❌ No working authentication found")
        print("   Please check your GoHighLevel API credentials.")
        print()
        print("🔧 Next steps:")
        print("   1. Log into your GoHighLevel account")
        print("   2. Go to Settings > API")
        print("   3. Generate a new API key")
        print("   4. Verify the location ID")
        print("   5. Check API permissions and scopes")

if __name__ == "__main__":
    main()
