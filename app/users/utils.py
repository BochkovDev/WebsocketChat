from datetime import datetime, timedelta, timezone
from typing import Union

from passlib.context import CryptContext
from jose import jwt, JWTError

from core.exceptions import CredentialsException
from core.settings import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.AUTH.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.AUTH.ACCESS_TOKEN_EXPIRE_MINUTES

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise CredentialsException()
        return username
    except JWTError:
        raise CredentialsException()