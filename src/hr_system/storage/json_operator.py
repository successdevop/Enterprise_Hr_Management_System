import json
from datetime import datetime


def save_to_jason_database(data, filename):
    with open(filename, mode="w", encoding="utf-8") as file_writer:
        json.dump(data, file_writer, indent=4)


def logger(msg, filename):
    with open(filename, mode="w", encoding="utf-8") as file_writer:
        file_writer.write(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]: {msg}\n")
