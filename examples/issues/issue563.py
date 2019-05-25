import sys
sys.path.append("../../")

from appJar import gui

def showme():
    entries = app.getAllInputs(includeEmptyInputs=False)
    columns = ','.join(entries.keys())
    print(columns)

with gui() as app:
    app.label('hello world')
    app.entry('a', label=True)
    app.entry('b', label=True)
    app.entry('c', label=True)
    app.entry('d', label=True)
    app.button("showme", showme)

