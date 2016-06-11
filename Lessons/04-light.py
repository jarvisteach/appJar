# import the library
from appJar import gui

onimg = "resources/bulb_on.gif"
offimg = "resources/bulb_off.gif"

# function to handle button press
def press(btn):
    if btn == "Exit":
        win.stop()
    elif btn == "On":
        win.setImage("Light", onimg)
        win.disableButton("On")
        win.enableButton("Off")
    elif btn == "Off":
        win.disableButton("Off")
        win.enableButton("On")
        win.setImage("Light", offimg)

# create the window
win = gui("Lights!")

# add the image & buttons
win.addImage("Light", offimg)
win.addButtons(["On", "Off"], press)
win.disableButton("Off")
win.addButton("Exit", press )

# start the window
win.go()
