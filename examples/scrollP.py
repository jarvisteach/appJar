import sys
sys.path.append("../")
from appJar import gui

app=gui("Scroll Pane", "900x300")
app.setSticky("nsew")
app.startPagedWindow("Pages")
app.startPage()

app.addLabel("l1", "Welcome to ScrollPane Demo", 0, 0, 3)
app.setLabelBg("l1", "peru")

app.addLabel("l2", "", 1, 0, 0, 4)
app.setLabelBg("l2", "peru")

app.startScrollPane("sp", 1, 1, 0, 0)
for x in range(10):
    for y in range(5):
        title=str(x)+str(y)
        app.addLabelEntry(title, x, y)
app.stopScrollPane()

app.addLabel("l3", "", 1, 2, 0, 4)
app.setLabelBg("l3", "peru")

app.addLabel("l4", "", 4, 1)
app.setLabelBg("l4", "peru")

app.stopPage()
app.startPage()
app.addLabel("2","2")
app.stopPage()
app.stopPagedWindow()

app.go()
