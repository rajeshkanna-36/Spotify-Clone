from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.Model.User import User
from app.Model.schemas import RefreshTokenRequest, Token, UserCreate
from app.Security.hashing import hash_password, verify_password
from app.Security.jwt import create_access_token, create_refresh_token, verify_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _tokens_for_user(user_id: int) -> dict:
    data = {"sub": str(user_id)}
    return {
        "access_token": create_access_token(data),
        "refresh_token": create_refresh_token(data),
        "token_type": "bearer",
    }


@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email_id == user.email_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    max_user_id = db.query(User.user_id).order_by(User.user_id.desc()).first()
    next_user_id = (max_user_id[0] if max_user_id else 0) + 1

    new_user = User(
        user_id=next_user_id,
        user_name=user.user_name,
        email_id=user.email_id,
        mobile_number=user.mobile_number,
        date_of_birth=user.date_of_birth,
        password_hash=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return _tokens_for_user(new_user.user_id)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email_id == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return _tokens_for_user(user.user_id)


@router.post("/refresh", response_model=Token)
def refresh_token(request: RefreshTokenRequest, db: Session = Depends(get_db)):
    payload = verify_token(request.refresh_token, expected_type="refresh")
    if not payload or payload.get("sub") is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        user_id = int(payload["sub"])
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Issue a new access token and rotate the refresh token.
    return _tokens_for_user(user.user_id)
