import random
import re
from datetime import datetime


class Utils:
    """ this class provides the functions/methods that serves as helper function to our application"""
    @staticmethod
    def generate_nin(employee_database: list) -> str:
        while True:
            nin = "".join(str(random.randint(1, 9)) for _ in range(10))
            if not any(person.nin == nin for person in employee_database):
                return nin

    @staticmethod
    def validate_name(name: str) -> str | None:
        name = name.strip().title()
        if name and len(name) >= 3:
            return name
        print("Name value cannot be empty and must be at-least 3 characters")
        return

    @staticmethod
    def validate_email(email: str) -> str | None:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        print("Invalid email")
        return

    @staticmethod
    def validate_age(age: int) -> int | None:
        if isinstance(age, int):
            if age >= 18:
                return age
            else:
                print("You must be at-least 18 years")
                return
        else:
            print("Invalid age value")
            return

    @staticmethod
    def validate_amount_input(amount) -> float:
        """
        this function takes the user input and checks if it is an actually number
        and that the number is also not negative
        :param amount: user input
        :return: float number
        """
        try:
            if float(amount) > 0:
                return float(amount)
        except Exception as e:
            print(f"{e} | Amount cannot be negative and must be greater than 0")

    @staticmethod
    def logger(message: str):
        print(f"[{datetime.now()}]: {message}")
