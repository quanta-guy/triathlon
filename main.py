from fastapi import FastAPI
from helper import worker 
import uvicorn
from urllib.parse import urlparse
app = FastAPI()



@app.get('/books')
def first_user(Genre: str="",author: str="",page:int=1,limit:int=10 ):
    data=worker.read_db(Genre,author)
    current_page_index=page

    next_page_index=current_page_index+1
    total_books=len(data['id'].values())
    total_pages=total_books/limit
    if total_pages==1:
        next_page_index=None
    next_page_url=f'http://localhost:8000/books?genre={Genre}&author={author}&page={next_page_index}&limit={limit}'
    books=list(data['title '].values())
    end_limit=limit*page if len(books)>limit*page else len(books)
    books=books[((limit*page)-limit):end_limit]
    if current_page_index-1!=0 :
        previous_page= current_page_index-1
    else:
            previous_page=None
    response={'current_page':page,'total_books':total_books,'total_pages':total_pages,'next_page':next_page_url,'previous_page':previous_page,'books':books}
    return response



@app.get('/books/{id}')
def first_user():
    data=worker.read_db(id)
   
    return data




if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)