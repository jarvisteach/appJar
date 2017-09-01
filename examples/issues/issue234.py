import sys
sys.path.append("../../")
from appJar import gui

with gui() as app:
    with app.panedFrame("pf"):
        with app.pagedWindow("pw"):
            with app.page(sticky="news"):
                with app.labelFrame("l1", sticky="nsew"):
                    app.addLabel("l1", "some text")
            with app.page():
                with app.labelFrame("l2"):
                    app.addLabel("l2", "some text")
            with app.page():
                with app.labelFrame("l3"):
                    app.addLabel("l3", "some text")
