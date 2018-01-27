import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
#    app.showSplash("test")
    with app.subWindow("s1"):
        app.addLabel("l1", "text")
    app.showSubWindow("s1")
    app.addGrip()
    app.addScale("sc1")
    with app.tabbedFrame("tf"):
        with app.tab("t1"):
            with app.pagedWindow("p1"):
#                with app.page():
#                    app.addGoogleMap("g1")
                with app.page():
                    app.addTree("t1",
                        """<people>
                        <person><name>Fred</name><age>45</age><gender>Male</gender></person>
                        <person><name>Tina</name><age>37</age><gender>Female</gender></person>
                        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
                        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
                        </people>""")
                    app.setTreeBg("t1", "green")
                with app.page():
                    app.setSticky("NEWS")
                    app.addGrid("g1", [[1, 2, 3,4,5,6,7,8,9,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,11],[1,2,3]])
                    app.setGridHeight("g1", 500)
                    app.setGridWidth("g1", 500)
                with app.page():
                    app.addListBox("lb", ["a", "b", "c"])
                with app.page():
                    app.addButtons(["TXT", "NUM"], [app.textBox, app.numberBox])
                    app.setSticky("NSEW")
                    app.addSelectableLabel("sll", "some text")
                    app.addProperties("p1", {"a":False, "b": True, "c":True})
                    app.setPropertiesBg("p1", "green")
                    app.addAutoEntry("ae", ["a", "b"])
                    app.addHorizontalSeparator()
                    app.addWebLink("l1", "http://www.google.com")
                    app.addLink("l2", None)
                    app.setLinkFg("l2", "pink")
                    app.addHorizontalSeparator()
                    with app.toggleFrame("tf"):
                        app.setToggleFrameState("tf", "disabled")
                        app.addMeter("m1")
                        app.setMeterBg("m1", "yellow")
                        app.addSplitMeter("m2")
                        app.addDualMeter("m3")
                with app.page():
                    app.addTextArea("a")
                    app.addScrolledTextArea("a1")
                with app.page():
                    app.addPieChart("p1", {"a":10, "b":100})
#                with app.page():
#                    app.addMicroBit("mb1")
