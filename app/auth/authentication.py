from datetime import datetime
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from app.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRES
from app.auth.models import TokenData
from app.auth.orm_models import get_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if user is None:
        return False
    if not user.verify_password(password) or not user.is_admin:
        return False
    return user


def create_access_token(*, data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRES
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
