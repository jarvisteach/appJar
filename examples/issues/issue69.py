import sys
sys.path.append("../../")

from appJar import gui
app = gui()
app.addTextArea("ta")
app.addScrolledTextArea("sta")
app.go()

