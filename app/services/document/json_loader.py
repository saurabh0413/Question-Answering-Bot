import json
from typing import Dict, Any

def load_json(file_content: bytes) -> Any:
    try:
        data = json.loads(file_content.decode('utf-8'))
        return data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")
