from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="search-conversation",
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
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact Id",
        "required": false
    },
    "assigne\\1_\\2": {
        "type": "string",
        "description": "User IDs that conversations are assigned to. Multiple IDs can be provided as comma-separated values. Use \\\"unassigned\\\" to fetch conversations not assigned to any user.",
        "required": false
    },
    "followers": {
        "type": "string",
        "description": "User IDs of followers to filter conversations by. Multiple IDs can be provided as comma-separated values.",
        "required": false
    },
    "mentions": {
        "type": "string",
        "description": "User Id of the mention. Multiple values are comma separated.",
        "required": false
    },
    "query": {
        "type": "string",
        "description": "Search paramater as a string",
        "required": false
    },
    "sort": {
        "type": "string",
        "description": "Sort paramater - asc or desc",
        "required": false
    },
    "star\\1_\\2_\\1ate": {
        "type": "any",
        "description": "Search to begin after the specified date - should contain the sort value of the last document",
        "required": false
    },
    "id": {
        "type": "string",
        "description": "Id of the conversation",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Limit of conversations - Default is 20",
        "required": false
    },
    "las\\1_\\2_\\1ype": {
        "type": "string",
        "description": "Type of the last message in the conversation as a string",
        "required": false
    },
    "las\\1_\\2_\\1ction": {
        "type": "string",
        "description": "Action of the last outbound message in the conversation as string.",
        "required": false
    },
    "las\\1_\\2_\\1irection": {
        "type": "string",
        "description": "Direction of the last message in the conversation as string.",
        "required": false
    },
    "status": {
        "type": "string",
        "description": "The status of the conversation to be filtered - all, read, unread, starred ",
        "required": false
    },
    "sor\\1_\\2": {
        "type": "string",
        "description": "The sorting of the conversation to be filtered as - manual messages or all messages",
        "required": false
    },
    "sor\\1_\\2_\\1rofile": {
        "type": "string",
        "description": "Id of score profile on which sortBy.ScoreProfile should sort on",
        "required": false
    },
    "scor\\1_\\2": {
        "type": "string",
        "description": "Id of score profile on which conversations should get filtered out, works with scoreProfileMin & scoreProfileMax",
        "required": false
    },
    "scor\\1_\\2_\\1in": {
        "type": "number",
        "description": "Minimum value for score",
        "required": false
    },
    "scor\\1_\\2_\\1ax": {
        "type": "number",
        "description": "Maximum value for score",
        "required": false
    }
}
)
async def search-conversation(authorization: str, version: str, locatio\1_\2: str, contac\1_\2: Optional[str], assigne\1_\2: Optional[str], followers: Optional[str], mentions: Optional[str], query: Optional[str], sort: Optional[str], star\1_\2_\1ate: Optional[Any], id: Optional[str], limit: Optional[float], las\1_\2_\1ype: Optional[str], las\1_\2_\1ction: Optional[str], las\1_\2_\1irection: Optional[str], status: Optional[str], sor\1_\2: Optional[str], sor\1_\2_\1rofile: Optional[str], scor\1_\2: Optional[str], scor\1_\2_\1in: Optional[float], scor\1_\2_\1ax: Optional[float]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for search-conversation",
    "path": "/conversations/search",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "assigne\\1_\\2": "__VAR__assigne\\1_\\2__VAR__",
        "followers": followers,
        "mentions": mentions,
        "query": query,
        "sort": sort,
        "star\\1_\\2_\\1ate": "__VAR__star\\1_\\2_\\1ate__VAR__",
        "id": id,
        "limit": limit,
        "las\\1_\\2_\\1ype": "__VAR__las\\1_\\2_\\1ype__VAR__",
        "las\\1_\\2_\\1ction": "__VAR__las\\1_\\2_\\1ction__VAR__",
        "las\\1_\\2_\\1irection": "__VAR__las\\1_\\2_\\1irection__VAR__",
        "status": status,
        "sor\\1_\\2": "__VAR__sor\\1_\\2__VAR__",
        "sor\\1_\\2_\\1rofile": "__VAR__sor\\1_\\2_\\1rofile__VAR__",
        "scor\\1_\\2": "__VAR__scor\\1_\\2__VAR__",
        "scor\\1_\\2_\\1in": "__VAR__scor\\1_\\2_\\1in__VAR__",
        "scor\\1_\\2_\\1ax": "__VAR__scor\\1_\\2_\\1ax__VAR__"
    }
}


@Tool(
    name="get-conversation",
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
    "conversatio\\1_\\2": {
        "type": "string",
        "description": "Conversation ID as string",
        "required": true
    }
}
)
async def get-conversation(authorization: str, version: str, conversatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-conversation",
    "path": "/conversations/{conversationId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "conversatio\\1_\\2": "__VAR__conversatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-conversation",
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
    "conversatio\\1_\\2": {
        "type": "string",
        "description": "Conversation ID as string",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-conversation(authorization: str, version: str, conversatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-conversation",
    "path": "/conversations/{conversationId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "conversatio\\1_\\2": "__VAR__conversatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-conversation",
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
    "conversatio\\1_\\2": {
        "type": "string",
        "description": "Conversation ID as string",
        "required": true
    }
}
)
async def delete-conversation(authorization: str, version: str, conversatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-conversation",
    "path": "/conversations/{conversationId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "conversatio\\1_\\2": "__VAR__conversatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-email-by-id",
    description="{description}",
    parameters={
    "authorization": {
        "type": "string",
        "description": "Access Token",
        "required": true
    }
}
)
async def get-email-by-id(authorization: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-email-by-id",
    "path": "/conversations/messages/email/{id}",
    "method": "get",
    "params": {
        "authorization": authorization
    }
}


@Tool(
    name="cancel-scheduled-email-message",
    description="{description}",
    parameters={
    "authorization": {
        "type": "string",
        "description": "Access Token",
        "required": true
    },
    "emai\\1_\\2_\\1d": {
        "type": "string",
        "description": "Email Message Id",
        "required": true
    }
}
)
async def cancel-scheduled-email-message(authorization: str, emai\1_\2_\1d: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for cancel-scheduled-email-message",
    "path": "/conversations/messages/email/{emailMessageId}/schedule",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "emai\\1_\\2_\\1d": "__VAR__emai\\1_\\2_\\1d__VAR__"
    }
}


@Tool(
    name="get-message",
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
async def get-message(authorization: str, version: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-message",
    "path": "/conversations/messages/{id}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version
    }
}


@Tool(
    name="get-messages",
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
    "conversatio\\1_\\2": {
        "type": "string",
        "description": "Conversation ID as string",
        "required": true
    },
    "las\\1_\\2_\\1d": {
        "type": "string",
        "description": "Message ID of the last message in the list as a string",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Number of messages to be fetched from the conversation. Default limit is 20",
        "required": false
    },
    "type": {
        "type": "string",
        "description": "Types of message to fetched separated with comma",
        "required": false
    }
}
)
async def get-messages(authorization: str, version: str, conversatio\1_\2: str, las\1_\2_\1d: Optional[str], limit: Optional[float], type: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-messages",
    "path": "/conversations/{conversationId}/messages",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "conversatio\\1_\\2": "__VAR__conversatio\\1_\\2__VAR__",
        "las\\1_\\2_\\1d": "__VAR__las\\1_\\2_\\1d__VAR__",
        "limit": limit,
        "type": type
    }
}


@Tool(
    name="send-a-new-message",
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
async def send-a-new-message(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for send-a-new-message",
    "path": "/conversations/messages",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="add-an-inbound-message",
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
async def add-an-inbound-message(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-an-inbound-message",
    "path": "/conversations/messages/inbound",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="add-an-outbound-message",
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
async def add-an-outbound-message(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for add-an-outbound-message",
    "path": "/conversations/messages/outbound",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="cancel-scheduled-message",
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
    "messag\\1_\\2": {
        "type": "string",
        "description": "Message Id",
        "required": true
    }
}
)
async def cancel-scheduled-message(authorization: str, version: str, messag\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for cancel-scheduled-message",
    "path": "/conversations/messages/{messageId}/schedule",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "messag\\1_\\2": "__VAR__messag\\1_\\2__VAR__"
    }
}


@Tool(
    name="upload-file-attachments",
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
async def upload-file-attachments(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for upload-file-attachments",
    "path": "/conversations/messages/upload",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="update-message-status",
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
    "messag\\1_\\2": {
        "type": "string",
        "description": "Message Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-message-status(authorization: str, version: str, messag\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-message-status",
    "path": "/conversations/messages/{messageId}/status",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "messag\\1_\\2": "__VAR__messag\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-message-recording",
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
        "description": "Location ID as string",
        "required": true
    },
    "messag\\1_\\2": {
        "type": "string",
        "description": "Message ID as string",
        "required": true
    }
}
)
async def get-message-recording(authorization: str, version: str, locatio\1_\2: str, messag\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-message-recording",
    "path": "/conversations/messages/{messageId}/locations/{locationId}/recording",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "messag\\1_\\2": "__VAR__messag\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-message-transcription",
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
        "description": "Location ID as string",
        "required": true
    },
    "messag\\1_\\2": {
        "type": "string",
        "description": "Message ID as string",
        "required": true
    }
}
)
async def get-message-transcription(authorization: str, version: str, locatio\1_\2: str, messag\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-message-transcription",
    "path": "/conversations/locations/{locationId}/messages/{messageId}/transcription",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "messag\\1_\\2": "__VAR__messag\\1_\\2__VAR__"
    }
}


@Tool(
    name="download-message-transcription",
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
        "description": "Location ID as string",
        "required": true
    },
    "messag\\1_\\2": {
        "type": "string",
        "description": "Message ID as string",
        "required": true
    }
}
)
async def download-message-transcription(authorization: str, version: str, locatio\1_\2: str, messag\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for download-message-transcription",
    "path": "/conversations/locations/{locationId}/messages/{messageId}/transcription/download",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "messag\\1_\\2": "__VAR__messag\\1_\\2__VAR__"
    }
}


@Tool(
    name="live-chat-agent-typing",
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
async def live-chat-agent-typing(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for live-chat-agent-typing",
    "path": "/conversations/providers/live-chat/typing",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="create-conversation",
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
async def create-conversation(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-conversation",
    "path": "/conversations/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


