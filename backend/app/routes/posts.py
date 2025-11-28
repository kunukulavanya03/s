from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Post
from app.config import settings

router = APIRouter(
    tags=['posts'],
    prefix='/api/posts'
)

@router.get('/')
def get_posts():
    db = SessionLocal()
    posts = db.query(Post).all()
    return {'posts': posts}

@router.get('/{post_id}')
def get_post(post_id: int):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    return {'post': post}

@router.post('/')
def create_post(title: str, content: str):
    db = SessionLocal()
    post = Post(title=title, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {'post_id': post.id}

@router.put('/{post_id}')
def update_post(post_id: int, title: str, content: str):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    post.title = title
    post.content = content
    db.commit()
    db.refresh(post)
    return {'post_id': post.id}

@router.delete('/{post_id}')
def delete_post(post_id: int):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    db.delete(post)
    db.commit()
    return {'message': 'Post deleted successfully'}
