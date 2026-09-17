from fastapi import APIRouter, Depends

from app.Model.User import User
from app.Model.schemas import UserProfile
from app.Security.dependencies import get_current_user

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/me", response_model=UserProfile)
def read_current_user_profile(current_user: User = Depends(get_current_user)):
    """Return the authenticated user profile from the access token."""
    return {
        "user_id": current_user.user_id,
        "user_name": current_user.user_name,
        "email_id": current_user.email_id,
        "mobile_number": current_user.mobile_number,
        "date_of_birth": current_user.date_of_birth,
    }
