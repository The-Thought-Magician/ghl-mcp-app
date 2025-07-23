from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

@Tool(
    name="create-invoice-template",
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
async def create-invoice-template(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-invoice-template",
    "path": "/invoices/template",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="list-invoice-templates",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    },
    "status": {
        "type": "string",
        "description": "status to be filtered",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "startAt in YYYY-MM-DD format",
        "required": false
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "endAt in YYYY-MM-DD format",
        "required": false
    },
    "search": {
        "type": "string",
        "description": "To search for an invoice by id / name / email / phoneNo",
        "required": false
    },
    "paymen\\1_\\2": {
        "type": "string",
        "description": "payment mode",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "Limit the number of items to return",
        "required": true
    },
    "offset": {
        "type": "string",
        "description": "Number of items to skip",
        "required": true
    }
}
)
async def list-invoice-templates(authorization: str, version: str, al\1_\2: str, al\1_\2: str, status: Optional[str], star\1_\2: Optional[str], en\1_\2: Optional[str], search: Optional[str], paymen\1_\2: Optional[str], limit: str, offset: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for list-invoice-templates",
    "path": "/invoices/template",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "status": status,
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__",
        "search": search,
        "paymen\\1_\\2": "__VAR__paymen\\1_\\2__VAR__",
        "limit": limit,
        "offset": offset
    }
}


@Tool(
    name="get-invoice-template",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def get-invoice-template(authorization: str, version: str, templat\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-invoice-template",
    "path": "/invoices/template/{templateId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-invoice-template",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice-template(authorization: str, version: str, templat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-template",
    "path": "/invoices/template/{templateId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-invoice-template",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def delete-invoice-template(authorization: str, version: str, templat\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-invoice-template",
    "path": "/invoices/template/{templateId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-invoice-late-fees-configuration",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice-late-fees-configuration(authorization: str, version: str, templat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-late-fees-configuration",
    "path": "/invoices/template/{templateId}/late-fees-configuration",
    "method": "patch",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="update-invoice-late-fees-configuration",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice-late-fees-configuration(authorization: str, version: str, templat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-late-fees-configuration",
    "path": "/invoices/template/{templateId}/payment-methods-configuration",
    "method": "patch",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="create-invoice-schedule",
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
async def create-invoice-schedule(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-invoice-schedule",
    "path": "/invoices/schedule",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="list-invoice-schedules",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    },
    "status": {
        "type": "string",
        "description": "status to be filtered",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "startAt in YYYY-MM-DD format",
        "required": false
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "endAt in YYYY-MM-DD format",
        "required": false
    },
    "search": {
        "type": "string",
        "description": "To search for an invoice by id / name / email / phoneNo",
        "required": false
    },
    "paymen\\1_\\2": {
        "type": "string",
        "description": "payment mode",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "Limit the number of items to return",
        "required": true
    },
    "offset": {
        "type": "string",
        "description": "Number of items to skip",
        "required": true
    }
}
)
async def list-invoice-schedules(authorization: str, version: str, al\1_\2: str, al\1_\2: str, status: Optional[str], star\1_\2: Optional[str], en\1_\2: Optional[str], search: Optional[str], paymen\1_\2: Optional[str], limit: str, offset: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for list-invoice-schedules",
    "path": "/invoices/schedule",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "status": status,
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__",
        "search": search,
        "paymen\\1_\\2": "__VAR__paymen\\1_\\2__VAR__",
        "limit": limit,
        "offset": offset
    }
}


@Tool(
    name="get-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def get-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def delete-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-and-schedule-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    }
}
)
async def update-and-schedule-invoice-schedule(authorization: str, version: str, schedul\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-and-schedule-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}/updateAndSchedule",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__"
    }
}


@Tool(
    name="schedule-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def schedule-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for schedule-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}/schedule",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="auto-payment-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def auto-payment-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for auto-payment-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}/auto-payment",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="cancel-invoice-schedule",
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
    "schedul\\1_\\2": {
        "type": "string",
        "description": "Schedule Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def cancel-invoice-schedule(authorization: str, version: str, schedul\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for cancel-invoice-schedule",
    "path": "/invoices/schedule/{scheduleId}/cancel",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "schedul\\1_\\2": "__VAR__schedul\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="text2pay-invoice",
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
async def text2pay-invoice(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for text2pay-invoice",
    "path": "/invoices/text2pay",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="generate-invoice-number",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    }
}
)
async def generate-invoice-number(authorization: str, version: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for generate-invoice-number",
    "path": "/invoices/generate-invoice-number",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="get-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def get-invoice(authorization: str, version: str, invoic\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for get-invoice",
    "path": "/invoices/{invoiceId}",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice(authorization: str, version: str, invoic\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice",
    "path": "/invoices/{invoiceId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    }
}
)
async def delete-invoice(authorization: str, version: str, invoic\1_\2: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-invoice",
    "path": "/invoices/{invoiceId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="update-invoice-late-fees-configuration",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-invoice-late-fees-configuration(authorization: str, version: str, invoic\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-late-fees-configuration",
    "path": "/invoices/{invoiceId}/late-fees-configuration",
    "method": "patch",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="void-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def void-invoice(authorization: str, version: str, invoic\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for void-invoice",
    "path": "/invoices/{invoiceId}/void",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="send-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def send-invoice(authorization: str, version: str, invoic\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for send-invoice",
    "path": "/invoices/{invoiceId}/send",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="record-invoice",
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
    "invoic\\1_\\2": {
        "type": "string",
        "description": "Invoice Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def record-invoice(authorization: str, version: str, invoic\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for record-invoice",
    "path": "/invoices/{invoiceId}/record-payment",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "invoic\\1_\\2": "__VAR__invoic\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="update-invoice-last-visited-at",
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
async def update-invoice-last-visited-at(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-invoice-last-visited-at",
    "path": "/invoices/stats/last-visited-at",
    "method": "patch",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="create-new-estimate",
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
async def create-new-estimate(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-new-estimate",
    "path": "/invoices/estimate",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="update-estimate",
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
    "estimat\\1_\\2": {
        "type": "string",
        "description": "Estimate Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-estimate(authorization: str, version: str, estimat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-estimate",
    "path": "/invoices/estimate/{estimateId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "estimat\\1_\\2": "__VAR__estimat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-estimate",
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
    "estimat\\1_\\2": {
        "type": "string",
        "description": "Estimate Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def delete-estimate(authorization: str, version: str, estimat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-estimate",
    "path": "/invoices/estimate/{estimateId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "estimat\\1_\\2": "__VAR__estimat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="generate-estimate-number",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    }
}
)
async def generate-estimate-number(authorization: str, version: str, al\1_\2: str, al\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for generate-estimate-number",
    "path": "/invoices/estimate/number/generate",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__"
    }
}


@Tool(
    name="send-estimate",
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
    "estimat\\1_\\2": {
        "type": "string",
        "description": "Estimate Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def send-estimate(authorization: str, version: str, estimat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for send-estimate",
    "path": "/invoices/estimate/{estimateId}/send",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "estimat\\1_\\2": "__VAR__estimat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="create-invoice-from-estimate",
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
    "estimat\\1_\\2": {
        "type": "string",
        "description": "Estimate Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def create-invoice-from-estimate(authorization: str, version: str, estimat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-invoice-from-estimate",
    "path": "/invoices/estimate/{estimateId}/invoice",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "estimat\\1_\\2": "__VAR__estimat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="list-estimates",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "startAt in YYYY-MM-DD format",
        "required": false
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "endAt in YYYY-MM-DD format",
        "required": false
    },
    "search": {
        "type": "string",
        "description": "search text for estimates name",
        "required": false
    },
    "status": {
        "type": "string",
        "description": "estimate status",
        "required": false
    },
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact ID for the estimate",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "Limit the number of items to return",
        "required": true
    },
    "offset": {
        "type": "string",
        "description": "Number of items to skip",
        "required": true
    }
}
)
async def list-estimates(authorization: str, version: str, al\1_\2: str, al\1_\2: str, star\1_\2: Optional[str], en\1_\2: Optional[str], search: Optional[str], status: Optional[str], contac\1_\2: Optional[str], limit: str, offset: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for list-estimates",
    "path": "/invoices/estimate/list",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__",
        "search": search,
        "status": status,
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "limit": limit,
        "offset": offset
    }
}


@Tool(
    name="update-estimate-last-visited-at",
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
async def update-estimate-last-visited-at(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-estimate-last-visited-at",
    "path": "/invoices/estimate/stats/last-visited-at",
    "method": "patch",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="list-estimate-templates",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "search": {
        "type": "string",
        "description": "To search for an estimate template by id / name",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "Limit the number of items to return",
        "required": true
    },
    "offset": {
        "type": "string",
        "description": "Number of items to skip",
        "required": true
    }
}
)
async def list-estimate-templates(authorization: str, version: str, al\1_\2: str, al\1_\2: str, search: Optional[str], limit: str, offset: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for list-estimate-templates",
    "path": "/invoices/estimate/template",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "search": search,
        "limit": limit,
        "offset": offset
    }
}


@Tool(
    name="create-estimate-template",
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
async def create-estimate-template(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-estimate-template",
    "path": "/invoices/estimate/template",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="update-estimate-template",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def update-estimate-template(authorization: str, version: str, templat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for update-estimate-template",
    "path": "/invoices/estimate/template/{templateId}",
    "method": "put",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="delete-estimate-template",
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
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    },
    "request_body": {
        "type": "object",
        "description": "The request body for the API call.",
        "required": true
    }
}
)
async def delete-estimate-template(authorization: str, version: str, templat\1_\2: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for delete-estimate-template",
    "path": "/invoices/estimate/template/{templateId}",
    "method": "delete",
    "params": {
        "authorization": authorization,
        "version": version,
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__",
        "request_body": request_body
    }
}


@Tool(
    name="preview-estimate-template",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "",
        "required": true
    },
    "templat\\1_\\2": {
        "type": "string",
        "description": "Template Id",
        "required": true
    }
}
)
async def preview-estimate-template(authorization: str, version: str, al\1_\2: str, al\1_\2: str, templat\1_\2: str) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for preview-estimate-template",
    "path": "/invoices/estimate/template/preview",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "templat\\1_\\2": "__VAR__templat\\1_\\2__VAR__"
    }
}


@Tool(
    name="create-invoice",
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
async def create-invoice(authorization: str, version: str, request_body: Dict[str, Any]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for create-invoice",
    "path": "/invoices/",
    "method": "post",
    "params": {
        "authorization": authorization,
        "version": version,
        "request_body": request_body
    }
}


@Tool(
    name="list-invoices",
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
    "al\\1_\\2": {
        "type": "string",
        "description": "Alt Type",
        "required": true
    },
    "status": {
        "type": "string",
        "description": "status to be filtered",
        "required": false
    },
    "star\\1_\\2": {
        "type": "string",
        "description": "startAt in YYYY-MM-DD format",
        "required": false
    },
    "en\\1_\\2": {
        "type": "string",
        "description": "endAt in YYYY-MM-DD format",
        "required": false
    },
    "search": {
        "type": "string",
        "description": "To search for an invoice by id / name / email / phoneNo",
        "required": false
    },
    "paymen\\1_\\2": {
        "type": "string",
        "description": "payment mode",
        "required": false
    },
    "contac\\1_\\2": {
        "type": "string",
        "description": "Contact ID for the invoice",
        "required": false
    },
    "limit": {
        "type": "string",
        "description": "Limit the number of items to return",
        "required": true
    },
    "offset": {
        "type": "string",
        "description": "Number of items to skip",
        "required": true
    },
    "sor\\1_\\2": {
        "type": "string",
        "description": "The order of sort which should be applied for the sortField",
        "required": false
    }
}
)
async def list-invoices(authorization: str, version: str, al\1_\2: str, al\1_\2: str, status: Optional[str], star\1_\2: Optional[str], en\1_\2: Optional[str], search: Optional[str], paymen\1_\2: Optional[str], contac\1_\2: Optional[str], limit: str, offset: str, sor\1_\2: Optional[str], sor\1_\2: Optional[str]) -> Dict[str, Any]::
    """Returns: Dict[str, Any]"""
    # TODO: Implement the actual API call using a client
    # For now, return a placeholder
    return {
    "message": "This is a placeholder for list-invoices",
    "path": "/invoices/",
    "method": "get",
    "params": {
        "authorization": authorization,
        "version": version,
        "al\\1_\\2": "__VAR__al\\1_\\2__VAR__",
        "status": status,
        "star\\1_\\2": "__VAR__star\\1_\\2__VAR__",
        "en\\1_\\2": "__VAR__en\\1_\\2__VAR__",
        "search": search,
        "paymen\\1_\\2": "__VAR__paymen\\1_\\2__VAR__",
        "contac\\1_\\2": "__VAR__contac\\1_\\2__VAR__",
        "limit": limit,
        "offset": offset,
        "sor\\1_\\2": "__VAR__sor\\1_\\2__VAR__"
    }
}


