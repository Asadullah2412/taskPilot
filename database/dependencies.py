from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
import model
from database_setup import SessionLocal, engine, Base

model.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]