import re


def validate_password(password: str):
    return (
        re.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!#%*?&])([A-Za-z\d$@$!#%*?&]|[^ ]){8,32}$",
            password,
        )
        is not None
    )


def validate_email(email: str):
    return re.match("^\S{1,}@\S{2,}\.\S{2,}$", email,) is not None

