from db.milvus_loader import connect_to_milvus, create_collection
from db.postgres import init_db, get_connection, get_session_local
from sqlalchemy.orm import Session

from app.models.auth.user import User, UserCreate

def get_users():
    session = get_session_local()
    users = session.query(User).all()
    return users

def create_user(user_create: UserCreate, db: Session) -> User:
    db_user = User(name=user_create.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user