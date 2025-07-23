from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="get-groups",
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
async def get-groups(authorization: str, version: str, locatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-groups",
    "path": "/calendars/groups",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-calendar-group",
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
async def create-calendar-group(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-calendar-group",
    "path": "/calendars/groups",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="validate-groups-slug",
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
async def validate-groups-slug(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for validate-groups-slug",
    "path": "/calendars/groups/validate-slug",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="delete-group",
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
    "grou\\1_\\2": {
        "type": "string",
        "description": "Group Id",
        "required": true
    }
}
)
async def delete-group(authorization: str, version: str, grou\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-group",
    "path": "/calendars/groups/{groupId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__"
    }
}


@Tool(
    name="edit-group",
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
    "grou\\1_\\2": {
        "type": "string",
        "description": "Group Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def edit-group(authorization: str, version: str, grou\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for edit-group",
    "path": "/calendars/groups/{groupId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="disable-group",
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
    "grou\\1_\\2": {
        "type": "string",
        "description": "Group Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def disable-group(authorization: str, version: str, grou\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for disable-group",
    "path": "/calendars/groups/{groupId}/status",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-calendar-events",
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
    "use\\1_\\2": {
        "type": "string",
        "description": "User Id - Owner of an appointment. Either of userId, groupId or calendarId is required",
        "required": false
    },
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Either of calendarId, userId or groupId is required",
        "required": false
    },
    "grou\\1_\\2": {
        "type": "string",
        "description": "Either of groupId, calendarId or userId is required",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "Start Time (in millis)",
        "required": true
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "End Time (in millis)",
        "required": true
    }
}
)
async def get-calendar-events(authorization: str, version: str, locatio\1_\2: str, use\1_\2: Optional[str], calenda\1_\2: Optional[str], grou\1_\2: Optional[str], star\1_\2: str, en\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-calendar-events",
    "path": "/calendars/events",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "use\\1_\\2": "__VAR__use\\1_\\2__VAR__",
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__",
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-blocked-slots",
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
    "use\\1_\\2": {
        "type": "string",
        "description": "User Id - Owner of an appointment. Either of userId, groupId or calendarId is required",
        "required": false
    },
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Either of calendarId, userId or groupId is required",
        "required": false
    },
    "grou\\1_\\2": {
        "type": "string",
        "description": "Either of groupId, calendarId or userId is required",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "Start Time (in millis)",
        "required": true
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "End Time (in millis)",
        "required": true
    }
}
)
async def get-blocked-slots(authorization: str, version: str, locatio\1_\2: str, use\1_\2: Optional[str], calenda\1_\2: Optional[str], grou\1_\2: Optional[str], star\1_\2: str, en\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-blocked-slots",
    "path": "/calendars/blocked-slots",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "use\\1_\\2": "__VAR__use\\1_\\2__VAR__",
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__",
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-slots",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Calendar Id",
        "required": true
    },
    "star\\1_\\2": {
        "type": "number",
        "description": "Start Date",
        "required": true
    },
    "en\\1_\\2": {
        "type": "number",
        "description": "End Date",
        "required": true
    },
    "timezone": {
        "type": "string",
        "description": "The timezone in which the free slots are returned",
        "required": false
    },
    "use\\1_\\2": {
        "type": "array",
        "description": "The users for whom the free slots are returned",
        "required": false
    },
    "enabl\\1_\\2_\\1usy": {
        "type": "boolean",
        "description": "Apply Look Busy",
        "required": false
    }
}
)
async def get-slots(authorization: str, version: str, calenda\1_\2: str, star\1_\2: float, en\1_\2: float, timezone: Optional[str], use\1_\2: Optional[str], use\1_\2: Optional[list], enabl\1_\2_\1usy: Optional[bool]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-slots",
    "path": "/calendars/{calendarId}/free-slots",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__",
        "timezone": timezone,
        "use\\1_\\2": "__VAR__use\\1_\\2__VAR__",
        "enabl\\1_\\2_\\1usy": "__VAR__enabl\\1_\\2_\\1usy__VAR__"
    }
}


@Tool(
    name="update-calendar",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Calendar Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-calendar(authorization: str, version: str, calenda\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-calendar",
    "path": "/calendars/{calendarId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-calendar",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Calendar Id",
        "required": true
    }
}
)
async def get-calendar(authorization: str, version: str, calenda\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-calendar",
    "path": "/calendars/{calendarId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__"
    }
}


@Tool(
    name="delete-calendar",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "Calendar Id",
        "required": true
    }
}
)
async def delete-calendar(authorization: str, version: str, calenda\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-calendar",
    "path": "/calendars/{calendarId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-appointment",
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
    "even\\1_\\2": {
        "type": "string",
        "description": "Event Id or Instance id. For recurring appointments send masterEventId to modify original series.",
        "required": true
    }
}
)
async def get-appointment(authorization: str, version: str, even\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-appointment",
    "path": "/calendars/events/appointments/{eventId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "even\\1_\\2": "__VAR__even\\1_\\2__VAR__"
    }
}


@Tool(
    name="edit-appointment",
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
    "even\\1_\\2": {
        "type": "string",
        "description": "Event Id or Instance id. For recurring appointments send masterEventId to modify original series.",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def edit-appointment(authorization: str, version: str, even\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for edit-appointment",
    "path": "/calendars/events/appointments/{eventId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "even\\1_\\2": "__VAR__even\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="create-appointment",
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
async def create-appointment(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-appointment",
    "path": "/calendars/events/appointments",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="create-block-slot",
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
async def create-block-slot(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-block-slot",
    "path": "/calendars/events/block-slots",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="edit-block-slot",
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
    "even\\1_\\2": {
        "type": "string",
        "description": "Event Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def edit-block-slot(authorization: str, version: str, even\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for edit-block-slot",
    "path": "/calendars/events/block-slots/{eventId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "even\\1_\\2": "__VAR__even\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-event",
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
    "even\\1_\\2": {
        "type": "string",
        "description": "Event Id or Instance id. For recurring appointments send masterEventId to modify original series.",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def delete-event(authorization: str, version: str, even\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-event",
    "path": "/calendars/events/{eventId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "even\\1_\\2": "__VAR__even\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-appointment-notes",
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
    "limit": {
        "type": "number",
        "description": "Limit of notes to fetch",
        "required": true
    },
    "offset": {
        "type": "number",
        "description": "Offset of notes to fetch",
        "required": true
    },
    "appointmen\\1_\\2": {
        "type": "string",
        "description": "Appointment ID",
        "required": true
    }
}
)
async def get-appointment-notes(authorization: str, version: str, limit: float, offset: float, appointmen\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-appointment-notes",
    "path": "/calendars/appointments/{appointmentId}/notes",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "limit": limit,
        "offset": offset,
        "appointmen\\1_\\2": "__VAR__appointmen\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-appointment-note",
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
    "appointmen\\1_\\2": {
        "type": "string",
        "description": "Appointment ID",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-appointment-note(authorization: str, version: str, appointmen\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-appointment-note",
    "path": "/calendars/appointments/{appointmentId}/notes",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "appointmen\\1_\\2": "__VAR__appointmen\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="update-appointment-note",
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
    "appointmen\\1_\\2": {
        "type": "string",
        "description": "Appointment ID",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-appointment-note(authorization: str, version: str, appointmen\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-appointment-note",
    "path": "/calendars/appointments/{appointmentId}/notes/{noteId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "appointmen\\1_\\2": "__VAR__appointmen\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-appointment-note",
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
    "appointmen\\1_\\2": {
        "type": "string",
        "description": "Appointment ID",
        "required": true
    }
}
)
async def delete-appointment-note(authorization: str, version: str, appointmen\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-appointment-note",
    "path": "/calendars/appointments/{appointmentId}/notes/{noteId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "appointmen\\1_\\2": "__VAR__appointmen\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-calendar-resource",
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
    "resourc\\1_\\2": {
        "type": "string",
        "description": "Calendar Resource Type",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Calendar Resource ID",
        "required": true
    }
}
)
async def get-calendar-resource(authorization: str, version: str, resourc\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-calendar-resource",
    "path": "/calendars/resources/{resourceType}/{id}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "resourc\\1_\\2": "__VAR__resourc\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="update-calendar-resource",
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
    "resourc\\1_\\2": {
        "type": "string",
        "description": "Calendar Resource Type",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Calendar Resource ID",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-calendar-resource(authorization: str, version: str, resourc\1_\2: str, id: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-calendar-resource",
    "path": "/calendars/resources/{resourceType}/{id}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "resourc\\1_\\2": "__VAR__resourc\\1_\\2__VAR__",
        "id": id,
        "request_body": request_body
    }
}


@Tool(
    name="delete-calendar-resource",
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
    "resourc\\1_\\2": {
        "type": "string",
        "description": "Calendar Resource Type",
        "required": true
    },
    "id": {
        "type": "string",
        "description": "Calendar Resource ID",
        "required": true
    }
}
)
async def delete-calendar-resource(authorization: str, version: str, resourc\1_\2: str, id: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-calendar-resource",
    "path": "/calendars/resources/{resourceType}/{id}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "resourc\\1_\\2": "__VAR__resourc\\1_\\2__VAR__",
        "id": id
    }
}


@Tool(
    name="fetch-calendar-resources",
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
    "resourc\\1_\\2": {
        "type": "string",
        "description": "Calendar Resource Type",
        "required": true
    },
    "locatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "limit": {
        "type": "number",
        "description": "",
        "required": true
    },
    "skip": {
        "type": "number",
        "description": "",
        "required": true
    }
}
)
async def fetch-calendar-resources(authorization: str, version: str, resourc\1_\2: str, locatio\1_\2: str, limit: float, skip: float) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for fetch-calendar-resources",
    "path": "/calendars/resources/{resourceType}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "resourc\\1_\\2": "__VAR__resourc\\1_\\2__VAR__",
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "limit": limit,
        "skip": skip
    }
}


@Tool(
    name="create-calendar-resource",
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
    "resourc\\1_\\2": {
        "type": "string",
        "description": "Calendar Resource Type",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-calendar-resource(authorization: str, version: str, resourc\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-calendar-resource",
    "path": "/calendars/resources/{resourceType}",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "resourc\\1_\\2": "__VAR__resourc\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="get-event-notification",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Specifies the ID of the model associated with the notification. This can be extended to support additional models in the future.",
        "required": false
    },
    "i\\1_\\2": {
        "type": "boolean",
        "description": "",
        "required": false
    },
    "deleted": {
        "type": "boolean",
        "description": "",
        "required": false
    },
    "limit": {
        "type": "number",
        "description": "Number of records to return",
        "required": false
    },
    "skip": {
        "type": "number",
        "description": "Number of records to skip",
        "required": false
    }
}
)
async def get-event-notification(authorization: str, version: str, calenda\1_\2: str, al\1_\2: Optional[str], al\1_\2: Optional[str], i\1_\2: Optional[bool], deleted: Optional[bool], limit: Optional[float], skip: Optional[float]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-event-notification",
    "path": "/calendars/{calendarId}/notifications",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "i\\1_\\2": "__VAR__i\\1_\\2__VAR__",
        "deleted": deleted,
        "limit": limit,
        "skip": skip
    }
}


@Tool(
    name="create-event-notification",
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
    "calenda\\1_\\2": {
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
async def create-event-notification(authorization: str, version: str, calenda\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-event-notification",
    "path": "/calendars/{calendarId}/notifications",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="find-event-notification",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "notificatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    }
}
)
async def find-event-notification(authorization: str, version: str, calenda\1_\2: str, notificatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for find-event-notification",
    "path": "/calendars/{calendarId}/notifications/{notificationId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "notificatio\\1_\\2": "__VAR__notificatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-event-notification",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "notificatio\\1_\\2": {
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
async def update-event-notification(authorization: str, version: str, calenda\1_\2: str, notificatio\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-event-notification",
    "path": "/calendars/{calendarId}/notifications/{notificationId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "notificatio\\1_\\2": "__VAR__notificatio\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-event-notification",
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
    "calenda\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "notificatio\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    }
}
)
async def delete-event-notification(authorization: str, version: str, calenda\1_\2: str, notificatio\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-event-notification",
    "path": "/calendars/{calendarId}/notifications/{notificationId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "calenda\\1_\\2": "__VAR__calenda\\1_\\2__VAR__",
        "notificatio\\1_\\2": "__VAR__notificatio\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-calendars",
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
    "grou\\1_\\2": {
        "type": "string",
        "description": "Group Id",
        "required": false
    },
    "sho\\1_\\2": {
        "type": "boolean",
        "description": "Show drafted",
        "required": false
    }
}
)
async def get-calendars(authorization: str, version: str, locatio\1_\2: str, grou\1_\2: Optional[str], sho\1_\2: Optional[bool]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-calendars",
    "path": "/calendars/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "locatio\\1_\\2": "__VAR__locatio\\1_\\2__VAR__",
        "grou\\1_\\2": "__VAR__grou\\1_\\2__VAR__",
        "sho\\1_\\2": "__VAR__sho\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-calendar",
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
async def create-calendar(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-calendar",
    "path": "/calendars/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


