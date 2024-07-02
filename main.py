from fastapi import FastAPI
from another import DBbank
import sqlite3

app = FastAPI()

@app.get("/")
def root():
    return("200 OK")


@app.get("/books")
def get_all_books():
    with sqlite3.connect('DataBase_API.db3') as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            query = "select * from tb_books"
            cur.execute(query)
            #data = [dict(d for d in cur.fetchall())]
            data = cur.fetchall()
            return {"response":"200 OK", "DATA":data}
        
@app.post("/books_add")
def post_new_book(name:str,amount:int):
    with sqlite3.connect('DataBase_API.db3') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = """INSERT INTO tb_books (T_NAME, N_QTD)
                    VALUES( ?, ?)
                """
        book = (name, amount)
        cur.execute(query, book)
        conn.commit()
        data = cur.fetchall()
        return {"response":"200 OK", "DATA":data}
    
@app.post("/books_update")
def update_new_book(book_id:int, name:str, amount:int):
    with sqlite3.connect('DataBase_API.db3') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = """UPDATE tb_books SET T_NAME = ?, N_QTD = ? WHERE N_ID = ?"""
        cur.execute(query, (name, amount, book_id))
        conn.commit()
        data = cur.fetchall()
        return {"response":"200 OK", "DATA":data}
    
@app.delete("/books_delete")
def book_delete(book_id:int):
    with sqlite3.connect('DataBase_API.db3') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = """DELETE FROM tb_books WHERE N_ID = ?"""
        cur.execute(query, book_id)
        conn.commit()
        data = cur.fetchall()
        return {"response":"200 OK", "DATA":data}
        