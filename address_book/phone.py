from field import Field

class Phone(Field):
    def __init__(self, value):
        # має бути 10 цифр
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)