import sys
sys.path.append("../")
from appJar import gui
canEdit=True
def edited(btn):
    print("EDITED:", btn)

def col(btn):
    #app.setTreeBg("t1", "black")
    #app.setTreeFg("t1", "white")
    #app.setTreeHighlightBg("t1", "white")
    #app.setTreeHighlightFg("t1", "black")
    global canEdit
    canEdit = not canEdit
    app.setTreeEditable("t1", canEdit)
    app.setBg("black")
#    app.setTreeBg("t1", "red")
#    app.setTreeFg("t1", "yellow")
#    app.setTreeHighlightBg("t1", "yellow")
#    app.setTreeHighlightFg("t1", "red")
    app.setTreeColours("t1", "yellow", "red", "red", "yellow")
def dClick(btn):
    print("DBL CLICK:", app.getTreeSelected(btn))

def press(btn):
    print("SELECTED:", app.getTreeSelected("t1"))
    print("ALL:", app.getTreeSelectedXML("t1"))

app=gui("Tree")
app.addTree("t1",
            """<people>
            <person><name>Fred</name><age>45</age><gender>Male</gender></person>
            <person><name>Tina</name><age>37</age><gender>Female</gender></person>
            <person><name>CLive</name><age>28</age><gender>Male</gender></person>
            <person><name>Betty</name><age>51</age><gender>Female</gender></person>
            </people>""")
app.setTreeDoubleClickFunction("t1", dClick)
app.setTreeEditFunction("t1", edited)
app.setTreeEditable("t1", canEdit)
#app.setTreeWidth("t1", 500)
#app.setTreeHeight("t1", 500)
app.addButtons(["PRESS", "YELLOW"], [press, col])
app.go()
