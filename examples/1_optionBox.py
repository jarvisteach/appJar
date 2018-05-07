import sys
sys.path.append("../")
from appJar import gui
options=["Blur", "Queen", "Oasis", "One Direction"]
app=gui("OptionBox Demo", "200x200")

app.setFont(20)
app.setBg("red")
app.addOptionBox("options", options)
app.setOptionBoxFg("options", "orange")
app.setOptionBoxBg("options", "green")

app.go()
