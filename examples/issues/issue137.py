import sys
sys.path.append("../../")
from appJar import gui

app=gui()
app.addFileEntry("e1")
app.addDirectoryEntry("d1")
app.go()
