from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Comment
from app.config import settings

router = APIRouter(
    tags=['comments'],
    prefix='/api/comments'
)

@router.get('/')
def get_comments():
    db = SessionLocal()
    comments = db.query(Comment).all()
    return {'comments': comments}

@router.get('/{comment_id}')
def get_comment(comment_id: int):
    db = SessionLocal()
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail='Comment not found')
    return {'comment': comment}

@router.post('/')
def create_comment(content: str, post_id: int):
    db = SessionLocal()
    comment = Comment(content=content, post_id=post_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return {'comment_id': comment.id}

@router.put('/{comment_id}')
def update_comment(comment_id: int, content: str):
    db = SessionLocal()
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail='Comment not found')
    comment.content = content
    db.commit()
    db.refresh(comment)
    return {'comment_id': comment.id}

@router.delete('/{comment_id}')
def delete_comment(comment_id: int):
    db = SessionLocal()
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail='Comment not found')
    db.delete(comment)
    db.commit()
    return {'message': 'Comment deleted successfully'}
