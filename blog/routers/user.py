from fastapi import APIRouter
from .. import database, schemas, models,oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, status, HTTPException

from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
)
get_db = database.get_db


@router.get('/')
def all(db: Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):  
    return user.get_all(db)

@router.post('/')
def create_user(request:schemas.User,db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request,db)


@router.get('/{id}')
def get_user(id: int,db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id,db)

@router.delete('/{id}',status_code=204)
def destroy(id:int, db: Session= Depends(get_db)):
    return user.destroy(id,db)