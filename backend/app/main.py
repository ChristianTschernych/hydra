import enum
from fastapi import FastAPI, Response, status, HTTPException
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    category: int
    private: bool = True
    rating: Optional[int] = None
    id: int = None

categories = ["Travel", "Food", "Shopping", "Retro"]
my_posts = [{"title":"Title of post 1", "content":"content of post 1", "id":0},
{"title":"FoodBoy", "content":"I like pizza", "id":1}]

def find_post(id:int):
    for post in my_posts:
        if post['id'] == id:
            return {"data" : post}

def delete_post(id:int):
    for ind, post in enumerate(my_posts):
        if post["id"] == id:
            print(ind)
            my_posts.pop(ind)
            print(f"Post {id} was deleted!")
            return post

def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i
    return None




@app.get("/")
def check():
    return {"message": "Hello World. This is fastAPI speaking!"}

@app.get("/posts")
def check():
    return {"data" : my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    new_post = new_post.dict()
    print("Added Post:")
    print(new_post)
    #new_post.id = len(my_posts)
    new_post['id'] = randrange(0, 10000)
    my_posts.append(new_post)
    return {"data": new_post}

#Id ist ein path parameter
@app.get("/posts/{id}")
def get_post(id:int):
    #important to convert to int
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= {"message":f"post with id {id} was not found!"})

        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message":f"post with id {id} was not found!"}
    return {"data" : post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_post(id:int):
    post = delete_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"Post with id {id} could not be deleted!"})

    return {"message" : f"Post with id {id} was deleted!"}

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={"message": f"Post with id {id} could not be updated!"})
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"message":post_dict}