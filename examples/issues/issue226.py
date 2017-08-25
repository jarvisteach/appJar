import sys
sys.path.append("../../")

from appJar import gui
def press(btn):
    print(btn)


app = gui()

app.addFileEntry("f1")
app.setFileEntryChangeFunction("f1", press)

app.addDirectoryEntry("f2")
app.setFileEntryChangeFunction("f2", press)
app.setEntrySubmitFunction("f2", press)

app.addEntry("f3")
app.setEntryDefault("f3", "default")
app.setEntryChangeFunction("f3", press)

app.go()
