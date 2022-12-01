import json


def load_json_file(file_path: str) -> dict:
    """Loads a json file and returns its content"""
    with open(file_path) as json_file:
        json_content = json_file.read()

    return json.loads(json_content)