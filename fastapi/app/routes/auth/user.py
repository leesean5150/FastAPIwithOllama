from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.services.user_service import get_users, create_user
from app.models.auth.user import UserResponse, UserBase
from db.postgres import get_session_local

user_router = APIRouter()

@user_router.get("/users")
def get_all_users():
    user = get_users()
    if user is None:
        raise HTTPException(status_code=404, detail="No users found")
    return user

@user_router.post("/user", response_model=UserResponse)
def create_a_user(user_create: UserBase, db: Session = Depends(get_session_local)):
    user = create_user(user_create, db)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")
    return user