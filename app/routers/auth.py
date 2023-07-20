from fastapi import APIRouter,Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import user_login
from ..import models,utils,oath2


router=APIRouter(tags=["authentication"])
@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_100_CONTINUE,detail=f'Invalid credentials')
    if not utils.verify(user_credentials.password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    access_token=oath2.create_access_token(data={'user_id':user.id})
    return {"access_token":access_token}