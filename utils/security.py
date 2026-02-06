import re


def valid_password(password: str, minimum=8) -> bool:
    p_length = len(password)
    has_upper = r"[A-Z]"
    has_lower_at_least_5 = r"[a-z]"
    has_special = r"[!@#$%^&*()\-_=+{}\[\]|\"';:\.,<>\?\/]"
    has_number = r"\d+"

    patterns = [
        has_upper,
        has_lower_at_least_5,
        has_special,
        has_number
    ]

    for p in patterns:
        match = re.search(p, password)
        if match is None:
            return False

    return p_length >= minimum
