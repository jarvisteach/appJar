import sys
sys.path.append("../")
from appJar import gui

app=gui()
app.setFont(20)
#app.setSticky("W")

app.addCheckBox("Apples")
app.addCheckBox("Pears")
app.addCheckBox("Oranges")
app.addCheckBox("Kiwis")

#app.setCheckBoxWidth("Apples", 10)
#app.setCheckBoxWidth("Pears", 10)
#app.setCheckBoxWidth("Oranges", 10)
#app.setCheckBoxWidth("Kiwis", 10)

app.setCheckBox("Oranges")

app.go()
