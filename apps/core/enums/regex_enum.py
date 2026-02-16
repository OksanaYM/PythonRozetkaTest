from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-ZА-ЯІЇЄҐ][a-zA-Zа-яіїєґА-ЯІЇЄҐ\s\',-]*$',
        'Only alpha characters, space, apostrophe, comma, hyphen are allowed',
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg