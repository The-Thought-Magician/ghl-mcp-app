from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="search-locations",
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
        "description": "The company/agency id on which you want to perform the search",
        "required": false
    },
    "skip": {
        "type": "string",
        "description": "The value by which the results should be skipped. Default will be 0",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "The value by which the results should be limited. Default will be 10",
        "required": false
    },
    "order": {
        "type": "string",
        "description": "The order in which the results should be returned - Allowed values asc, desc. Default will be asc",
        "required": false
    },
    "email": {
        "type": "string",
        "description": "",
        "required": false
    }
}
)
async def search-locations(authorization: str, version: str, compan\1_\2: Optional[str], skip: Optional[str], limit: Optional[str], order: Optional[str], email: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for search-locations",
    "path": "/locations/search",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "compan\\1_\\2": "__VAR__compan\\1_\\2__VAR__",
        "skip": skip,
        "limit": limit,
        "order": order,
        "email": email
    }
}


@Tool(
    name="get-location",
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
        "description": "Location Id",
        "required": true
    }
}
)
async def get-location(authorization: str, version: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-location",
    "path": "/locations/{locationId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="put-location",
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
        "description": "Location Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def put-location(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for put-location",
    "path": "/locations/{locationId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-location",
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
        "description": "Location Id",
        "required": true
    },
    "delet\\1_\\2_\\1ccount": {
        "type": "boolean",
        "description": "Boolean value to indicate whether to delete Twilio Account or not",
        "required": true
    }
}
)
async def delete-location(authorization: str, version: str, locatio\1_\2: str, delet\1_\2_\1ccount: bool) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-location",
    "path": "/locations/{locationId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "delet\\1_\\2_\\1ccount": "__VAR__delet\\1_\\2_\\1ccount__VAR__"
    }
}


@Tool(
    name="get-location-tags",
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
        "description": "Location Id",
        "required": true
    }
}
)
async def get-location-tags(authorization: str, version: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-location-tags",
    "path": "/locations/{locationId}/tags",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-tag",
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
        "description": "Location Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-tag(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-tag",
    "path": "/locations/{locationId}/tags",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-tag-by-id",
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
        "description": "Location Id",
        "required": true
    },
    "ta\\1_\\2": {
        "type": "string",
        "description": "Tag Id",
        "required": true
    }
}
)
async def get-tag-by-id(authorization: str, version: str, locatio\1_\2: str, ta\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-tag-by-id",
    "path": "/locations/{locationId}/tags/{tagId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "ta\\1_\\2": "__VAR__ta\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-tag",
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
        "description": "Location Id",
        "required": true
    },
    "ta\\1_\\2": {
        "type": "string",
        "description": "Tag Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-tag(authorization: str, version: str, locatio\1_\2: str, ta\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-tag",
    "path": "/locations/{locationId}/tags/{tagId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "ta\\1_\\2": "__VAR__ta\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-tag",
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
        "description": "Location Id",
        "required": true
    },
    "ta\\1_\\2": {
        "type": "string",
        "description": "Tag Id",
        "required": true
    }
}
)
async def delete-tag(authorization: str, version: str, locatio\1_\2: str, ta\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-tag",
    "path": "/locations/{locationId}/tags/{tagId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "ta\\1_\\2": "__VAR__ta\\1_\\2__VAR__"
    }
}


@Tool(
    name="task-search",
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
        "description": "Location Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def task-search(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for task-search",
    "path": "/locations/{locationId}/tasks/search",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-custom-fields",
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
        "description": "Location Id",
        "required": true
    },
    "model": {
        "type": "string",
        "description": "Model of the custom field you want to retrieve",
        "required": false
    }
}
)
async def get-custom-fields(authorization: str, version: str, locatio\1_\2: str, model: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-fields",
    "path": "/locations/{locationId}/customFields",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "model": model
    }
}


@Tool(
    name="create-custom-field",
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
        "description": "Location Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-custom-field(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-custom-field",
    "path": "/locations/{locationId}/customFields",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-custom-field",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Field Id",
        "required": true
    }
}
)
async def get-custom-field(authorization: str, version: str, locatio\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-field",
    "path": "/locations/{locationId}/customFields/{id}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="update-custom-field",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Field Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-custom-field(authorization: str, version: str, locatio\1_\2: str, id: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-custom-field",
    "path": "/locations/{locationId}/customFields/{id}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id,
        "request_body": request_body
    }
}


@Tool(
    name="delete-custom-field",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Field Id",
        "required": true
    }
}
)
async def delete-custom-field(authorization: str, version: str, locatio\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-custom-field",
    "path": "/locations/{locationId}/customFields/{id}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="upload-file-customFields",
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
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def upload-file-custo\1_\2(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for upload-file-customFields",
    "path": "/locations/{locationId}/customFields/upload",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-custom-values",
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
        "description": "Location Id",
        "required": true
    }
}
)
async def get-custom-values(authorization: str, version: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-values",
    "path": "/locations/{locationId}/customValues",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-custom-value",
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
        "description": "Location Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-custom-value(authorization: str, version: str, locatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-custom-value",
    "path": "/locations/{locationId}/customValues",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-custom-value",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Value Id",
        "required": true
    }
}
)
async def get-custom-value(authorization: str, version: str, locatio\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-custom-value",
    "path": "/locations/{locationId}/customValues/{id}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="update-custom-value",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Value Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-custom-value(authorization: str, version: str, locatio\1_\2: str, id: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-custom-value",
    "path": "/locations/{locationId}/customValues/{id}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id,
        "request_body": request_body
    }
}


@Tool(
    name="delete-custom-value",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Custom Value Id",
        "required": true
    }
}
)
async def delete-custom-value(authorization: str, version: str, locatio\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-custom-value",
    "path": "/locations/{locationId}/customValues/{id}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="get-timezones",
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
async def get-timezones(authorization: str, version: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-timezones",
    "path": "/locations/{locationId}/timezones",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version
    }
}


@Tool(
    name="GET-all-or-email-sms-templates",
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
    "deleted": {
        "type": "boolean",
        "description": "",
        "required": false
    },
    "skip": {
        "type": "string",
        "description": "",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "",
        "required": false
    },
    "type": {
        "type": "string",
        "description": "",
        "required": false
    },
    "origi\\1_\\2": {
        "type": "string",
        "description": "Origin Id",
        "required": true
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "Location Id",
        "required": true
    }
}
)
async def g_\1_\1-all-or-email-sms-templates(authorization: str, version: str, deleted: Optional[bool], skip: Optional[str], limit: Optional[str], type: Optional[str], origi\1_\2: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for GET-all-or-email-sms-templates",
    "path": "/locations/{locationId}/templates",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "deleted": deleted,
        "skip": skip,
        "limit": limit,
        "type": type,
        "origi\\1_\\2": "__VAR__origi\\1_\\2__VAR__",
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="DELETE-an-email-sms-template",
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
        "description": "Location Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Template Id",
        "required": true
    }
}
)
async def d_\1_\1_\1_\1_\1-an-email-sms-template(authorization: str, version: str, locatio\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for DELETE-an-email-sms-template",
    "path": "/locations/{locationId}/templates/{id}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="create-location",
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
async def create-location(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-location",
    "path": "/locations/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


