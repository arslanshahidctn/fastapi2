from fastapi import FastAPI,Depends, status, HTTPException,APIRouter
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..import models,schemas,utils,oath2
from ..schemas import new_posted_2
from ..database import get_db
router=APIRouter(
    tags=['followers']
)

@router.post("/followers")
def followers(vote:schemas.vots,db: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    user=db.query(models.User).filter(models.User.id==vote.post_id)
    exist=user.first()
    user_exist=db.query(models.Follower).filter(models.Follower.follower_id==current_user.id,models.Following.following_user==vote.post_id)
    found=user_exist.first()
    del_posts=db.query(models.Following).filter(models.Following.following_user==vote.post_id)
    if not exist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not exists")
    if found:
        # user_exist.delete(synchronize_session=False)
        # db.commit()
        del_posts.delete(synchronize_session=False)
        db.commit()
        return {"message":"you unfollow the user"}
    else:
        new_following=models.Following(following_user=vote.post_id)
        db.add(new_following)
        db.commit()
        new_follower=models.Follower(follower_id=current_user.id,following_id=new_following.following_user)
        db.add(new_follower)
        db.commit()
        return {"message":"ok"}   
@router.delete("/followers/{id}")
def followers(id:int,db: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    user=db.query(models.User).filter(current_user.id==id)
    del_us=user.first()
    del_posts=db.query(models.User).filter(models.User.id==id)
    found=del_posts.first()
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not exists")
    if del_us:
        del_posts.delete(synchronize_session=False)
        db.commit()
        return("your user deleted successfully")
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='to mery lan wasty dosry user nu delete kr riya?')
resp=[]
@router.get("/followers")
def get_all_followers(db: Session = Depends(get_db)):
     get_posts=db.query(models.Follower).all()
     resp.append(get_posts)
     return resp
