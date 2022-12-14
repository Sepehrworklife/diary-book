from hashlib import pbkdf2_hmac


salt = b"My!LittleS0ecr2etS#al%t"


def encrtypt_password(password: str) -> str:
    return pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000).hex()


def verify_password(password: str, encrypted_password: str) -> bool:
    password = encrtypt_password(password)
    if password == encrypted_password:
        return True
    return False
