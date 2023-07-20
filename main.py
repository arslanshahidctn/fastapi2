from fastapi import FastAPI, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app= FastAPI()
class new_post(BaseModel):
    tittle:str
    content:str
    published:bool=True

g=[{'tittle':"tittle of post 1","content":"content of post 1","id":1},{"tittle":'how are you?',"content":"where you live","id":2}]
def find_post(id):
    for p in g:
        if p["id"]==id:
            return p

@app.get("/posts")
def read_root():
    return (g)


@app.post("/posts")
def ll_root(name:new_post):
    new_name=name.dict()
    new_name['id']=randrange(0,100000)
    g.append(new_name)
    return (new_name)
@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    post=find_post(id)
    if not post:
        response.check_status= 404
    return {"post details":post}