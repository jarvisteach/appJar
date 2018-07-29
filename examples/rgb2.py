import sys
sys.path.append("../")
from appJar import gui

# funciton to handle the button presses
def btnPress(btnName):
    if btnName == "Reset":
        app.spin("redSpin", 0)
        app.spin("greSpin", 0)
        app.spin("bluSpin", 0)
        app.slider("redScale", value=0)
        app.slider("greScale", value=0)
        app.slider("bluScale", value=0)
    elif btnName == "Log":
        RGB = getRGB()
        if RGB in app.listbox("colours"):
            app.selectListItem("colours", RGB)
        else:
            app.addListItem("colours", RGB)
            app.setListItemBg("colours", RGB, RGB)
            app.setListItemFg("colours", RGB, "yellow")
    elif btnName == "colours":
        RGB = app.listbox("colours")
        if len(RGB) > 0:
            RGB = RGB[0]
            app.setLabelBg("colBox", RGB)
            app.setEntry("colCode", RGB)
            loadRGB(RGB)
    elif btnName == "Clear":
        app.clearListBox("colours")


# function to convert the scale values to an RGB hex code
def getRGB():
    R = app.scale("redScale")
    G = app.scale("greScale")
    B = app.scale("bluScale")

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

    app.scale("redScale", R)
    app.scale("greScale", G)
    app.scale("bluScale", B)

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
        app.setSpinBox(colour+"Spin", value, callFunction = False)
    elif widg == "Spin":
        value = app.getSpinBox(name)
        app.setScale(colour+"Scale", value, callFunction = False)

    # update the label
    app.label("colBox", bg=RGB)
    app.entry("colCode", RGB)

with gui("RGB COlours", bg="#BBDEE2", font=18, guiPadding='5,5') as app:

    # frame to contain sliders
    with app.labelFrame("Colour Codes", sticky='news', padding='5,5'):
        app.label("redLab", "Red (R):", 0, 0, align='w')
        app.label("greLab", "Green (G):", 1, 0, align='w')
        app.label("bluLab", "Blue (B):", 2, 0, align='w')

        app.spin("redSpin", 0, 0, 1, endValue=255, width=4, change=updateRGB)
        app.spin("greSpin", 0, 1, 1, endValue=255, width=4, change=updateRGB)
        app.spin("bluSpin", 0, 2, 1, endValue=255, width=4, change=updateRGB)

        app.slider("redScale", 0, 2, change=updateRGB, range=[0,255])
        app.slider("greScale", 1, 2, change=updateRGB, range=[0,255])
        app.slider("bluScale", 2, 2, change=updateRGB, range=[0,255])

    # frame to hold coloured label
    with app.labelFrame("Colour Preview", padding='5,5', sticky='news'):
        app.label("colBox", '', colspan=3, height=5, width=25, relief='ridge')
        app.separator(colspan=3)
        app.label("colCodeLab", "HEX Colour Code:", column=0)
        app.entry("colCode", row=2, column=1, state='disabled')
        app.button("Reset", btnPress, row=2, column=2)

    with app.labelFrame("Colour History", padding='5,5', sticky='EW'):
        app.listbox("colours", [], rows=4, change=btnPress)
        app.buttons(["Log", "Clear"], btnPress)
