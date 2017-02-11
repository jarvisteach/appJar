import sys
sys.path.append("../")
from appJar import gui

alreadyDone = False

# funciton to handle the button presses
def btnPress(btnName):
    if btnName == "Reset":
        app.setSpinBox("redSpin", 0)
        app.setSpinBox("greSpin", 0)
        app.setSpinBox("bluSpin", 0)
    elif btnName == "Log":
        RGB = getRGB()
        if RGB in app.getAllListItems("colours"):
            app.selectListItem("colours", RGB)
        else:
            app.addListItem("colours", RGB)
            app.setListItemBg("colours", RGB, RGB)
            app.setListItemFg("colours", RGB, "yellow")
    elif btnName == "colours":
        RGB = app.getListItems("colours")
        if len(RGB) > 0:
            RGB = RGB[0]
            app.setLabelBg("colBox", RGB)
            app.setEntry("colCode", RGB)
            loadRGB(RGB)
    elif btnName == "Clear":
        app.clearListBox("colours")


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

def loadRGB(RGB):
    # split the RGB string, then convert to ints
    R = int(RGB[1:3], 16)
    G = int(RGB[3:5], 16)
    B = int(RGB[5:7], 16)

    app.setScale("redScale", R)
    app.setScale("greScale", G)
    app.setScale("bluScale", B)

# funciton to update widgets
def updateRGB(name):
    # this stops the changes in slider/spin from constantly calling each other
    global alreadyDone
    if alreadyDone:
        alreadyDone = False
        return
    else:
        alreadyDone = True

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

app = gui("RGB COlours")
app.setBg("#B8DEE2")
app.setGuiPadding(5,5)
app.setFont(18)

# frame to contain sliders
app.startLabelFrame("Colour Codes")
app.setSticky("news")
app.setPadding(5,5)

app.addLabel("redLab", "Red (R):", 0, 0)
app.addLabel("greLab", "Green (G):", 1, 0)
app.addLabel("bluLab", "Blue (B):", 2, 0)

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
app.setPadding(5,5)
app.setSticky("news")
app.addEmptyLabel("colBox", colspan=3)
app.setLabelHeight("colBox", 5)
app.setLabelWidth("colBox", 25)
app.setLabelRelief("colBox", "ridge")
app.addHorizontalSeparator(colspan=3)
app.addLabel("colCodeLab", "HEX Colour Code:", column=0)
app.addEntry("colCode", row=2, column=1)
app.addButton("Reset", btnPress, row=2, column=2)
app.disableEntry("colCode")
app.stopLabelFrame()

app.startLabelFrame("Colour History")
app.setPadding(5,5)
app.setSticky("EW")
app.addListBox("colours", [])
app.setListBoxRows("colours", 4)
app.setListBoxFunction("colours", btnPress)
app.addButtons(["Log", "Clear"], btnPress)
app.stopLabelFrame()

app.go()
