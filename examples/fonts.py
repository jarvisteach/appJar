import sys
sys.path.append("../")

from appJar import gui
app=gui("Font Styles")
app.addLabel("l1", "Times")
app.addLabel("l2", "Comic Sans")
app.addLabel("l3", "Helvetica")
app.addLabel("l4", "Sans Serif")
app.addLabel("l5", "Verdana")
app.addLabel("l6", "Courier")

app.getLabelWidget("l1").config(font="Times 20 italic underline")
app.getLabelWidget("l2").config(font=("Comic Sans", "20", "normal"))
app.getLabelWidget("l3").config(font="Helvetica 20 underline")
app.getLabelWidget("l4").config(font=("Sans Serif", "20", "bold"))
app.getLabelWidget("l5").config(font="Verdana 20 overstrike")
app.getLabelWidget("l6").config(font="Courier 20")

app.go()
