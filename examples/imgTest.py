import sys
sys.path.append("../")
from appJar import gui

clicked = False
animated = True

def changePic(btn):
    if btn == "clickme":
        global clicked
        if clicked: app.setImage("clickme", "balloons.gif")
        else: app.setImage("clickme", "balloons2.png")
        clicked = not clicked
    elif btn == "No reload":
        app.setImage("no_reload", "balloons.gif")
    elif btn == "Reload":
        app.reloadImage("reload", "balloons.gif")
    elif btn == "Stop":
        global animated
        if animated:
            app.stopAnimation("animated")
            app.setButton("Stop", "Start")
        else:
            app.startAnimation("animated")
            app.setButton("Stop", "Stop")
        animated = not animated
    elif btn == "Speed":
        app.setAnimationSpeed("animated", app.getScale("Speed"))
    elif btn == "Zoom":
        app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
    elif btn == "Open":
        imgPath = app.openBox(fileTypes=[('images', '*.png'), ('images', '*.jpg'), ('images', '*.gif')])
        if imgPath != "":
            try:
                app.setImage("Open", imgPath)
            except:
                app.errorBox("File error", "Unable to open image: " + str(imgPath))

app=gui("Image Test")

app.setImageLocation("images")

app.startLabelFrame("Simple", 0, 0)
app.addImage("simple", "balloons.gif")
app.stopLabelFrame()

app.startLabelFrame("Mouse Over", 0, 1)
app.addImage("mo_1", "balloons.gif")
app.setImageMouseOver("mo_1", "balloons2.png")
app.stopLabelFrame()

app.startLabelFrame("Click Me", 0, 2)
app.addImage("clickme", "balloons.gif")
app.setImageFunction("clickme", changePic)
app.stopLabelFrame()

app.startLabelFrame("Zoom", 0, 3)
app.setPadding([10,10])
app.setSticky("ew")
app.addImage("Zoom", "balloons.gif")
app.setImageSize("Zoom", 200,200)
app.addLabelSpinBox("Zoom", [5, 4, 3, 2, 1, -2, -3, -4, -5, -6, -7, -8, -9])
app.setSpinBox("Zoom", 1)
app.setSpinBoxFunction("Zoom", changePic)
app.stopLabelFrame()


app.startLabelFrame("No reload", 1, 0)
app.setSticky("ew")
app.addImage("no_reload", "balloons.gif")
app.addButton("No reload", changePic)
app.stopLabelFrame()

app.startLabelFrame("Reload", 1, 1)
app.setSticky("ew")
app.addImage("reload", "balloons.gif")
app.addButton("Reload", changePic)
app.stopLabelFrame()

app.startLabelFrame("Animated", 1, 2)
app.setSticky("ew")
app.addImage("animated", "animated_balloons.gif")
app.addLabelScale("Speed")
app.showScaleValue("Speed")
app.showScaleIntervals("Speed", 50)
app.setScaleRange("Speed", 1, 200, 50)
app.setScaleFunction("Speed", changePic)
app.addButton("Stop", changePic)
app.stopLabelFrame()

app.startLabelFrame("Open", 1, 3)
app.setSticky("ew")
app.addImage("Open", "balloons3.jpg")
app.addButton("Open", changePic)
app.stopLabelFrame()

app.go()
