from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
import logging

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend_Api_For_S API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running", "endpoints": 1}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.put("/output")
def output(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
