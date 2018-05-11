import sys
sys.path.append("../../")

from appJar import gui

with gui("GUI", "600x600") as app:
#    app.label("after", pos=(0, 4, 1, 3), bg="yellow")
#    app.addCanvasImage("c1", 0, 0, "bg.jpg")
#    app.label('top left', pos=(0,0,1,1), bg="red", sticky="", stretch="none")
#    app.label('top right', pos=(0,2,1,1), bg="blue", sticky="", stretch="none")
#
#    app.button("PRESS", None, pos=(1,1,1,1))
#
#    app.label('bottom left', pos=(2,0,1,1), bg="green", sticky="", stretch="none")
#    app.label('bottom right', pos=(2,2,1,3), bg="pink", stretch="none")

    app.label("one", pos=(0,1,2,2), bg="red", sticky="news")
    app.label("two", pos=(0,3,2,2), bg="orange", sticky="news")

    app.label("three", pos=(2,1,2,2), bg="yellow", sticky="news")
    app.label("four", pos=(2,3,2,2), bg="green", sticky="news")

    app.label("mid", pos=(1,1,2,2), bg="blue", sticky="news")
 #   app.addCanvas("c1", 1,1,2,2)

    app.label("six", pos=(4,0))
    app.label("seven", pos=(4,1))
    app.label("eight", pos=(4,2))
    app.label("nine", pos=(4,3))
