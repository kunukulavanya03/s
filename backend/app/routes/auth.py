from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import User
from app.config import settings
from app.utils import get_password_hash, verify_password

router = APIRouter(
    tags=['auth'],
    prefix='/api/auth'
)

@router.post('/register')
def register_user(user: User):
    db = SessionLocal()
    user_exists = db.query(User).filter(User.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail='User already exists')
    user.password = get_password_hash(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'token': 'token_here', 'user_id': user.id}

@router.post('/login')
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail='Invalid username or password')
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid username or password')
    return {'token': 'token_here', 'user_id': user.id}
