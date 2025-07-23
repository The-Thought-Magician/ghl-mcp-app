from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="search-contacts-advanced",
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
async def search-contacts-advanced(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for search-contacts-advanced",
    "path": "/contacts/search",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="get-duplicate-contact",
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
    "number": {
        "type": "string",
        "description": "Phone Number - Pass in URL Encoded form. i.e +1423164516 will become `%2B1423164516`",
        "required": false
    },
    "email": {
        "type": "string",
        "description": "Email - Pass in URL Encoded form. i.e test+abc@gmail.com will become `test%2Babc%40gmail.com`",
        "required": false
    }
}
)
async def get-duplicate-contact(authorization: str, version: str, locatio\1_\2: str, number: Optional[str], email: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-duplicate-contact",
    "path": "/contacts/search/duplicate",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "number": number,
        "email": email
    }
}


@Tool(
    name="get-all-tasks",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def get-all-tasks(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-all-tasks",
    "path": "/contacts/{contactId}/tasks",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-task",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-task(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-task",
    "path": "/contacts/{contactId}/tasks",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-task",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "tas\\1_\\2": {
        "type": "string",
        "description": "Task Id",
        "required": true
    }
}
)
async def get-task(authorization: str, version: str, contac\1_\2: str, tas\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-task",
    "path": "/contacts/{contactId}/tasks/{taskId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "tas\\1_\\2": "__VAR__tas\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-task",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "tas\\1_\\2": {
        "type": "string",
        "description": "Task Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-task(authorization: str, version: str, contac\1_\2: str, tas\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-task",
    "path": "/contacts/{contactId}/tasks/{taskId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "tas\\1_\\2": "__VAR__tas\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-task",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "tas\\1_\\2": {
        "type": "string",
        "description": "Task Id",
        "required": true
    }
}
)
async def delete-task(authorization: str, version: str, contac\1_\2: str, tas\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-task",
    "path": "/contacts/{contactId}/tasks/{taskId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "tas\\1_\\2": "__VAR__tas\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-task-completed",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "tas\\1_\\2": {
        "type": "string",
        "description": "Task Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-task-completed(authorization: str, version: str, contac\1_\2: str, tas\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-task-completed",
    "path": "/contacts/{contactId}/tasks/{taskId}/completed",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "tas\\1_\\2": "__VAR__tas\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-appointments-for-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def get-appointments-for-contact(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-appointments-for-contact",
    "path": "/contacts/{contactId}/appointments",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="add-tags",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def add-tags(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-tags",
    "path": "/contacts/{contactId}/tags",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="remove-tags",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def remove-tags(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for remove-tags",
    "path": "/contacts/{contactId}/tags",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-all-notes",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def get-all-notes(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-all-notes",
    "path": "/contacts/{contactId}/notes",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-note",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-note(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-note",
    "path": "/contacts/{contactId}/notes",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-note",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Note Id",
        "required": true
    }
}
)
async def get-note(authorization: str, version: str, contac\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-note",
    "path": "/contacts/{contactId}/notes/{id}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="update-note",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Note Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-note(authorization: str, version: str, contac\1_\2: str, id: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-note",
    "path": "/contacts/{contactId}/notes/{id}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "id": id,
        "request_body": request_body
    }
}


@Tool(
    name="delete-note",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Note Id",
        "required": true
    }
}
)
async def delete-note(authorization: str, version: str, contac\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-note",
    "path": "/contacts/{contactId}/notes/{id}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="create-association",
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
    "type": {
        "type": "string",
        "description": "Tags operation type",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-association(authorization: str, version: str, type: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-association",
    "path": "/contacts/bulk/tags/update/{type}",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "type": type,
        "request_body": request_body
    }
}


@Tool(
    name="add-remove-contact-from-business",
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
async def add-remove-contact-from-business(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-remove-contact-from-business",
    "path": "/contacts/bulk/business",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="get-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def get-contact(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-contact",
    "path": "/contacts/{contactId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-contact(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-contact",
    "path": "/contacts/{contactId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def delete-contact(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-contact",
    "path": "/contacts/{contactId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="upsert-contact",
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
async def upsert-contact(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for upsert-contact",
    "path": "/contacts/upsert",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="get-contacts-by-businessId",
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
    "busines\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "limit": {
        "type": "string",
        "description": "",
        "required": false
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "skip": {
        "type": "string",
        "description": "",
        "required": false
    },
    "query": {
        "type": "string",
        "description": "",
        "required": false
    }
}
)
async def get-contacts-by-busines\1_\2(authorization: str, version: str, busines\1_\2: str, limit: Optional[str], locatio\1_\2: str, skip: Optional[str], query: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-contacts-by-businessId",
    "path": "/contacts/business/{businessId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "busines\\1_\\2": "__VAR__busines\\1_\\2__VAR__",
        "limit": limit,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "skip": skip,
        "query": query
    }
}


@Tool(
    name="add-followers-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def add-followers-contact(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-followers-contact",
    "path": "/contacts/{contactId}/followers",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="remove-followers-contact",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def remove-followers-contact(authorization: str, version: str, contac\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for remove-followers-contact",
    "path": "/contacts/{contactId}/followers",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="add-contact-to-campaign",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "campaig\\1_\\2": {
        "type": "string",
        "description": "Campaigns Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def add-contact-to-campaign(authorization: str, version: str, contac\1_\2: str, campaig\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-contact-to-campaign",
    "path": "/contacts/{contactId}/campaigns/{campaignId}",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "campaig\\1_\\2": "__VAR__campaig\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="remove-contact-from-campaign",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "campaig\\1_\\2": {
        "type": "string",
        "description": "Campaigns Id",
        "required": true
    }
}
)
async def remove-contact-from-campaign(authorization: str, version: str, contac\1_\2: str, campaig\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for remove-contact-from-campaign",
    "path": "/contacts/{contactId}/campaigns/{campaignId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "campaig\\1_\\2": "__VAR__campaig\\1_\\2__VAR__"
    }
}


@Tool(
    name="remove-contact-from-every-campaign",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    }
}
)
async def remove-contact-from-every-campaign(authorization: str, version: str, contac\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for remove-contact-from-every-campaign",
    "path": "/contacts/{contactId}/campaigns/removeAll",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__"
    }
}


@Tool(
    name="add-contact-to-workflow",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "workflo\\1_\\2": {
        "type": "string",
        "description": "Workflow Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def add-contact-to-workflow(authorization: str, version: str, contac\1_\2: str, workflo\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-contact-to-workflow",
    "path": "/contacts/{contactId}/workflow/{workflowId}",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "workflo\\1_\\2": "__VAR__workflo\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-contact-to-workflow",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": true
    },
    "workflo\\1_\\2": {
        "type": "string",
        "description": "Workflow Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def delete-contact-to-workflow(authorization: str, version: str, contac\1_\2: str, workflo\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-contact-to-workflow",
    "path": "/contacts/{contactId}/workflow/{workflowId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "workflo\\1_\\2": "__VAR__workflo\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="create-contact",
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
async def create-contact(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-contact",
    "path": "/contacts/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="get-contacts",
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
    "star\\1_\\2_\\1d": {
        "type": "string",
        "description": "Start After Id",
        "required": false
    },
    "star\\1_\\2": {
        "type": "number",
        "description": "Start Afte",
        "required": false
    },
    "query": {
        "type": "string",
        "description": "Contact Query",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Limit Per Page records count. will allow maximum up to 100 and default will be 20",
        "required": false
    }
}
)
async def get-contacts(authorization: str, version: str, locatio\1_\2: str, star\1_\2_\1d: Optional[str], star\1_\2: Optional[float], query: Optional[str], limit: Optional[float]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-contacts",
    "path": "/contacts/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "star\\1_\\2_\\1d": "__VAR__star\\1_\\2_\\1d__VAR__",
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "query": query,
        "limit": limit
    }
}


