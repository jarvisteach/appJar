import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    with app.tabbedFrame("tabs"):
        with app.tab("Tab 1"):
            with app.labelFrame("Label Frame 1"):
                app.label("a", "A label")
            with app.labelFrame("Label Frame 2"):
                app.label("b", "Another label")
        with app.tab("Tab 2"):
            with app.labelFrame("Label Frame 3"):
                app.label("2a", "A label")
            with app.labelFrame("Label Frame 4"):
                app.label("2b", "Another label")

