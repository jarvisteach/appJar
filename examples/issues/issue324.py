import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "UP": app.increaseFont()
    elif btn == "DOWN": app.decreaseFont()
    elif btn == "MEUP": app.setTabFont("tabs", **style)
    elif btn == "MEDOWN": app.decreaseFont()

with gui("TabTest") as app:
    style={"size":40}
    app.label("title", "Tab Tester Demo", fg="blue", font=style)
    app.setLabelFont
    with app.tabbedFrame("tabs") as tabs:
        with app.tab("Tab One"):
            app.label("t1", "Tab One")
        with app.tab("Tab Two"):
            app.label("t2", "Tab Two")
        with app.tab("Tab Three"):
            app.label("t3", "Tab Three")

    app.addButtons(["UP", "DOWN"], press)
    app.addButtons(["MEUP", "MEDOWN"], press)
    with app.tabbedFrame("2tabs") as tabs:
        with app.tab("Tab One"):
            app.label("2t1", "Tab One")
        with app.tab("Tab Two"):
            app.label("2t2", "Tab Two")
        with app.tab("Tab Three"):
            app.label("2t3", "Tab Three")

