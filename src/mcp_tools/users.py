from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="search-users",
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
    "compan\\1_\\2": {
        "type": "string",
        "description": "Company ID in which the search needs to be performed",
        "required": true
    },
    "query": {
        "type": "string",
        "description": "The search term for the user is matched based on the user full name, email or phone",
        "required": false
    },
    "skip": {
        "type": "string",
        "description": "No of results to be skipped before returning the result",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "No of results to be limited before returning the result",
        "required": false
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "Location ID in which the search needs to be performed",
        "required": false
    },
    "type": {
        "type": "string",
        "description": "Type of the users to be filtered in the search",
        "required": false
    },
    "role": {
        "type": "string",
        "description": "Role of the users to be filtered in the search",
        "required": false
    },
    "ids": {
        "type": "string",
        "description": "List of User IDs to be filtered in the search",
        "required": false
    },
    "sort": {
        "type": "string",
        "description": "The field on which sort is applied in which the results need to be sorted. Default is based on the first and last name",
        "required": false
    },
    "sor\\1_\\2": {
        "type": "string",
        "description": "The direction in which the results need to be sorted",
        "required": false
    },
    "enabled2wa\\1_\\2": {
        "type": "boolean",
        "description": "",
        "required": false
    }
}
)
async def search-users(authorization: str, version: str, compan\1_\2: str, query: Optional[str], skip: Optional[str], limit: Optional[str], locatio\1_\2: Optional[str], type: Optional[str], role: Optional[str], ids: Optional[str], sort: Optional[str], sor\1_\2: Optional[str], enabled2wa\1_\2: Optional[bool]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for search-users",
    "path": "/users/search",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "compan\\1_\\2": "__VAR__compan\\1_\\2__VAR__",
        "query": query,
        "skip": skip,
        "limit": limit,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "type": type,
        "role": role,
        "ids": ids,
        "sort": sort,
        "sor\\1_\\2": "__VAR__sor\\1_\\2__VAR__",
        "enabled2wa\\1_\\2": "__VAR__enabled2wa\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-user",
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
    }
}
)
async def get-user(authorization: str, version: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-user",
    "path": "/users/{userId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version
    }
}


@Tool(
    name="update-user",
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
async def update-user(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-user",
    "path": "/users/{userId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="delete-user",
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
    }
}
)
async def delete-user(authorization: str, version: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-user",
    "path": "/users/{userId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version
    }
}


@Tool(
    name="get-user-by-location",
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
    }
}
)
async def get-user-by-location(authorization: str, version: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-user-by-location",
    "path": "/users/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-user",
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
async def create-user(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-user",
    "path": "/users/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


