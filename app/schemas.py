from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class new_posted(BaseModel):
    email:str
    hashed_password:str
class new_posted_2(BaseModel):
    hashed_password:str
    content:str
    user_id=int

class Post(BaseModel):
    email:EmailStr
    id:int
    time:datetime
    class Config:
        orm_mode=True

class Test(BaseModel):
    id: int
    email:EmailStr
    class Config:
        orm_mode=True

class return_post(BaseModel):
    id:int
    time:datetime
    user_id:int
    content:str
    owner:Test
    class Config:
        orm_mode=True



class user_login(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None

class vots(BaseModel):
    post_id:int
    # dir: conint(le=1)