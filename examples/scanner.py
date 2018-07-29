import sqlite3

create_q = """CREATE TABLE IF NOT EXISTS pupils (
        id  VARCHAR(20),
        name VARCHAR(50),
        year int
    )"""

select_q = "select * from pupils"

with sqlite3.connect("register.db") as db:
    db.cursor().execute(create_q)
    
