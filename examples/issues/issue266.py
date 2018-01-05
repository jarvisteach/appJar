import sys
sys.path.append("../../")

def delRow(val):
    print(val)

def addRow(val):
    print(val)

def changeDb(val):
    print(val)
    app.replaceDbGrid("projects", "issue266.db", app.list("table")[0])

from appJar import gui

def setup():
    import sqlite3
    from sqlite3 import Error

    proj = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''
    task = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''

    with sqlite3.connect("issue266.db") as conn:
        c = conn.cursor()
        c.execute( """ CREATE TABLE IF NOT EXISTS projects (
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        begin_date text,
                        end_date text
                    ); """)

        c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        priority integer,
                        status_id integer NOT NULL,
                        project_id integer NOT NULL,
                        begin_date text NOT NULL,
                        end_date text NOT NULL,
                        FOREIGN KEY (project_id) REFERENCES projects (id)
                    );""")

        c.execute(proj, ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30'))
        project_id = c.lastrowid
        c.execute(task, ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02'))
        c.execute(task, ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05'))

with gui("DB Demo", "800x400") as app:
    app.setStretch("column")
    app.label("title", "DB tester")
    app.list("table", ["projects", "tasks"], change=changeDb, rows=2)
    app.setStretch("both")
    app.addDbGrid("projects", "issue266.db", "projects", action=delRow, addRow=addRow, showMenu=True)
