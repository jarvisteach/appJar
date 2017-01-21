import sys
sys.path.append("../../")
from appJar import gui

# global variable to remember what's being dragged
dragged = "dd"
# globals to remember the meter's values
meter1 = 0
meter2 = 100
# some useful colours
colours = ["red", "orange", "green", "pink", "purple"]

# calculator function
calcVal = 0
def calculator(key):
    global calcVal
    val = app.getLabel("calculator")
    app.setLabel("calculator", val + key)

# function to login the user
def login(btn):
    if btn == "Clear":
        app.clearEntry("username")
        app.clearEntry("password")
        app.setEntryFocus("username")
    elif btn == "Submit":
        app.infoBox("Success", "Access granted")
        app.setTabbedFrameDisableAllTabs("Tabs", False)
        app.setToolbarEnabled()
        app.setToolbarButtonDisabled("LOGOUT", False)
        app.enableMenubar()

# function to confirm logout
def logoutFunction():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit?")

# disable the tabs
def logout(btn = None):
    app.setTabbedFrameDisableAllTabs("Tabs")
    app.setTabbedFrameDisabledTab("Tabs", "Login", False)
    app.setTabbedFrameSelectedTab("Tabs", "Login")
    # disable toolbar
    app.setToolbarDisabled()
    app.setToolbarButtonEnabled("EXIT")
    app.disableMenubar()
    app.enableMenuItem("Test", "EXIT")

# function to update the meters
def meters():
    global meter1, meter2
    meter1=(meter1+1)%100
    meter2=(meter2-1)%100
    app.setMeter("Meter1", meter1)
    app.setMeter("Meter2", meter2)

# functions to handle drag'n drop

# call this to reset the drag'n drop label
def resetDD(btn):
    app.setLabel("dd", "Drop here")
    app.setLabelBg("dd", "blue")

# called when a drag starts - remember the label being dragged
def drag(lbl):
    global dragged
    dragged = lbl

# called when a drag stops - check the label being dropped on
def drop(lbl):
    if lbl == "dd": 
        app.setLabel("dd", app.getLabel(dragged))
        app.setLabelBg("dd", colours[int(dragged[2])])

# called by the toolbar buttons
def toolbar(btn):
    print(btn)
    if btn == "EXIT": app.stop()
    elif btn == "LOGOUT": logout()
    elif btn == "FILL": app.setTabBg("Tabs", app.getTabbedFrameSelectedTab("Tabs"), app.colourBox())
    elif btn == "PIE-CHART": app.showSubWindow("Statistics")
    elif btn == "FULL-SCREEN":
        if app.exitFullscreen():
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN")
        else:
            app.setGeometry("fullscreen")
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN-EXIT")
    elif btn == "CALENDAR": app.showSubWindow("DatePicker")
    elif btn == "ADDRESS-BOOK": app.showSubWindow("AddressBook")

# called when scale/meters are changed
def scale(name):
    if name == "TransparencySpin":
        trans = int(app.getSpinBox(name))
        app.setTransparency(trans)
        app.setScale("TransparencyScale", trans)
    elif name == "TransparencyScale":
        trans = app.getScale(name)
        app.setTransparency(trans)
        app.setSpinBox("TransparencySpin", trans)
    elif name == "FontScale": app.setFont(app.getScale(name))

def move(direction):
    if direction == ">":
        for item in app.getListItems("Animals"):
            app.addListItem("Sports",item) 
            app.removeListItem("Animals", item)
    elif direction == "<":
        for item in app.getListItems("Sports"):
            app.addListItem("Animals",item) 
            app.removeListItem("Sports", item)
    elif direction == "<<":
        app.addListItems("Animals", app.getAllListItems("Sports"))
        app.clearListBox("Sports")
    elif direction == ">>":
        app.addListItems("Sports", app.getAllListItems("Animals"))
        app.clearListBox("Animals")

def add(entry):
    if entry == "animalsEntry": app.addListItem("Animals", app.getEntry("animalsEntry"))
    elif entry == "sportsEntry": app.addListItem("Sports", app.getEntry("sportsEntry"))

# funciton to change the selected tab - called from menu
def changeTab(tabName):
    print("Changing to: ", tabName)
    app.setTabbedFrameSelectedTab("Tabs", tabName)
    print("done")

###########################
## GUI Code starts here ##
###########################

app = gui("ShowCase")
app.showSplash("appJar Showcase")

# add a simple toolbar
app.addToolbar(["EXIT", "LOGOUT", "FILL", "PIE-CHART", "CALENDAR", "ADDRESS-BOOK", "FULL-SCREEN"], toolbar, findIcon=True)
#app.createMenu("Test")
app.addMenuPreferences(toolbar)
#app.addMenuItem("APPMENU", "About", toolbar)
app.addMenuItem("Test", "EXIT", toolbar, shortcut="Option-Control-Shift-Alt-Command-B", underline=2)
app.addMenuList("Tabs", ["Login", "Lists", "Properties", "Meters", "Drag`nDrop", "Calculator", "Panes", "Labels"], changeTab)
app.addMenuItem("Test", "LOGOUT", toolbar, shortcut="Shift-Command-B", underline=3)
app.addMenuItem("Test", "FILL", toolbar, shortcut="Control-Shift-C", underline=1)
app.addSubMenu("Test", "Bobs")
app.addMenuItem("Bobs", "EXIT", toolbar)
app.addMenuItem("Bobs", "LOGOUT", toolbar)
app.addMenuItem("Bobs", "FILL", toolbar)
app.addMenu("PRESSME", toolbar)
app.addMenuCheckBox("Boxes", "Box 1", toolbar, "Command-1")
app.addMenuCheckBox("Boxes", "Box 2", toolbar, "Command-2")
app.addMenuCheckBox("Boxes", "Box 3", toolbar, "Command-3")
app.addMenuCheckBox("Boxes", "Box 4", toolbar, "Command-4")
app.addMenuCheckBox("Boxes", "Box 5", toolbar, "Command-5")

app.addMenuRadioButton("Radios", "r1", "Radio 6", toolbar, "Command-6", 7)
app.addMenuRadioButton("Radios", "r1", "Radio 7", toolbar, "Command-7", 7)
app.addMenuRadioButton("Radios", "r1", "Radio 8", toolbar, "Command-8", 7)
app.addMenuRadioButton("Radios", "r1", "Radio 9", toolbar, "Command-9", 7)
app.addMenuRadioButton("Radios", "r1", "Radio 0", toolbar, "Command-0", 7)

app.addMenuList("List Items", ["Item 1", "Item 2", "-", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7"], toolbar)
app.addMenuList("List Items", ["-", "aaa", "-", "bbb", "-", "ccc", "-", "ddd", "-"], toolbar)

#app.addMenuItem("2222List Items", "FILL", toolbar, shortcut="Control-Shift-C")

app.addMenuWindow()
app.addMenuHelp(toolbar)

app.setMenuIcon("Test", "EXIT", "EXIT", "left")
app.setMenuIcon("Test", "LOGOUT", "LOGOUT", "right")
app.setMenuIcon("Test", "FILL", "FILL", "none")

app.disableMenuItem("List Items", "aaa")
app.disableMenubar()

# start the tabbed frame
app.startTabbedFrame("Tabs")

#### LOGIN TAB
app.startTab("Login")
app.setBg("SlateGray")
app.setSticky("NEW")
app.startLabelFrame("Login Form")
app.setSticky("ew")
app.addLabel("username", "Username", 0, 0)
app.addEntry("username", 0, 1)
app.addLabel("password", "Password", 1, 0)
app.addSecretEntry("password", 1, 1)
app.addButtons(["Submit", "Clear"], login, 2, 0, 2)
app.setEntryFocus("username")
app.stopLabelFrame()
app.stopTab()

#### LISTS TAB
app.startTab("Lists")
app.setSticky("ew")
app.setExpand("all")
app.setBg("OrangeRed")

app.addListBox("Animals", ["Zebra", "Sheep", "Lion", "Giraffe", "Snake", "Fish"], 0, 0, 1, 4)
app.addListBox("Sports", ["Football", "Rugby", "Cricket", "Golf", "Cycling", "Netball", "Rounders"], 0, 2, 1, 4)

app.addButton("<", move, 0, 1)
app.addButton("<<", move, 1, 1)
app.addButton(">>", move, 2, 1)
app.addButton(">", move, 3, 1)

app.addEntry("animalsEntry", 4, 0)
app.addEntry("sportsEntry", 4, 2)

app.setListBoxBg("Animals", "Orange")
app.setListBoxBg("Sports", "Orange")
app.setEntryBg("animalsEntry", "LightGrey")
app.setEntryBg("sportsEntry", "LightGrey")
app.setEntryFunction("animalsEntry", add)
app.setEntryFunction("sportsEntry", add)
app.stopTab()

#### PROPERTIES TAB
app.startTab("Properties")
app.addLabel("t", "Transparency",0,0)
app.addScale("TransparencyScale",0,1)
app.setScale("TransparencyScale", 100)
app.setScaleFunction("TransparencyScale", scale)

app.addLabel("t2", "Transparency",1,0)
app.addSpinBoxRange("TransparencySpin", 1, 100, 1, 1)
app.setSpinBox("TransparencySpin", 100)
app.setSpinBoxFunction("TransparencySpin", scale)

app.addLabel("f","Font",2,0)
app.addScale("FontScale",2,1)
app.setScaleRange("FontScale", 6, 40, 12)
app.setScaleFunction("FontScale", scale)
app.stopTab()

#### METERS TAB
app.startTab("Meters")
app.addMeter("Meter1")
app.addMeter("Meter2")
app.setMeterFill("Meter1", "Yellow")
app.setMeterFill("Meter2", "Orange")
app.registerEvent(meters)
app.stopTab()

#### DRAG'N DROP TAB
app.startTab("Drag'nDrop")
app.startLabelFrame("")
app.setSticky("news")
app.setIPadX(20)
app.setIPadY(20)

for i in range(5):
    l = "DD"+str(i)
    app.addLabel(l, l, 0, i)
    app.setLabelBg(l, colours[i])
    app.setLabelFg(l, "white")
    app.setLabelDragFunction(l, [drag, drop])

app.addHorizontalSeparator(1, 0, 5)

app.addLabel("dd", "DROP HERE", 2, 0, 5)
app.setLabelTooltip("dd", "Drag any of the colours here to make a change...")
app.setLabelBg("dd", "blue")
app.setLabelFg("dd", "white")
app.stopLabelFrame()

app.startLabelFrame("Reset")
app.setSticky("news")
app.addButton("RESET", resetDD, 0,0)
app.addLabel("RESET", "RESET", 0,1)
app.setLabelBg("RESET", "grey")
app.setLabelFunction("RESET", resetDD)
app.addLink("RESET", resetDD, 0,2)
app.stopLabelFrame()
app.stopTab()

app.startTab("Calculator")
app.setIPadX(5)
app.setIPadY(5)
app.addEmptyLabel("calculator")
app.setLabelBg("calculator", "grey")
app.setLabelRelief("calculator", "sunken")
app.setLabelAlign("calculator", "e")
buttons=[["1", "2", "3", "C"],
                ["4", "5", "6", "+"],
                ["7", "8", "9", "-"],
                ["0", "*", "/", "="]]

app.addButtons(buttons, calculator)
app.setButtonWidths(buttons, 3)
app.setButtonHeights(buttons, 3)
app.stopTab()

app.startTab("Panes")

app.startPanedFrame("a")
app.setSticky("news")
app.addLabel("p1", "Edit Pane")
app.setLabelRelief("p1", "groove")
app.addTextArea("t1")

app.startPanedFrameVertical("b")
app.addLabel("p2", "Pane 2")

app.startPanedFrame("c")
app.addLabel("p3", "Pane 3")
app.stopPanedFrame()

app.startPanedFrame("d")
app.addLabel("p4", "Pane 4")
app.stopPanedFrame()

app.stopPanedFrame()
app.stopPanedFrame()

app.stopTab()

app.startTab("Labels")
app.setSticky("nesw")

app.addLabel("ll1", "Red", 0, 1, 4)
app.setLabelBg("ll1", "Red")
app.addLabel("ll2", "Yellow", 0, 0, 1, 4)
app.setLabelBg("ll2", "Yellow")
app.addLabel("ll3", "Green", 1, 1, 2)
app.setLabelBg("ll3", "Green")
app.addLabel("ll4", "Blue", 1, 3, 1, 2)
app.setLabelBg("ll4", "Blue")
app.addLabel("ll5", "Orange", 2, 1, 2)
app.setLabelBg("ll5", "Orange")
app.addLabel("ll6", "Pink", 3, 1, 4)
app.setLabelBg("ll6", "Pink")
app.addLabel("ll7", "Purple", 4, 0, 4)
app.setLabelBg("ll7", "Purple")

app.stopTab()

# end the tabbed interface
app.stopTabbedFrame()

# set up the sub window - by default it's hidden
app.startSubWindow("Statistics")
#app.setBg("yellow")
app.setSticky("news")
app.setGeometry("300x330")
values={"German":20, "French":10, "English":60, "Dutch": 5, "Belgium":3, "Danish":2}
app.addPieChart("Nationality", values)
app.addLabelOptionBox("Nationality", values.keys())
app.addNumericEntry("Percentage")
def changePie(btn):
    app.setPieChart("Nationality", app.getOptionBox("Nationality"), app.getEntry("Percentage"))
app.addButton("Update", changePie)
app.stopSubWindow()

# date picker
app.startSubWindow("DatePicker")
app.addDatePicker("dp")
app.setDatePicker("dp")
def getDate(btn=None):
    print(app.getDatePicker("dp"))
    return True
app.addNamedButton("DONE", "DatePicker", app.hideSubWindow)
app.setStopFunction(getDate)
app.stopSubWindow()

# paged window
app.startSubWindow("AddressBook")
app.startPagedWindow("AddressBook")
app.startPage("Page 1")
app.addLabel("PP1", "PP1")
app.stopPage()
app.stopPagedWindow()
app.stopSubWindow()

# start the GUI
logout()
app.setStopFunction(logoutFunction)
app.go()
