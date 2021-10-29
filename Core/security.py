from passlib.context import CryptContext


pwd_contexs = CryptContext(schemes=["bcrypt"])

def verify_password(plain_password: str, hashed_password: str):
    return pwd_contexs.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_contexs.hash(password)