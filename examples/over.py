from appJar import gui

def enter(btn):
    print("IN:", btn)

def leave(btn):
    print("OUT:", btn)

app=gui()
app.addLabel("l1", "Testing...")
app.setLabelOverFunction("l1", [enter, leave])
app.go()
