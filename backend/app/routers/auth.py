from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.crud.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)
from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    # Check username
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    # Check email
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return create_user(db, user)


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):

    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        db_user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "user_id": db_user.id
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user