from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Design
from app.config import settings

router = APIRouter(
    tags=['designs'],
    prefix='/api/designs'
)

@router.get('/')
def get_designs():
    db = SessionLocal()
    designs = db.query(Design).all()
    return {'designs': designs}

@router.get('/{design_id}')
def get_design(design_id: int):
    db = SessionLocal()
    design = db.query(Design).filter(Design.id == design_id).first()
    if not design:
        raise HTTPException(status_code=404, detail='Design not found')
    return {'design': design}

@router.post('/')
def create_design(name: str, description: str):
    db = SessionLocal()
    design = Design(name=name, description=description)
    db.add(design)
    db.commit()
    db.refresh(design)
    return {'design_id': design.id}

@router.put('/{design_id}')
def update_design(design_id: int, name: str, description: str):
    db = SessionLocal()
    design = db.query(Design).filter(Design.id == design_id).first()
    if not design:
        raise HTTPException(status_code=404, detail='Design not found')
    design.name = name
    design.description = description
    db.commit()
    db.refresh(design)
    return {'design_id': design.id}

@router.delete('/{design_id}')
def delete_design(design_id: int):
    db = SessionLocal()
    design = db.query(Design).filter(Design.id == design_id).first()
    if not design:
        raise HTTPException(status_code=404, detail='Design not found')
    db.delete(design)
    db.commit()
    return {'message': 'Design deleted successfully'}
