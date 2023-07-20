from fastapi import FastAPI,Depends, status, HTTPException, Form
from sqlalchemy.orm import Session
from .import models,utils
from .import schemas
from .schemas import new_posted,Post, Test
from .database import engine,get_db
from typing import List
from .routers import users,new_users,auth,vote,follower
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(new_users.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(follower.router)

@app.get("/")
def get():
    return {"message":"hello world"}
