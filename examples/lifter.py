import sys
sys.path.append("../")

from appJar import gui

with gui("LIFTER") as app:

    with app.tabbedFrame("tabs"):
        with app.tab("tab 1"):
            for x in range(20):
                app.label("T0"+str(x))
        with app.tab("tab 2"):
            for x in range(20):
                app.label("T2"+str(x))
        with app.tab("tab 3"):
            for x in range(20):
                app.label("T3"+str(x))
        with app.tab("tab 4"):
            for x in range(20):
                app.label("T4"+str(x))
        with app.tab("tab 5"):
            for x in range(20):
                app.label("T5"+str(x))
        with app.tab("tab 6"):

            with app.pagedWindow("PAGES"):
                with app.page():
                    for x in range(20):
                        app.label("0"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("1"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("2"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("3"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("4"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("5"+str(x))
                with app.page():
                    for x in range(20):
                        app.label("6"+str(x))
