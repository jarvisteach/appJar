import sys
sys.path.append("../../")

from appJar import gui

with gui('canvas demo') as app:
    app.bg = 'green'
    app.setSticky('')
#    app.stretch = 'none'
    app.addCanvas("c1")
    app.addCanvasOval("c1", 10, 10, 500, 100, fill="red", outline="blue", width=3)
    app.addCanvasLine("c1", 0, 0, 255, 255, width=5)
    app.setCanvasBg('c1', 'yellow')
    app.setCanvasWidth('c1', 550)
