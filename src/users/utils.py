from hashlib import pbkdf2_hmac
from django.shortcuts import redirect
from functools import wraps


salt = b"My!LittleS0ecr2etS#al%t"


def encrtypt_password(password: str) -> str:
    return pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000).hex()


def verify_password(password: str, encrypted_password: str) -> bool:
    password = encrtypt_password(password)
    if password == encrypted_password:
        return True
    return False


def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwrags):
        if request.session.get("user"):
            return func(request, *args, **kwrags)
        return redirect("login")
    return wrapper