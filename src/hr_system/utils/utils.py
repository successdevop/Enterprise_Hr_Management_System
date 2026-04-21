import re


class Utils:
    """ this class provides the functions/methods that serves as helper function to our application"""

    @staticmethod
    def validate_name(name: str) -> str | None:
        if name and len(name) >= 3:
            return name.strip().title()
        print("Name value cannot be empty and must be at-least 3 characters")
        return None

    @staticmethod
    def validate_email(email: str) -> str | None:
        # Stricter pattern that prevents leading/trailing dots
        pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9]@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Additional check for consecutive dots
        local_part = email.split('@')[0]
        if re.match(pattern, email) and '..' not in local_part:
            return email

        print("Invalid email format. Enter a correct email")
        return None

    @staticmethod
    def validate_age(age: int) -> int | None:
        if isinstance(age, int):
            if age >= 18:
                return age
            else:
                print("You must be at-least 18 years")
                return None
        else:
            print("Invalid age value")
            return None

    @staticmethod
    def validate_amount_input(amount) -> float | None:
        """
        this function takes the user input and checks if it is an actually number
        and that the number is also not negative
        :param amount: user input
        :return: float number
        """
        if float(amount) > 0:
            return float(amount)
        else:
            print(f"Amount cannot be negative and must be greater than 0")
            return None
