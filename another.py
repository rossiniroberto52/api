import sqlite3

class DBbank():
    def get_from_another_page():
        with sqlite3.connect('DataBase_API.db3') as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            query = "select * from frutas"
            cur.execute(query)
            data = [dict(d for d in cur.fetchall())]
            return data