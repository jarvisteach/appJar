import sys
sys.path.append("../../")

from appJar import gui
app=gui("Demo")
app.addLabel("l1", "Installer Demo")
app.go()
