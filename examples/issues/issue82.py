import sys
sys.path.append("../../")

from appJar import gui

counter = 5

def looper(btn=None):
    global counter
    print(btn, "a", counter)
    if counter == 0: app.stop()
    counter -= 1

with gui() as app:
    app.addLabel("l1", "app")
    app.registerEvent(looper)

with gui() as app2:
    app2.addLabel("l1", "app2")

with gui() as app3:
    app3.addLabel("l1", "app3")

with gui() as app4:
    app4.addLabel("l1", "app4")
