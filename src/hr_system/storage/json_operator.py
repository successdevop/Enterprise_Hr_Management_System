import json


def save_to_jason_database(data, filename):
    with open(filename, mode="w", encoding="utf-8") as file_writer:
        return json.dump(data, file_writer, indent=4)
