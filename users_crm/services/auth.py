from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from config import settings
from fastapi import HTTPException, status
from schemas.auth import AuthSchema, TokenSchema
from jose import JWTError, jwt

from users_crm.repositories.abstract import AbstractRepository
from users_crm.schemas.types import PyObjectId
from users_crm.schemas.users import UserSchema

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class AuthService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({'exp': expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    async def authenticate_user(self, email: str, password: str):
        user = await self.users_repo.find_one({'email': email})
        if not user or not self.verify_password(password, user['password']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
        return user

    async def login_user(self, auth_data: dict) -> TokenSchema:
        user = await self.authenticate_user(auth_data['email'], auth_data['password'])
        access_token = self.create_access_token(data={'sub': user['email'], 'role': user['role']})
        user['last_login'] = datetime.now(timezone.utc)
        self.users_repo.update_one(id=user['_id'], data=user)
        return TokenSchema(access_token=access_token, token_type='bearer')

    async def register_user(self, user: UserSchema) -> UserSchema:
        existing_user = await self.users_repo.find_by_filters({'email': user.email})
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')

        auth_data = user.model_dump(by_alias=True, exclude=['id'])
        auth_data['password'] = self.hash_password(user.password)

        new_id = await self.users_repo.add_one(auth_data)
        data = await self.users_repo.find_one({'_id': PyObjectId(new_id)})
        if not data:
            raise HTTPException(status_code=404, detail='User not found')
        return UserSchema(**data)

    async def get_user_by_token(self, token: str) -> UserSchema:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            email: str = payload.get('sub')
            if not email:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

            user = await self.users_repo.find_one({'email': email})
            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')

            await self.users_repo.update_one(
                id=user['_id'],
                data={'last_login': datetime.now(timezone.utc)}
            )
            return UserSchema(**user)
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
