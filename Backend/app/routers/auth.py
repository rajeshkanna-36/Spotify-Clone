from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.Model.User import User
from app.Model.schemas import UserCreate, Token
from app.Security.hashing import hash_password, verify_password
from app.Security.jwt import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(User).filter(User.email_id == user.email_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    # Create new user
    new_user = User(
        user_name=user.user_name,
        email_id=user.email_id,
        mobile_number=user.mobile_number,
        date_of_birth=user.date_of_birth,
        password_hash=hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Generate token
    access_token = create_access_token(data={"sub": str(new_user.user_id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Find user by email (OAuth2 uses 'username' field for the identifier)
    user = db.query(User).filter(User.email_id == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Verify password
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Generate token
    access_token = create_access_token(data={"sub": str(user.user_id)})
    return {"access_token": access_token, "token_type": "bearer"}
