from fastapi import APIRouter,Depends,status,requests
from typing import List
from .. import schemas, database, models ,oauth2
from sqlalchemy.orm import Session
from ..repository import blog


from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/')
def all(db: Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):  
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request :schemas.Blog,db: Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.delete('/{id}',status_code=204)
def destroy(id:int, db: Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}' , status_code=202)
def update(id:int,request : schemas.Blog , db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,db,request) 


@router.get('/{id}',status_code=200)
def show(id:int, db: Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.show(id,db)