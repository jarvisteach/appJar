from appJar import gui

def toggle(btn):
    if btn=="toggle": app.toggleToggleFrame("Options")
    elif btn=="disable":
        app.setToggleFrameState("Options","disabled")
    elif btn=="enable":
        app.setToggleFrameState("Options", "normal")
    elif btn=="state": print(app.getToggleFrameState("Options"))

app=gui()
app.setFont(20)

app.startToggleFrame("Options")
app.addCheckBox("Show this")
app.addCheckBox("Show that")
app.addCheckBox("Show the other")
app.setCheckBox("Show that")
app.stopToggleFrame()

app.addButtons(["toggle", "disable", "enable", "state"], toggle)

app.setToggleFrameBg("Options", "yellow")

app.go()
