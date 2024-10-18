from typing import Any, Dict
from fastapi import HTTPException, status


class CredentialsException(HTTPException):
    ''' Raises when can't validate user's credentials '''
    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        status_code = status.HTTP_401_UNAUTHORIZED
        detail = 'Could not validate credentials'
        headers = {'WWW-Authenticate': 'Bearer'}
        super().__init__(status_code, detail, headers)