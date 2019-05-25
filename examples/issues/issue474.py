import sys
sys.path.append("../../")

import time
from appJar import gui

def press():
    app.text("log", app.entry("Text:")+"\n")

def logText():
    name='a'
    while True:
        app.queueFunction(app.text, "log", "new data\n")
        time.sleep(1)
        app.queueFunction(app.openTab, "tabs", "Data")
        app.queueFunction(app.label, name)
        app.queueFunction(app.stopTab)
        name += "a"

with gui() as app:
    with app.tabbedFrame("tabs"):
        with app.tab("Log"):
            app.text("log", scroll=True)
        with app.tab("Data"):
            app.entry("Text:", label=True, submit=press)
            app.button("Submit", press)

    app.thread(logText)
