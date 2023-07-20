# host = "localhost"
# dbname = 'fast api'
# user = 'postgres'
# password = 'arslan12'
# conn_string = f"host='{host}' dbname='{dbname}' user='{user}' password='{password}'"
# try:
#     conn = psycopg2.connect(conn_string)
#     arslan=conn.cursor()
#     print("ok")
# except Exception as error:
#     print("connection fail")
#     print("error",error)
# g=[
#     {"tittle":"city name","content":"city of pakistan","id":1},
#     {"tittle":"food","content":"fast foood","id":2}
# ]
# @app.get("/")
# def new_post():
#     arslan.execute("""SELECT * FROM data""")
#     pos=arslan.fetchall()
#     return(pos)
# @app.get("/{id}")
# def new_post(id:int):
#     arslan.execute("""select * from data where id=%s """,
#                    (str(id)))
#     new_pos=arslan.fetchone()
#     print(new_pos)
#     return(new_pos)
# # def new_index_posts(id):
#     for i, p in enumerate(g):
#         if p["key"]==id:    
#             return i
# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_posts(post: new_posted):
#     arslan.execute("""insert into users (email,hashed_password) values(%s,%s) returning *""",
#                 (post.email,post.hashed_password))
#     new_post=arslan.fetchone()
#     conn.commit()
#     return (new_post)
# ===============================================================================
# @app.get("/hello")
# def read_users(lol: Session = Depends(get_db)):
#     puss=lol.query(models.User).all()
#     return("data",puss)
# @app.post("/hello")
# def read_users( post:new_posted,lol: Session = Depends(get_db)):
#     created=models.User(**post.dict())
#     lol.add(created)
#     lol.commit()
#     lol.refresh(created)
#     return{"status":created}
# @app.get("/hello/{id}")
# def read_users( id:int,lol: Session = Depends(get_db)):
#     post=lol.query(models.User).filter(models.User.id==id).first()
#     return("your post",post)
# @app.delete("/hello/{id}")
# def read_users( id:int,lol: Session = Depends(get_db)):
#     deleted_post=lol.query(models.User).filter(models.User.id==id)
#     if deleted_post.first()==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="lol")
#     deleted_post.delete(synchronize_session=False)
#     lol.commit()
#     return("your post deleted successfully")

# @app.delete("/test/{user_id}")
# def test(user_id: int, db: Session = Depends(get_db)):
#     dell = db.query(models.User).filter(models.User.id == user_id)
#     print(dell.first())
#     dell.delete(synchronize_session=False)
#     db.commit()
#     return {'message': 'maa choda'}
# @app.delete("/hello/{id}")
# def read_users( id:int,lol: Session = Depends(get_db)):
#     deleted_post=lol.query(models.User).filter(models.User.id==id)
#     if deleted_post.first()==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='ok')
#     deleted_post.delete(synchronize_session=False)
#     lol.commit()
#     return("your post deleted successfully")

# @router.post("/vots",status_code=status.HTTP_201_CREATED)
# def vots(vote:schemas.vots,db:Session=Depends(database.get_db),current_user:int=Depends(oath2.get_current_user)):
#     vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
#     found_vote=vote_query.first()
#     if (vote.dir==1):
#         if found_vote:
#             raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="you already like it")
#         new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
#         db.add(new_vote)
#         db.commit()
#         return {"message":"successfully added"}
#     else:
#         if not found_vote:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="not found")
#         vote_query.delete(synchronize_session=False)
#         db.commit()
#         return {"message":"successfully deleted vote"}