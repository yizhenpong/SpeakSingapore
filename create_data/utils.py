import json

def write_to_json_file(file_path, object, string = False):
    if string:
        object = json.loads(object)
    json_object = json.dumps(object, indent=4)
    with open(file_path, "w") as file:
        file.write(json_object)
    print(f"contents saved to {file_path}")