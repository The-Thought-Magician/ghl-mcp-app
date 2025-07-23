import json
import os
from pathlib import Path
import re

# Mapping of OpenAPI types to Python types
TYPE_MAP = {
    "string": "str",
    "number": "float", 
    "integer": "int",
    "boolean": "bool",
    "array": "list",
    "object": "dict",
}

def to_python_type(openapi_type: str, is_required: bool = True) -> str:
    py_type = TYPE_MAP.get(openapi_type, "Any")
    if not is_required:
        py_type = f"Optional[{py_type}]"
    return py_type

def to_snake_case(name: str) -> str:
    # Handle hyphens first
    name = name.replace('-', '_')
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\\1_\\2', name)
    return re.sub('(?<!^)([A-Z])', r'_\\1', s1).lower()

def sanitize_function_name(name: str) -> str:
    """Sanitize function name to be valid Python identifier"""
    name = to_snake_case(name)
    # Remove any non-alphanumeric characters except underscores
    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    # Ensure it doesn't start with a number
    if name[0].isdigit():
        name = f"operation_{name}"
    return name

def generate_tools(docs_path: Path, output_path: Path):
    output_path.mkdir(parents=True, exist_ok=True)

    # List of JSON files to process (excluding toc.json and .github/highlevel-teams.json)
    json_files = [
        f for f in docs_path.glob("**/*.json")
        if f.name not in ["toc.json", "highlevel-teams.json"]
    ]

    for json_file in json_files:
        with open(json_file, 'r') as f:
            spec = json.load(f)

        file_name = to_snake_case(json_file.stem) + ".py"
        output_file_path = output_path / file_name

        with open(output_file_path, 'w') as out_f:
            out_f.write("""from typing import Any, Dict, List, Optional
from fastmcp.tool import Tool

""")

            for path, methods in spec.get("paths", {}).items():
                for method, details in methods.items():
                    operation_id = details.get("operationId")
                    summary = details.get("summary", "")
                    # Escape description for inclusion in a Python string literal
                    description = details.get("description", summary).replace('"', '\\"').replace("\n", "\\n")

                    if not operation_id:
                        print(f"Skipping unnamed operation in {json_file.name} for path {path} method {method}")
                        continue

                    func_name = sanitize_function_name(operation_id)
                    params = []
                    args = []
                    tool_params_dict = {}

                    # Process parameters
                    for param in details.get("parameters", []):
                        param_name_snake = to_snake_case(param["name"])
                        param_type_openapi = param["schema"]["type"] if "schema" in param and "type" in param["schema"] else "string" # Default to string if type is missing
                        param_type_python = to_python_type(param_type_openapi, param.get("required", False))
                        param_description = param.get("description", "").replace('"', '\\"').replace("\n", "\\n")

                        params.append(f"{param_name_snake}: {param_type_python}")
                        args.append(param_name_snake)
                        
                        tool_params_dict[param_name_snake] = {
                            "type": param_type_openapi,
                            "description": param_description,
                            "required": param.get("required", False)
                        }

                    # Process request body
                    request_body = details.get("requestBody")
                    if request_body:
                        content = request_body.get("content", {})
                        app_json = content.get("application/json", {})
                        schema_ref = app_json.get("schema", {}).get("$ref")
                        
                        # For now, just add a generic dict for request body
                        # TODO: Parse schema_ref to generate proper Pydantic models or dict structures
                        params.append("request_body: Dict[str, Any]")
                        args.append("request_body")
                        tool_params_dict["request_body"] = {"type": "object", "description": "The request body for the API call.", "required": True}

                    # Construct the function signature
                    func_signature = f"async def {func_name}({', '.join(params)}) -> Dict[str, Any]:"

                    # Construct the tool definition
                    tool_decorator_params_str = json.dumps(tool_params_dict, indent=4)

                    # Write the tool and function definition to the file
                    out_f.write(f"@Tool(\n")
                    out_f.write(f'    name="{operation_id}",\n')
                    out_f.write(f'    description="{description}",\n')
                    out_f.write(f"    parameters={tool_decorator_params_str}\n")
                    out_f.write(f")\n")
                    out_f.write(f"{func_signature}\n")
                    out_f.write(f'    """Returns: Dict[str, Any]"""\n')
                    out_f.write(f"    # TODO: Implement the actual API call using a client\n")
                    out_f.write(f"    # For now, return a placeholder\n")
                    
                    # Construct the return dictionary string with placeholders for variables
                    return_dict_str_template = json.dumps({
                        "message": f"This is a placeholder for {operation_id}",
                        "path": path,
                        "method": method,
                        "params": {arg: f"__VAR__{arg}__VAR__" for arg in args}
                    }, indent=4)

                    # Replace placeholders with actual variable names
                    for arg in args:
                        return_dict_str_template = return_dict_str_template.replace(f'"__VAR__{arg}__VAR__"', arg)

                    out_f.write(f"    return {return_dict_str_template}\n\n\n")


if __name__ == "__main__":
    project_root = Path(__file__).parents[1]
    docs_path = project_root / "docs"
    output_path = project_root / "src" / "mcp_tools"

    generate_tools(docs_path, output_path)