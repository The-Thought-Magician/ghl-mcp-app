from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="get-surveys-submissions",
    description="{description}",
    parameters={
    "authorization": {
        "type": "string",
        "description": "Access Token",
        "required": true
    },
    "version": {
        "type": "string",
        "description": "API Version",
        "required": true
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "page": {
        "type": "number",
        "description": "Page No. By default it will be 1",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Limit Per Page records count. will allow maximum up to 100 and default will be 20",
        "required": false
    },
    "surve\\1_\\2": {
        "type": "string",
        "description": "Filter submission by survey id",
        "required": false
    },
    "q": {
        "type": "string",
        "description": "Filter by contactId, name, email or phone no.",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "Get submission by starting of this date. By default it will be same date of last month(YYYY-MM-DD).",
        "required": false
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "Get submission by ending of this date. By default it will be current date(YYYY-MM-DD).",
        "required": false
    }
}
)
async def get-surveys-submissions(authorization: str, version: str, locatio\1_\2: str, page: Optional[float], limit: Optional[float], surve\1_\2: Optional[str], q: Optional[str], star\1_\2: Optional[str], en\1_\2: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-surveys-submissions",
    "path": "/surveys/submissions",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "page": page,
        "limit": limit,
        "surve\\1_\\2": "__VAR__surve\\1_\\2__VAR__",
        "q": q,
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-surveys",
    description="{description}",
    parameters={
    "authorization": {
        "type": "string",
        "description": "Access Token",
        "required": true
    },
    "version": {
        "type": "string",
        "description": "API Version",
        "required": true
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "skip": {
        "type": "number",
        "description": "",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Limit Per Page records count. will allow maximum up to 50 and default will be 10",
        "required": false
    },
    "type": {
        "type": "string",
        "description": "",
        "required": false
    }
}
)
async def get-surveys(authorization: str, version: str, locatio\1_\2: str, skip: Optional[float], limit: Optional[float], type: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-surveys",
    "path": "/surveys/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "skip": skip,
        "limit": limit,
        "type": type
    }
}


