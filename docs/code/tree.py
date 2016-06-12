from appJar import gui
def dClick(btn):
    print("dclick:",btn)
def press(btn):
    print("press:", app.getTree("t1"))
app=gui("Tree", "800x800")
app.addTree("t1",
            """<people>
            <person><name>Fred</name><age>45</age><gender>Male</gender></person>
            <person><name>Tina</name><age>37</age><gender>Female</gender></person>
            <person><name>CLive</name><age>28</age><gender>Male</gender></person>
            <person><name>Betty</name><age>51</age><gender>Female</gender></person>
            </people>""")
app.addTreeFunction("t1", dClick)
app.setTreeWidth("t1", 500)
app.setTreeHeight("t1", 500)
app.addButton("PRESS", press)
app.go()
