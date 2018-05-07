import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    with app.pagedWindow("Pages"):
        for i in range(10):
            with app.page():
                for x in range(10):
                    app.label(str(i)+str(x))
