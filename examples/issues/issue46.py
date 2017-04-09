import sys
sys.path.append("../../")

from appJar import gui

app=gui()
app.addMenuItem("Help", "About", app.appJarAbout)
app.addMenuItem("Help", "Help", app.appJarHelp)
app.addLabel("l1", "Test menus...")
app.go()
