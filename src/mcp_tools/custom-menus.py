from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="get-custom-menu-by-id",
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
    "custo\\1_\\2_\\1d": {
        "type": "string",
        "description": "Unique identifier of the custom menu",
        "required": true
    }
}
)
async def get-custom-menu-by-id(authorization: str, version: str, custo\1_\2_\1d: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-menu-by-id",
    "path": "/custom-menus/{customMenuId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "custo\\1_\\2_\\1d": "__VAR__custo\\1_\\2_\\1d__VAR__"
    }
}


@Tool(
    name="delete-custom-menu",
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
    "custo\\1_\\2_\\1d": {
        "type": "string",
        "description": "ID of the custom menu to delete",
        "required": true
    }
}
)
async def delete-custom-menu(authorization: str, version: str, custo\1_\2_\1d: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-custom-menu",
    "path": "/custom-menus/{customMenuId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "custo\\1_\\2_\\1d": "__VAR__custo\\1_\\2_\\1d__VAR__"
    }
}


@Tool(
    name="update-custom-menu",
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
    "custo\\1_\\2_\\1d": {
        "type": "string",
        "description": "ID of the custom menu to update",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-custom-menu(authorization: str, version: str, custo\1_\2_\1d: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-custom-menu",
    "path": "/custom-menus/{customMenuId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "custo\\1_\\2_\\1d": "__VAR__custo\\1_\\2_\\1d__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-custom-menus",
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
        "description": "Unique identifier of the location",
        "required": false
    },
    "skip": {
        "type": "number",
        "description": "Number of items to skip for pagination",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Maximum number of items to return",
        "required": false
    },
    "query": {
        "type": "string",
        "description": "Search query to filter custom menus by name, supports partial || full names",
        "required": false
    },
    "sho\\1_\\2_\\1ompany": {
        "type": "boolean",
        "description": "Filter to show only agency-level menu links. When omitted, fetches both agency and sub-account menu links. Ignored if locationId is provided",
        "required": false
    }
}
)
async def get-custom-menus(authorization: str, version: str, locatio\1_\2: Optional[str], skip: Optional[float], limit: Optional[float], query: Optional[str], sho\1_\2_\1ompany: Optional[bool]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-menus",
    "path": "/custom-menus/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "skip": skip,
        "limit": limit,
        "query": query,
        "sho\\1_\\2_\\1ompany": "__VAR__sho\\1_\\2_\\1ompany__VAR__"
    }
}


@Tool(
    name="create-custom-menu",
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
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-custom-menu(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-custom-menu",
    "path": "/custom-menus/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


