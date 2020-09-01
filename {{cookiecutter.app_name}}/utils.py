import re


def contains_upper_case(value: str) -> bool:
    return value != value.lower()


def contains_digit(value: str) -> bool:
    return bool(re.match(r".*\d*", value))


def contains_special_char(value: str) -> bool:
    return bool(re.match(r".*[~!@#$%^&*()_\-]*", value))
