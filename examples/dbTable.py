import sys
sys.path.append("../")

LABS = {'view':'Table View',
        'run':'Run SQL',
        'log':'Log'
        }
DB = 'demoDb.sqlite'
import time
import sqlite3
conn = sqlite3.connect(DB)
from appJar import gui
sqlUpdate = False

def setFocus(tab):
    global sqlUpdate
    log("Tab changed to " + tab)
    if tab == LABS['run']:
        app.after(100, app.setTextAreaFocus, LABS['run'])
    elif tab == LABS['view']:
        if sqlUpdate:
            app.refreshDbTable(LABS['view'])
            app.refreshDbOptionBox(LABS['view'])
            sqlUpdate = False

def updateTable(tbl):
    app.replaceDbTable(LABS['view'], DB, app.option(LABS['view']))

def log(msg):
    d = time.strftime('%a %H:%M:%S') + ": "
    app.text(LABS['log'], d + msg+"\n")
    app.textAreaTagPattern(LABS["log"], "date", d)

def loadSQL(btn):
    if btn == "create":
        app.text(LABS['run'], "CREATE TABLE " + app.option(LABS['view']) + " (col type, col type)", replace=True)
    elif btn == "update":
        app.text(LABS['run'], "ALTER TABLE " + app.option(LABS['view']) + " ADD COLUMN 'col' type", replace=True)
    elif btn == "insert":
        app.text(LABS['run'], "INSERT INTO " + app.option(LABS['view']) + " (cols) VALUES (vals)", replace=True)
    elif btn == "select":
        app.text(LABS['run'], "SELECT * FROM " + app.option(LABS['view']), replace=True)

def runSQL(action):
    global sqlUpdate
    if action == "Clear":
        app.clearTextArea(LABS['run'])
        app.message(LABS['run'], '', bg='grey')
        log("SQL cleared")
    elif action == 'Run':
        app.setMessage(LABS['run'], "")
        sql = app.text(LABS['run']).strip()
        if len(sql) > 0:
            try:
                cur = conn.cursor()
                success = cur.execute(sql)
                conn.commit()
                log("Run SQL - " + sql)
                data = cur.fetchall()
                if not success:
                    app.message(LABS['run'], "Query failed", bg='red')
                else:
                    if len(data) == 0:
                        app.message(LABS['run'], "No rows returned", bg='orange')
                    else:
                        app.message(LABS['run'], data, bg='green')
                    sqlUpdate = True
            except sqlite3.OperationalError as e:
                app.message(LABS['run'], str(e), bg='red')
                log(str(e))
        else:
            app.message(LABS['run'], '', bg='grey')
    app.setTextAreaFocus(LABS['run'])

with gui("DB Editor", '400x400', bg='pink') as app:
    with app.tabbedFrame("tabs") as tf:
        tf.config(command=setFocus)
        with app.tab(LABS['view']):
            app.addDbOptionBox(LABS['view'], DB, sticky='ne', stretch='column', change=updateTable)
            app.sticky='news'
            app.addDbTable(LABS['view'], DB, app.option(LABS['view']), sticky='news', stretch='both')
        with app.tab(LABS['run']):
            app.label(LABS['run'], sticky='new', stretch='column')
            app.text(LABS['run'], sticky='news', stretch='both')
            app.message(LABS['run'], '', bg='grey', border=2)
            app.setMessageWidth(LABS['run'], 300)
            app.buttons(["create", "update", "insert", "select"], loadSQL)
            app.buttons(["Run", "Clear"], runSQL, sticky='sew', stretch='column')
        with app.tab(LABS['log']):
            app.text(LABS['log'])
            app.disableTextArea(LABS['log'])
            app.textAreaCreateTag(LABS['log'], "date", foreground="blue")

conn.commit()
conn.close()
