from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,status,HTTPException
import jwt_token
oauth_scheme=OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(data:str=Depends(oauth_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail={"Could not validate credentials"})
    return jwt_token.verify_token(data,credentials_exception)

