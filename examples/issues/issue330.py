import sys
sys.path.append("../../")
from appJar import gui

style = "Times 20 italic underline"

app=gui()
app.addLabel("f1", "Choose a file:", row=0, column=0)
app.addLabelFileEntry("file", row=0, column=1)
#app.getEntryWidget("file").config(font="Times 20 italic underline")
#app.getLabelWidget("file").config(font="Times 20 italic underline")
app.setFont(20, style)
app.go()
