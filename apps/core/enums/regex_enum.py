from enum import Enum


class RegexEnum(Enum):
    NAME_C_SC = (
        r'^[A-ZА-ЯІЇЄҐ][a-zA-Zа-яіїєґА-ЯІЇЄҐ\s\',-]*$',
        'Only alpha characters, space, apostrophe, comma, hyphen are allowed',
    )

    NAME = (
        r'^[A-Z][a-zA-Z\s\'-]{1,29}$',
        'The name must begin with a capital letter, a space, a hyphen, or an apostrophe'
    )

    PASSWORD = (
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        'At least one lowercase letter, at least one capital letter, at least one digit, at least one special character, minimum 8 characters'
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg