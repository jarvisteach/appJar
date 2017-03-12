import sys
sys.path.append("../")
from appJar import gui

app=gui("Tester","100x50")
app.setFont(20)
app.addLabel("l1", "Welcome to ScrollFrame")

app.startScrollPane("sf")
app.addLabel("l2", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
app.addLabel("l3", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
app.addLabel("l4", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
app.addLabel("l5", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
app.go()

