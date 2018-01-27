import sys
sys.path.append("../")
from appJar import gui

clicked = False
animated = True


photo="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"

def changePic(btn):
    if btn == "clickme":
        global clicked
        if clicked: app.image("clickme", "balloons.gif")
        else: app.image("clickme", "balloons2.png")
        clicked = not clicked
    elif btn == "No reload":
        app.image("no_reload", "balloons.gif")
    elif btn == "Reload":
        app.reloadImage("reload", "balloons.gif")
    elif btn == "Stop":
        global animated
        if animated:
            app.stopAnimation("animated")
            app.button("Stop", "Start")
        else:
            app.startAnimation("animated")
            app.button("Stop", "Stop")
        animated = not animated
    elif btn == "Speed":
        app.setAnimationSpeed("animated", app.getScale("Speed"))
    elif btn == "Zoom":
        app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
    elif btn == "Open":
        imgPath = app.openBox(title="Open Image", dirName="images", fileTypes=[('images', '*.png'), ('images', '*.jpg'), ('images', '*.gif'), ('images', '*.jpeg'), ('all', '*')])
        if imgPath != "":
            try:
                app.image("Open", imgPath)
            except:
                app.errorBox("File error", "Unable to open image: " + str(imgPath))

with gui("Image Test") as app:
    app.setImageLocation("images")

    with app.labelFrame("Image Data", 0, 0, sticky="ew"):
        app.image("imgdata", photo, kind="data")

    with app.labelFrame("Compound Image", 1, 0):
        app.image("cimage", "balloons.gif", compound="top")

    def imgMap(pos):
        print(pos)

    with app.labelFrame("ImageMap", 0, 1):
        mapData = {"Yellow": [15,52,77,138], "Red":[75,1,129,138], "White":[137,15,184,127]}
        app.image("simple", "balloons.gif", submit=imgMap, map=mapData)

    with app.labelFrame("Mouse Over", 0, 2):
        app.image("mo_1", "balloons.gif", over="balloons2.png")

    with app.labelFrame("Click Me", 0, 3):
        app.image("clickme", "balloons.gif", submit=changePic)

    with app.labelFrame("Zoom", 0, 4, sticky="ew"):
        app.setPadding([5,5])
        with app.scrollPane("sp"):
            app.image("Zoom", "balloons.gif")
        app.spin("Zoom", [20,5, 4, 3, 2, 1, -2, -3, -4, -5, -6, -7, -8, -9], label=True, change=changePic, item=1)

    with app.labelFrame("No reload", 1, 1, sticky="ew"):
        app.image("no_reload", "balloons.gif")
        app.button("No reload", changePic)

    with app.labelFrame("Reload", 1, 2, sticky="ew"):
        app.image("reload", "balloons.gif")
        app.button("Reload", changePic)

    with app.labelFrame("Animated", 1, 3, sticky="ew"):
        app.image("animated", "animated_balloons.gif")
        app.scale("Speed", label=True, interval=50, show=True, range=(1,200), value=50, change=changePic)
        app.button("Stop", changePic)

    with app.labelFrame("Open", 1, 4, sticky="ew"):
        app.image("Open", "balloons3.jpg")
        app.button("Open", changePic)
