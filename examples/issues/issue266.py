import sys
sys.path.append("../../")

DB_NAME = "issue266.db"
types = ["NULL", "INTEGER", "REAL", "TEXT", "BLOB"]

def makeTable():
    fields = app.getAllEntries()
    types = app.getAllOptionBoxes()
    prim = app.radio("PRIMARY")
    tbName = app.entry("Table Name")

    data = "CREATE TABLE IF NOT EXISTS " + tbName + "("
        

    counter = 0
    while True:
        try:
            data += fields["field"+str(counter)] + " " + types["type"+str(counter)]
            if app.radio("PRIMARY") == "primary"+str(counter):
                data += " PRIMARY KEY"
            data += ", "
            counter += 1
        except:
            break
    data = data[:-2]
    data += ");"
    runSql(data)
    app.changeOptionBox("table", getTables())
    changeDb()

def runSql(sql):
    print(sql)
    data = []
    import sqlite3
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(sql)
        for r in c:
            data.append(r)
    return data

def genRows():
    with app.subWindow("Make Table"):
        row = app.gr()
        with app.labelFrame(app.entry("Table Name")):
            for i in range(int(app.entry("Num Fields"))):
                app.entry("field"+str(i), row=row, column=0)
                app.optionBox("type"+str(i), types, row=row, column=1)
                app.radio("PRIMARY", "primary"+str(i), row=row, column=2)
                row += 1

        app.setFocus("field0")

        app.button("GO", makeTable)

def showMakeTable():
    with app.subWindow("Make Table"):
        app.entry("Table Name", label=True, focus=True, colspan=3)
        app.entry("Num Fields", label=True, kind="numeric", submit=genRows, colspan=3)
    app.showSubWindow("Make Table")

def changeDb():
    app.replaceDbGrid("projects", DB_NAME, app.optionBox("table"))

def getTables():
    query = "SELECT distinct tbl_name from sqlite_master order by 1"
    rows = runSql(query)
    tables = []
    for r in rows:
        tables.append(r[0])
    return tables

from appJar import gui

def setup():
    import sqlite3
    from sqlite3 import Error

    proj = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''
    task = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''

    with sqlite3.connect(DB_NAME) as conn:
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

with gui("DB Demo", "800x600", stretch="column", bg="DarkOrange") as app:
    app.setLogLevel("debug")
    app.label("title", "DB tester", bg="orange", font={'size':20})
    app.config(sticky="NE")
    tables = getTables()
    app.optionBox("table", tables, change=changeDb)
    app.config(sticky="NEWS")
    app.setStretch("both")
    app.addDbGrid("projects", DB_NAME, "projects")
    app.config(sticky="")
    app.button("NEW TABLE", showMakeTable)
