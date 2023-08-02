import json

def load_schema_from_file(file_path):
    with open(file_path, 'r') as file:
        schema = json.load(file)
    return schema
