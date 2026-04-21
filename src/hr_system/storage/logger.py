from datetime import datetime
from src.hr_system.storage.config import ERROR_LOGS


class Logger:
    @staticmethod
    def info(msg, filename):
        try:
            with open(filename, mode="a", encoding="utf-8") as file_writer:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file_writer.write(f"[{timestamp}]: {msg} \n")
        except Exception as e:
            (print(f"ERROR writing to log file {filename}: {e}"))

    @staticmethod
    def error(msg):
        try:
            with open(ERROR_LOGS, mode="a", encoding="utf-8") as file_writer:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file_writer.write(f"[{timestamp}]: {msg} \n")
        except Exception as e:
            print(f"ERROR writing to log file {ERROR_LOGS}: {e}")
