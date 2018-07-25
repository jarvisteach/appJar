import sys
sys.path.append("../../")

from appJar import gui 

app = gui("appjar font problem", "400x400")
app.setFont(size=16, family="Times", underline=True, slant="italic")

app.addLabel("l1", "Times")
app.addLabel("l2", "Comic Sans")
app.label("l3", "Helvetica", font={'family':'helvetica', 'size':44}, fg='blue')
app.addLabel("l4", "Sans Serif")
app.addLabel("l5", "Verdana")
app.addLabel("l6", "Courier")
app.addLabel("texas", "Texas")

app.go()
