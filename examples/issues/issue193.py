import sys
sys.path.append("../../")

from appJar import gui

app=gui()

app.addFileEntry("f1")
app.addDirectoryEntry("d1")

app.go()
