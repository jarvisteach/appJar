from appJar import gui

def pos(btn):
    if btn=="top":
        app.setPagedWindowTop("pager", True)
    elif btn=="bottom":
        app.setPagedWindowTop("pager", False)
    elif btn=="hide":
        app.showPageLabel("pager", False)
    elif btn=="show":
        app.showPageLabel("pager", True)

app=gui("Pages")
app.addToolbar(["top", "hide", "show","bottom"], pos)

app.startPagedWindow("pager")

app.addPage("pager")
app.addLabel("l11", "Label 1")
app.addLabel("l12", "Label 1")
app.addLabel("l13", "Label 1")
app.stopPage()

app.addPage("pager")
app.addLabel("l21", "Label 2")
app.addLabel("l22", "Label 2")
app.addLabel("l23", "Label 2")
app.addLabel("l24", "Label 2")
app.stopPage()

app.addPage("pager")
app.addLabel("l3", "Label 3")
app.stopPage()

app.addPage("pager")
app.addLabel("l4", "Label 4")
app.stopPage()

app.addPage("pager")
app.addLabel("l5", "Label 5")
app.stopPage()

app.addPage("pager")
app.addLabel("l6", "Label 6")
app.stopPage()

app.stopPagedWindow()
app.go()
