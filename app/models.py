from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
# from fastapi import uuid
# from uuid import UUID

from .database import Base




class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True,index=True)
    hashed_password = Column(String)
    content=Column(String)
    time=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner= relationship ("User")
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    email = Column(String,index=True,unique=True)
    hashed_password = Column(String)
    time=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class Vote(Base):
    __tablename__ = "vots"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    phone_number=Column(String)






class Following(Base):
    __tablename__ = "following"
    following_follower_id=Column(Integer,ForeignKey("follower.id",ondelete="CASCADE"))
    following_user=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    following_id=Column(Integer,ForeignKey("following.following_user",ondelete="CASCADE"))
    follower_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))