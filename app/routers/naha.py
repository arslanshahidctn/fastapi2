from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engin
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..import models,schemas,utils,oath2
from fastapi import FastAPI,Depends, status, HTTPException,APIRouter
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..import models,schemas,utils,oath2
from ..schemas import new_posted_2
from ..database import get_db
router=APIRouter(
    tags=['folow']
)

app = FastAPI()





# API Models
class FollowCreate(BaseModel):
    follower_id: str
    following_id: str


# API endpoints
@app.post('/follow', status_code=201)
def follow_user(follow: FollowCreate, db: Session = Depends(get_db)):
    follower = db.query(models.User).filter(models.User.id == follow.follower_id).first()
    following = db.query(models.User).filter(models.User.id == follow.following_id).first()
    
    if not follower or not following:
        raise HTTPException(status_code=404, detail='Invalid follower or following user ID.')
    
    new_follow = models.Follow(follower_id=follow.follower_id, following_id=follow.following_id)
    db.add(new_follow)
    db.commit()
    return {'message': 'User followed successfully.'}


@app.get('/followers/{user_id}', status_code=200)
def get_followers(user_id: str, db: Session = Depends(get_db)):
    followers = db.query(models.Follow).filter(models.Follow.following_id == user_id).all()
    follower_ids = [follower.follower_id for follower in followers]
    return {'followers': follower_ids}


@app.get('/following/{user_id}', status_code=200)
def get_following(user_id: str, db: Session = Depends(get_db)):
    following = db.query(models.Follow).filter(models.Follow.follower_id == user_id).all()
    following_ids = [follow.following_id for follow in following]
    return {'following': following_ids}