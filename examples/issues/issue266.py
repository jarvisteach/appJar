import sys
sys.path.append("../../")
from appJar import gui

DB_NAME = "issue266.db"
types = ["NULL", "INTEGER", "REAL", "TEXT", "BLOB"]

def press(btn):
    print(app.getTableSelectedCells("table"))
    if btn == 'REFRESH':
        app.refreshDbTable('table')

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

def setup():
    ''' cretes a new database if needed '''
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
        for i in range(10):
            c.execute(task, ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02'))
            c.execute(task, ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05'))

def showMakeTable():
    with app.subWindow("Make Table"):
        app.entry("Table Name", label=True, focus=True, colspan=3)
        app.entry("Num Fields", label=True, kind="numeric", submit=genRows, colspan=3)
    app.showSubWindow("Make Table")

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
    app.refreshDbOptionBox("table", selected=tbName)

def changeDb():
    table = app.optionBox("table")
    app.replaceDbTable("table", DB_NAME, table)
    app.label("title", "DB tester: " + table)

def addRow(a):
    table = app.optionBox("table")
    values = app.table("table")
    sql = "INSERT INTO " + table + " VALUES ("
    for v in values:
        sql += "'" + v + "', "

    sql = sql[:-2] + ")"
    try:
        runSql(sql)
        app.refreshDbTable("table")
    except:
        app.errorBox("SQL Error", "Unable to add row, check id is unique and numeric")

def deleteRow(btn, row=None):
    print(btn, row)
    if row is None:
        btn, row = "Delete", btn
    if btn == "Delete":
        rowData = app.getTableRow('table', row)
        app.selectTableRow("table", row, highlight=True)
        if app.okBox("Delete Row " + str(row), "Are you sure you want to delete row " + str(row) + "?"):
            table = app.optionBox("table")
            sql = "DELETE FROM " + table + " WHERE id='" + str(rowData[0]) + "'"
            runSql(sql)
            app.refreshDbTable("table")
        try: app.selectTableRow("table", row, highlight=False)
        except: pass

# check the database exists, make if not
try:
    con = sqlite3.connect('file:'+DB_NAME+'?mode=rw', uri=True)
except:
    setup()

def edit(btn):
    if btn == "EN": app.editMenu = True 
    else: app.editMenu = False

# create the GUI
#with gui("DB Demo", "800x600", stretch="column", bg="DarkOrange", log="trace", sticky="NE", labelFont = {"size":20, "family":"arial", "slant":"italic"}) as app:
with gui("DB Demo", "800x600", stretch="column", bg="DarkOrange", log="trace", sticky="NE") as app:
#    app.buttonFont = {"size":10, "family":"helvetica", "weight":"bold"}
    app.editMenu = True
    app.createRightClickMenu("demo")
    app.addMenuItem("demo", "STOP", app.stop)

    app.addDbOptionBox("table", DB_NAME, change=changeDb, right="demo")
    app.label("title", "DB tester:", font=60, bg="orange", sticky="EW")
    app.setLabelRightClick("title", "demo")
    app.config(sticky="NEWS", stretch="both")
    app.table("table", DB_NAME, "tasks", kind='database', action=deleteRow, addRow=addRow, actionButton="Delete", showMenu=True, disabledEntries=[0])
    app.setOptionBox("table", "tasks", callFunction=False)
    app.button("NEW TABLE", showMakeTable, sticky="", stretch="column")
    app.label("PRESS ME", font={"size":40, "underline":True}, right="demo")
    app.addButtons(["EN", "DI"], edit)
    app.button("COUNT", press)
    app.button("REFRESH", press)
