import sys
sys.path.append("../../")

def here(btn=None):
    while True:
        print("A")

from appJar import gui

app=gui()

app.addLabel("l0", "Some Text")
app.addLabel("l1", "Some Text", row=0, column=1)

app.setExpand("NONE")
app.addLabel("l2", "Some Text")
app.setLabelBg("l2", "red")

app.setExpand("ALL")
app.addLabel("l3", "Some Text", row=1, column=1)
app.setLabelBg("l3", "green")
app.after(10000, here)

app.go()
