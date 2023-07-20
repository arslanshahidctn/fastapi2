from fastapi import FastAPI,Depends, status, HTTPException,APIRouter
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..import models,schemas,utils,oath2
from ..schemas import new_posted_2
from ..database import get_db
router=APIRouter(
    tags=['posts']
)

@router.post("/posts",response_model=schemas.return_post)
def new_file(post:new_posted_2,data: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    # pps=pwd_context.hash(post.hashed_password)
    pps=utils.hash(post.hashed_password)
    post.hashed_password=pps
    print(current_user.id)
    new_create_posts=models.Posts(user_id=current_user.id,**post.dict())
    data.add(new_create_posts)
    data.commit()
    data.refresh(new_create_posts)
    return new_create_posts
@router.get("/posts")
def new_files(data: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user),skip:int=0,search:Optional[str]=''):
    # get_new_posts=data.query(models.Posts).filter(models.Posts.user_id==current_user.id).all()
    get_new_posts=data.query(models.Posts).filter(models.Posts.content.contains(search)).offset(skip).all()
    result=data.query(models.Posts,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Posts.id,isouter=True).group_by(models.Posts.id).all
    return result

@router.get("/posts/{id}",response_model=schemas.return_post)
def new_files(id:int,data: Session = Depends(get_db),get_current_user:int=Depends(oath2.get_current_user)):
    get_new_posts=data.query(models.Posts).filter(models.Posts.id==id).first()
    # posts=get_new_posts.first()
    # if posts.user_id != get_current_user.id:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="dafa ho")
    return get_new_posts




@router.delete("/posts/{id}")
def files(id:int, db: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    del_posts=db.query(models.Posts).filter(models.Posts.id==id)
    posts=del_posts.first()
    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="lol")
    
    if posts.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="dafa ho")
    
    del_posts.delete(synchronize_session=False)
    db.commit()
    return("your post deleted successfully")

@router.put("/posts/{id}")
def read_users( post:new_posted_2,id:int,lol: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    pps=utils.hash(post.hashed_password)
    post.hashed_password=pps
    a=lol.query(models.Posts).filter(models.Posts.id==id)
    b=a.first()
    if b==None:
        raise HTTPException(status_code=status.HTTP_200_OK,detail="oka")
    if b.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="dafa ho")
    a.update(post.dict(),synchronize_session=False)
    lol.commit()
    return a.first()

