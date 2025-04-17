from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta


# Datos simulados (en un caso real se usaria una base de datos)
fake_users_db = {
    "admin":{
        "username":"admin",
        "password":"admin123" # en un caso real, no se almacena en texto plano y se hashea
    }
}

# configuracion del token
SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # el token se obtiene desde en endpoint /login

def authenticate_user(username:str, password:str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta=None): 
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub") # el usuario se logeo correctamente
        if username is None: 
            raise credentials_exception
        return {"username": username}
    except JWTError:
        raise credentials_exception
        