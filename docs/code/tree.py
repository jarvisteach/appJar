from appJar import gui
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
#app.setTreeWidth("t1", 500)
#app.setTreeHeight("t1", 500)
app.addButton("PRESS", press)
app.go()
