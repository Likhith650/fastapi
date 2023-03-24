from turtle import done
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from .. hashing import Hash


def get_all(db:Session):
    users= db.query(models.User).all()
    return users

def create(request:schemas.User,db:Session):
    new_user =models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))  # type: ignore
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
    
    return user

def destroy(id:int,db:Session):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return done

    