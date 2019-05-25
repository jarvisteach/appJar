import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    for i in range(10):
        app.label(i*100)

    app.button('CLEAR', app.clearAllLabels)
