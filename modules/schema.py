import json
import os
import logging

def load_schema(schema_file='schema.json'):
    # schema_path = os.path.join(os.path.dirname(__file__), schema_file)
    if not os.path.exists(schema_path):
        logging.warning(f"Schema file {schema_file} does not exist.")
        return None

    try:
        with open(schema_path, 'r') as file:
            schema = json.load(file)
            print(f'Schema loaded: {json.dumps(schema, indent=4)}')
            return schema
    except json.JSONDecodeError:
        logging.warning(f"Schema file {schema_file} is not a valid JSON file.")
        return None
def validate_data(data, schema):
    # This is placeholder for data validation logic.
    # Accessing data and schema to remove the warning
    print(data, schema)
    return True

schema = load_schema('schema.json')
