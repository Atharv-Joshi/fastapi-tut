from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
def index(limit: Optional[int] = 10, published: Optional[bool] = True):
    if(published):
        return f'{limit} are published'
    else:
        return f'{limit} are unpublished'


@app.get('/blogs/unpublished')
def index():
    return {'data': 'unpublished blogs'}


@app.get('/blogs/{id}')
def about(id: int):
    return{"data": id}
