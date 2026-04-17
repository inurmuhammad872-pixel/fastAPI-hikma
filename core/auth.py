from jose import jwt
from datetime import datetime, timedelta
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_HOURS


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)