class Person:
    def __init__(self, name: str, email: str, age: int, state_of_origin: str):
        self._name = name
        self._email = email
        self._age = age
        self._origin = state_of_origin

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    @property
    def origin(self):
        return self._origin

    def __repr__(self):
        return f"Person(name={self._name} | email={self._email} | age={self._age} | origin={self._origin})"
