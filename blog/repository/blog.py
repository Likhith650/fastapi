from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status,requests

from ..routers import blog


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog =models.Blog(title =request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int,db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,db:Session,request:schemas.Blog):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'


def show(id:int,db:Session):
    blog= db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    
    return blog
