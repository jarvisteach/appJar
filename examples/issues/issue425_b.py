import sys
sys.path.append("../../")

from appJar import gui

count = 0
def press():
    global count
    app.entry("NEW" + str(count))
    count += 1

with gui() as app:
    app.label('hello world')
    app.button("ADD ENTRY", press)
