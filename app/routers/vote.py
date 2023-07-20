from fastapi import FastAPI,Depends, status, HTTPException,APIRouter
from typing import Optional
from sqlalchemy.orm import Session
from ..import models,schemas,utils,oath2,database
from ..schemas import new_posted_2
from ..database import get_db



router=APIRouter(
    tags=['vots']
)
@router.post("/vots")
def vote(vote:schemas.vots,db: Session = Depends(get_db),current_user:int=Depends(oath2.get_current_user)):
    query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    found=query.first()
    if (vote.dir==1):
        if found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='you already like this post')
        new_vote=models.Vote(user_id=current_user.id,post_id=vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"message":"post liked successfully"}
    else:
        if not found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail='user or post not found')
        query.delete(synchronize_session=False)
        db.commit()
        return{"message":"post successfully unliked"}
        
