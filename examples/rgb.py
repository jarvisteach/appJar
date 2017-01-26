import sys
sys.path.append("../")
from appJar import gui

# funciton to handle the button presses
def btnPress(btnName):
    if btnName == "Reset":
        app.setSpinBox("redSpin", 0)
        app.setSpinBox("greSpin", 0)
        app.setSpinBox("bluSpin", 0)
        app.clearEntry("colCode")
    elif btnName == "Convert":
        RGB = getRGB()
        app.setEntry("colCode", RGB)

# function to convert the scale values to an RGB hex code
def getRGB():
    R = app.getScale("redScale")
    G = app.getScale("greScale")
    B = app.getScale("bluScale")

    R=hex(R).split('x')[1]
    G=hex(G).split('x')[1]
    B=hex(B).split('x')[1]

    if len(R) == 1: R = "0" + R
    if len(G) == 1: G = "0" + G
    if len(B) == 1: B = "0" + B

    RGB = "#"+str(R)+str(G)+str(B)

    return RGB

# funciton to update widgets
def updateRGB(name):
    # split the widget's name into the type & colour
    colour = name[0:3]
    widg = name[3:]
    
    # get the current RGB value
    RGB = getRGB()

    # depending on the type, get & set...
    if widg == "Scale":
        value = app.getScale(name)
        app.setSpinBox(colour+"Spin", value)
    elif widg == "Spin":
        value = app.getSpinBox(name)
        app.setScale(colour+"Scale", value)

    # update the label
    app.setLabelBg("colBox", RGB)
    app.setEntry("colCode", RGB)

app = gui()
app.setBg("#B8DEE2")
app.setGuiPadding(5,5)
app.setFont(18)

# frame to contain sliders
app.startLabelFrame("Colour Codes")
app.setSticky("news")

app.addLabel("redLab", "Red Color (R):", 0, 0)
app.addLabel("greLab", "Green Color (G):", 1, 0)
app.addLabel("bluLab", "Blue Color (B):", 2, 0)

app.setLabelAlign("redLab", "left")
app.setLabelAlign("greLab", "left")
app.setLabelAlign("bluLab", "left")

app.addSpinBoxRange("redSpin", 0, 255, 0, 1)
app.addSpinBoxRange("greSpin", 0, 255, 1, 1)
app.addSpinBoxRange("bluSpin", 0, 255, 2, 1)

app.setSpinBoxWidth("redSpin", 4)
app.setSpinBoxWidth("greSpin", 4)
app.setSpinBoxWidth("bluSpin", 4)

app.setSpinBoxFunction("redSpin", updateRGB)
app.setSpinBoxFunction("greSpin", updateRGB)
app.setSpinBoxFunction("bluSpin", updateRGB)

app.addScale("redScale", 0, 2)
app.addScale("greScale", 1, 2)
app.addScale("bluScale", 2, 2)

app.setScaleRange("redScale", 0, 255)
app.setScaleRange("greScale", 0, 255)
app.setScaleRange("bluScale", 0, 255)

app.setScaleFunction("redScale", updateRGB)
app.setScaleFunction("greScale", updateRGB)
app.setScaleFunction("bluScale", updateRGB)

app.stopLabelFrame()

# frame to hold coloured label
app.startLabelFrame("Colour Preview")

app.setInPadding(5,5)
app.setSticky("news")
app.addEmptyLabel("colBox", 3, 0, 3)
app.setLabelHeight("colBox", 5)
app.setLabelWidth("colBox", 25)
app.setLabelRelief("colBox", "ridge")

app.stopLabelFrame()

# frame with result & buttons
app.startLabelFrame("Actions")

app.addLabel("colCodeLab", "HEX colour code:", 0, 0)
app.addEntry("colCode", 0, 1)
app.disableEntry("colCode")
app.setSticky("EW")
app.addButtons(["Convert", "Reset"], btnPress, 1, 0, 2)

app.stopLabelFrame()

app.go()
