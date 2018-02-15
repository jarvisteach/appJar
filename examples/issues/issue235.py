import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(
        app.label("title"),
        app.label("title2"),
        app.entry("data"),
        app.button("Clap"),
        app.radio("happy"),
        app.date("date"),
        app.check("Clap"),
        app.option("feelings"),
        app.spin("feelings"),
        app.listbox("feelings"),
        app.scale("happiness"),
        app.message("mess"),
        app.text("mess2"),
        app.meter("Cry"),
        app.link("Cry"),
        app.link("Shout"),
        app.image("img"),
        app.image("img2"),
        app.properties("Toppings"),
    )

    app.label("title2", "not empty")
    app.meter("Cry", app.scale("happiness"), text="fred")
    app.meter("CryingMore", app.slider("happiness again"))
    app.meter("CryingMorer", app.scale("happiness again"), text="alphabet")
    app.meter("CryingMorerr", (app.slider("happiness again"),app.scale("happiness again")))

    updateApp4()

def updateApp4(btn=None):
    app.label("title", "aaa")
    app.label("title2", "aaa")
    app.meter("Cry", 50)
    app.entry("data", "aaa")
    #    app.date("date")
    app.button("Clap", updateApp4)
    app.radio("happy", "Miserable")
    app.check("Clap", True)
    app.option("feelings", 1)
    app.spin("feelings", 2)
    app.listbox("feelings", 3)
    app.scale("happiness", 50)
    app.message("mess", "aaa")
    app.text("mess2", "aaa")
    app.meter("Cry", 50)
    app.link("Cry", "http://www.oggle.com")
    app.link("Shout", updateApp4)
#    app.image("img")
#    app.image("img2")
    app.properties("Toppings", {"a":False, "b":True})

with gui("Simple Demo") as app:
    with app.tabbedFrame("tp"):
        with app.tab("part1"):
            app.label("title", "Simple Props Demo", colspan=3, kind="flash")
            app.label("title2", row=0, column=3)
            app.setLabelBg("title", "green")

            app.radio("happy", "Very Happy", row=1, column=0)
            app.radio("happy", "Ambivalent", row=1, column=1)
            app.radio("happy", "Miserable", row=1, column=2, selected=True)

            app.message("mess", "Simple Sadness", row=2, rowspan=3)
            app.setMessageBg("mess", "pink")

            app.text("mess2", "Simple Happiness", row=2, column=2, rowspan=3, scroll=False)
            app.setTextAreaBg("mess2", "pink")

            app.image("img", "../images/balloons.gif", over="../images/balloons2.gif", row=2, column=3, rowspan=7)
            app.image("img2", "OPEN", row=2, column=4, rowspan=3, kind="icon")

            app.check("Clap", row=2, column=1)
            app.check("Cheer", True, row=3, column=1)
            app.check("Cry", row=4, column=1)

            app.entry("data", colspan=3, kind="directory")
            app.entry("data2", value="lots of data", colspan=3, focus=True, case="upper", limit=15)
            app.entry("data3", colspan=3, default="france", kind="validation")
            app.entry("data4", value=["a", "aa", "aba", "abc", "abd"], colspan=3, kind="auto", rows=4)

            row=app.gr()

        with app.tab("part2"):
            app.button("Clap", press, icon="OPEN", row=row, column=0, anchor="n")
            app.button("Cheer", press, row=row, column=1)
            app.button("Cheer", "")
            app.button("Cry", press, row=row, column=2)

            app.date("date", 2002, toValue=2020, row=row, column=3, rowspan=4)

            app.scale("happiness", colspan=3, increment=1, show=True, change=press)


            row=app.gr()
            app.option("feelings", ["happy", "bored", "angry"], column=0, row=row)
            app.spin("feelings", ["happy", "bored", "angry"], column=1, row=row, item="angry")
            app.listbox("feelings", ["happy", "bored", "angry"], column=2, row=row, rows=4, multi=True, group=True)

            app.separator(colspan=3)
            app.spin("vals", 4, endValue=10, colspan=3, pos=3)
            app.separator(colspan=3, direction="horizontal")

            row=app.gr()
            app.meter("Cry", row=row, column=0, fill="orange")
            with app.labelFrame("Links", row=row, column=1):
                app.link("Cry", "http://www.google.com")
                app.link("Shout", press)
                app.separator(row=0, column=1, rowspan=2, direction="vertical")
                app.slider("happiness again", 45, row=0, rowspan=2, direction="vertical", column=2, interval=25, change=press)

        with app.tab("part3"):
            app.grip(row=row, column=2)
            toppings={"Cheese":False, "Tomato":False, "Bacon":False,
                        "Corn":False, "Mushroom":False}

            app.properties("Toppings", toppings, row=row, column=2)

            app.meter("CryingMore", 50, colspan=3, kind="other")
            app.meter("CryingMorer", 50, colspan=3, kind="split")
            app.meter("CryingMorerr", (50,70), colspan=3, kind="dual")

        with app.tab("new"):
            app.pie("p1", {"A":50, "B":30, "c":20})
            app.separator(direction="vertical", pos=('p', 1), sticky="ns")
            app.config(sticky="ew")
            app.microbit("mb1", pos=('p', 2))
            app.separator(direction='horizontal', colspan=3)
            app.canvas("c2")
            app.addCanvasCircle("c2", 10, 10, 30)
        with app.tab("plot"):
            app.plot('p1')
        with app.tab("map"):
            app.map("m1", "paris", zoom=3, terrain="Roadmap", size='300x300')

        with app.tab('tree'):
            app.tree("tree",
                    """<people>
                    <person><name>Fred</name><age>45</age><gender>Male</gender></person>
                    <person><name>Tina</name><age>37</age><gender>Female</gender></person>
                    <person><name>CLive</name><age>28</age><gender>Male</gender></person>
                    <person><name>Betty</name><age>51</age><gender>Female</gender></person>
                    </people>""")
