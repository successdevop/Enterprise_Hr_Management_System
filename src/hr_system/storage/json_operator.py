import json
from datetime import datetime


def save_to_json_database(data, filename):
    try:
        with open(filename, mode="w", encoding="utf-8") as file_writer:
            json.dump(data, file_writer, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")


def logger(msg, filename):
    try:
        with open(filename, mode="a", encoding="utf-8") as file_writer:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_writer.write(f"[{timestamp}]: {msg} \n")
    except Exception as e:
        print(f"ERROR writing to log file {filename}: {e}")
