from fastapi import FastAPI,Depends, status, HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..import models,schemas,utils,oath2
from ..schemas import new_posted,Post, Test
from ..database import get_db
from typing import List
router=APIRouter(tags=['users'])

# ===========================GET ALL POST======================================
@router.get("/users",response_model=List[schemas.Post])
def file(data: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    get_posts=data.query(models.User).all()
    return get_posts
# ===========================NEW POST==========================================
@router.post("/users",response_model=schemas.Post)
def file(post:new_posted,data: Session = Depends(get_db)):
    # print(current_user.email)
    pps=utils.hash(post.hashed_password)
    post.hashed_password=pps    
    create_posts=models.User(**post.dict())
    data.add(create_posts)
    data.commit()
    data.refresh(create_posts)
    return create_posts 
# =====================GET SPECIFIC POST=======================================
@router.get("/users/{id}",response_model=schemas.Post)
def file(id:int,data: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    print(current_user.email)
    get_posts_id=data.query(models.User).filter(models.User.id==id).first()
    if get_posts_id==None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="ok")
    return get_posts_id
# ==========================Delete POST========================================
@router.delete("/users/{id}")
def files(id:int, db: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    del_posts=db.query(models.User).filter(models.User.id==id)
    if del_posts.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="lol")
    del_posts.delete(synchronize_session=False)
    db.commit()
    return("your post deleted successfully")
# ==========================update POST========================================
@router.put("/users/{id}",response_model=schemas.Post)
def read_users( post:new_posted,id:int,lol: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    print(current_user.email)
    pps=utils.hash(post.hashed_password)
    post.hashed_password=pps
    a=lol.query(models.User).filter(models.User.id==id)
    b=a.first()
    if b==None:
        raise HTTPException(status_code=status.HTTP_200_OK,detail="oka")
    a.update(post.dict(),synchronize_session=False)
    lol.commit()
    return a.first()