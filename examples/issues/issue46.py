import sys
sys.path.append("../../")

from appJar import gui

app=gui()
app.addMenuItem("appJar", "Help", app.appJarHelp)
app.addMenuItem("appJar", "About", app.appJarAbout)
app.addLabel("l1", "Test menus...")
app.go()
