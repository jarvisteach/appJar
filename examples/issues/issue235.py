import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(
        app.label("title"),
        app.entry("data"),
        app.button("Clap"),
        app.radio("happy"),
        app.check("Clap"),
        app.option("feelings"),
        app.spin("feelings"),
        app.list("feelings"),
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

    app.meter("Cry", app.scale("happiness"))
    app.meter("CryingMore", app.slider("happiness again"))
    app.meter("CryingMorer", app.scale("happiness again"))
    app.meter("CryingMorerr", (app.slider("happiness again"),app.scale("happiness again")))

with gui("Simple Demo") as app:
    app.label("title", "Simple Props Demo", colspan=3, type="flash")
    app.setLabelBg("title", "green")

    app.radio("happy", "Very Happy", row=1, column=0)
    app.radio("happy", "Ambivalent", row=1, column=1)
    app.radio("happy", "Miserable", row=1, column=2, selected=True)

    app.message("mess", "Simple Sadness", row=2, rowspan=3)
    app.setMessageBg("mess", "pink")

    app.text("mess2", "Simple Happiness", row=2, column=2, rowspan=3, scroll=False)
    app.setTextAreaBg("mess2", "pink")

    app.image("img", "../images/balloons.gif", over="../images/balloons2.gif", row=2, column=3, rowspan=3)
    app.image("img2", "OPEN", row=2, column=4, rowspan=3, type="icon")

    app.check("Clap", row=2, column=1)
    app.check("Cheer", True, row=3, column=1)
    app.check("Cry", row=4, column=1)

    app.entry("data", colspan=3, type="directory")
    app.entry("data2", value="lots of data", colspan=3, focus=True, case="upper", limit=15)
    app.entry("data3", colspan=3, default="france", type="validation")
    app.entry("data4", value=["a", "aa", "aba", "abc", "abd"], colspan=3, type="auto", autoRows=4)

    row=app.gr()

    app.button("Clap", press, icon="OPEN", row=row, column=0)
    app.button("Cheer", press, row=row, column=1)
    app.button("Cry", press, row=row, column=2)

    app.date("date", row=row, column=3, rowspan=4)

    app.scale("happiness", colspan=3, increment=1, show=True, change=press)


    row=app.gr()
    app.option("feelings", ["happy", "bored", "angry"], column=0, row=row)
    app.spin("feelings", ["happy", "bored", "angry"], column=1, row=row, item="angry")
    app.list("feelings", ["happy", "bored", "angry"], column=2, row=row, rows=4, multi=True, group=True)

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

#    app.grip(row=row, column=2)
    toppings={"Cheese":False, "Tomato":False, "Bacon":False,
                "Corn":False, "Mushroom":False}

    app.properties("Toppings", toppings, row=row, column=2)

    app.meter("CryingMore", 50, colspan=3, type="other")
    app.meter("CryingMorer", 50, colspan=3, type="split")
    app.meter("CryingMorerr", (50,70), colspan=3, type="dual")
