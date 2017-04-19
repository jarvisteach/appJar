import sys
import logging
sys.path.append("../../")

levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def changed(btn):
    app.setLogLevel(app.getOptionBox("LogLevel"))

def filer(btn):
    if app.getRadioButton("place") == "File":
        app.setLogFile("a.log")

def submit(level):
    msg = app.getEntry(level)
    app.logMessage(msg, level)

from appJar import gui
app=gui("Logging")

app.addLabel("l1", "Logging demo", 0, colspan=2)
app.addLabelOptionBox("LogLevel",levels, 1, colspan=2) 
app.setOptionBoxChangeFunction("LogLevel", changed)

app.addRadioButton("place", "Console", 2, column=0)
app.addRadioButton("place", "File", 2, column=1)
app.setRadioButtonChangeFunction("place", filer)

app.startLabelFrame("Generate Msg", row=3, colspan=2)
for level in levels:
    app.addEntry(level)
    app.setEntryDefault(level, level)
    app.setEntrySubmitFunction(level, submit)
app.stopLabelFrame()

app.go()

