import sys
sys.path.append("../../")

from appJar import gui
app = gui()
app.setLogLevel('ERROR')


app.startFrame(title="demo")
app.addTable('t', [[2,4],[1,4]] )
app.stopFrame()

app.emptyFrame("demo")

app.go()
