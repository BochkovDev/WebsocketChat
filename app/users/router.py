from fastapi import APIRouter, status, Response

from .auth import authenticate_user
from .utils import get_password_hash, create_access_token
from .dao import UsersDAO
from .schemas import UserRegister as SUserRegister
from .schemas import UserAuth as SUserAuth
from .exceptions import (
    UserAlreadyExistsException, 
    InvalidCredentialsException,
    PasswordMismatchException,
)


router = APIRouter(prefix='/auth', tags=['Auth'])

ACCESS_TOKEN_COOKIE = 'Access_Token'

@router.post('/register/')
async def register(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExistsException()
    
    if user_data.password != user_data.password_check:
        raise PasswordMismatchException()
    
    user_data.password = get_password_hash(user_data.password)
    await UsersDAO.add(**user_data.model_dump())
    return {'message': 'User successfully registered'}

@router.post('/login/')
async def login(response: Response, user_data: SUserAuth) -> dict:
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if user is None:
        raise InvalidCredentialsException()
    access_token = create_access_token({'sub': user.id})
    response.set_cookie(ACCESS_TOKEN_COOKIE, access_token, httponly=True)
    return {ACCESS_TOKEN_COOKIE: access_token, 'Refresh_Token': None, 'Token_Type': 'Bearer'}

@router.post('/logout/')
async def logout(response: Response):
    response.delete_cookie(ACCESS_TOKEN_COOKIE)
    return {'message': 'User successfully logout'}
