from typing import Union

from pydantic import EmailStr

from .models import User
from .dao import UsersDAO
from .utils import verify_password


async def authenticate_user(email: EmailStr, password: str) -> Union[User, None]:
    user: Union[User, None] = await UsersDAO.find_one_or_none(email=email)
    if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
        return None
    return user