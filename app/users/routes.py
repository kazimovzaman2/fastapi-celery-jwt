from fastapi import APIRouter, HTTPException, Depends
from app.config.security import get_current_user

from app.users.model import User
from app.users.schema import LoginSchema, UserSchema
from app.config.utils import (
    create_access_token,
    create_refresh_token,
    get_hashed_password,
    verify_password,
    verify_refresh_token,
)

router_user = APIRouter(prefix="/api/v1")


@router_user.post("/signup")
async def signup(user_data: UserSchema):
    try:
        if User.select().where(User.email == user_data.email).exists():
            raise HTTPException(status_code=400, detail="User already exists")

        user_data.password = get_hashed_password(user_data.password)

        user = User.create(**user_data.dict())

        access_token = create_access_token(user.email)
        refresh_token = create_refresh_token(user.email)

        return {"access_token": access_token, "refresh_token": refresh_token}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_user.post("/auth")
async def auth(user_data: LoginSchema):
    try:
        user = User.get(User.email == user_data.email)

        if verify_password(get_hashed_password(user_data.password), user.password):
            raise HTTPException(status_code=400, detail="Invalid password")

        access_token = create_access_token(user.email)
        refresh_token = create_refresh_token(user.email)

        return {"access_token": access_token, "refresh_token": refresh_token}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_user.post("/refresh")
async def refresh_tokens(refresh_token: str):
    try:
        email = verify_refresh_token(refresh_token)

        access_token = create_access_token(email)
        new_refresh_token = create_refresh_token(email)

        return {"access_token": access_token, "refresh_token": new_refresh_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_user.get("/user")
async def get_me(user: UserSchema = Depends(get_current_user)):
    return user
