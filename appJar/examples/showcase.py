import sys
import time
sys.path.append("../../")
from appJar import gui

# global variable to remember what's being dragged
dragged = "dd"
# some useful colours
colours = ["red", "orange", "green", "pink", "purple"]

# calculator function
def calculator(key):
    app.label("calculator", app.label("calculator") + key)

# function to login the user
def login(btn):
    if btn == "Clear":
        app.entry("username", "")
        app.setEntryFocus("username")
        app.entry("password", "")
    elif btn == "Submit":
        app.infoBox("Success", "Access granted")
        app.setTabbedFrameDisableAllTabs("Tabs", False)
        app.setToolbarEnabled()
        app.setToolbarPinned()
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
    val = app.meter("Meter1")[0]*100 + 1
    app.meter("Meter1", (app.meter("Meter1")[0]*100 + 1)%100)
    app.meter("Meter2", (app.meter("Meter2")[0]*100 - 1)%100)

# functions to handle drag'n drop

# call this to reset the drag'n drop label
def resetDD(btn):
    app.label("dd", "Drop here", bg="blue")

# called when a drag starts - remember the label being dragged
def drag(lbl):
    global dragged
    dragged = lbl

# called when a drag stops - check the label being dropped on
def drop(lbl):
    if lbl == "dd":
        app.label("dd", app.getLabel(dragged), bg=colours[int(dragged[2])])

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
            app.setSize("fullscreen")
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN-EXIT")
    elif btn == "CALENDAR": app.showSubWindow("DatePicker")
    elif btn == "ADDRESS-BOOK": app.showSubWindow("AddressBook")
    elif btn == "MAP": app.showSubWindow("Maps")
    elif btn == "ACCESS": app.showAccess()

# called when scale/meters are changed
def scale(name):
    if name == "TransparencySpin":
        trans = int(app.getSpinBox(name))
        app.setTransparency(trans)
        app.setScale("TransparencyScale", trans, callFunction=False)
    elif name == "TransparencyScale":
        trans = app.getScale(name)
        app.setTransparency(trans)
        app.setSpinBox("TransparencySpin", trans, callFunction=False)
    elif name == "FontScale": app.setFont(size=app.getScale(name))

def move(direction):
    if direction == ">":
        for item in app.getListBox("Animals"):
            app.addListItem("Sports",item)
            app.removeListItem("Animals", item)
    elif direction == "<":
        for item in app.getListBox("Sports"):
            app.addListItem("Animals",item)
            app.removeListItem("Sports", item)
    elif direction == "<<":
        app.addListItems("Animals", app.getAllListItems("Sports"))
        app.clearListBox("Sports")
    elif direction == ">>":
        app.addListItems("Sports", app.getAllListItems("Animals"))
        app.clearListBox("Animals")

def add(entry):
    if entry == "animalsEntry":
        app.addListItem("Animals", app.getEntry("animalsEntry"))
        app.clearEntry("animalsEntry")
    elif entry == "sportsEntry":
        app.addListItem("Sports", app.getEntry("sportsEntry"))
        app.clearEntry("sportsEntry")

# funciton to change the selected tab - called from menu
def changeTab(tabName):
    print("Changing to: ", tabName)
    app.setTabbedFrameSelectedTab("Tabs", tabName)
    print("done")

# function to get a help message on log-in page
def helpMe(nbtn):
    app.infoBox("Login Help", "Any username/password will do...")

# function to update status bar with the time
def showTime():
    app.setStatusbar(time.strftime("%X"))

###########################
## GUI Code starts here ##
###########################

with gui("ShowCase") as app:
    app.showSplash("appJar Showcase")

    # add a simple toolbar
    app.addToolbar(["EXIT", "LOGOUT", "FILL", "ACCESS", "PIE-CHART", "CALENDAR", "ADDRESS-BOOK", "MAP", "FULL-SCREEN"], toolbar, findIcon=True)

    #app.createMenu("Test")
    app.addMenuPreferences(toolbar)
    #app.addMenuItem("APPMENU", "About", toolbar)
    app.addMenuItem("Test", "EXIT", toolbar, shortcut="Option-Control-Shift-Alt-Command-B", underline=2)
    app.addMenuList("Tabs", ["Login", "Lists", "Properties", "Meters", "Drag'nDrop", "Calculator", "Panes", "Labels"], changeTab)
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
    app.addMenuItem("WIN_SYS", "About", app.appJarAbout)

    app.addMenuList("Help", ["Help", "About"], [app.appJarHelp, app.appJarAbout])

    try:
        app.setMenuIcon("Test", "EXIT", "EXIT", "left")
        app.setMenuIcon("Test", "LOGOUT", "LOGOUT", "right")
        app.setMenuIcon("Test", "FILL", "FILL", "none")
    except:
        pass

    app.disableMenuItem("List Items", "aaa")
    app.disableMenubar()

    # add a statusbar to show the time
    app.addStatusbar(side="RIGHT")
    app.registerEvent(showTime)
    app.stopFunction = logoutFunction

    with app.tabbedFrame("Tabs"):
        with app.tab("Login", bg="slategrey", sticky="new"):
            with app.labelFrame("Login Form"):
                app.label("username", "Username", sticky="ew")
                app.entry("username", pos=('p', 1), focus=True)
                app.label("password", "Password")
                app.entry("password", pos=('p', 1), secret=True)
                app.buttons(["Submit", "Clear"], login, colspan=2)
                app.link("help", helpMe, column=1, sticky="e")

        with app.tab("Lists", sticky="ew", expand="all", bg="orangered"):
            app.listbox("Animals", ["Zebra", "Sheep", "Lion", "Giraffe", "Snake", "Fish"], pos=(0, 0, 1, 4), bg="orange")
            app.listbox("Sports", ["Football", "Rugby", "Cricket", "Golf", "Cycling", "Netball", "Rounders"], pos=(0, 2, 1, 4), bg="orange")
            app.button("<", move, pos=(0, 1))
            app.button("<<", move, pos=(1, 1))
            app.button(">>", move, pos=(2, 1))
            app.button(">", move, pos=(3, 1))
            app.entry("animalsEntry", pos=(4, 0), bg="lightgrey", submit=add, default="-- add an item --")
            app.entry("sportsEntry", pos=(4, 2), bg="lightgrey", submit=add, default="-- add an item --")

        with app.tab("Properties"):
            with app.panedFrame("left"):
                app.label("t", "Transparency")
                app.label("t2", "Transparency")
                app.label("f","Font")

                with app.panedFrame("right"):
                    app.slider("TransparencyScale", 100, change=scale, interval=25)
                    app.spin("TransparencySpin", value=0, endValue=100, item='100', change=scale)
                    app.slider("FontScale", 12, show=True, change=scale, range=(6,40))

        with app.tab("Meters"):
            app.meter("Meter1", fill="Yellow")
            app.meter("Meter2", fill="green")
            app.registerEvent(meters)

        with app.tab("Drag'nDrop"):
            with app.labelFrame("dnd", hideTitle=True, sticky="news", inPadding=(20,20)):
                for i in range(5):
                    l = "DD"+str(i)
                    app.label(l, l, pos=(0, i), tip=colours[i], bg=colours[i], fg="white", drag=[drag, drop])

                app.separator(1, 0, 5)
                app.label("dd", "DROP HERE", pos=(2, 0, 5), bg="blue", fg="white", tip="Drag any of the colours here to make a change...")

            with app.labelFrame("Reset", sticky="news"):
                app.button("RESET", resetDD, 0,0)
                app.label("RESET", "RESET", 0,1, bg="grey", submit=resetDD)
                app.link("RESET", resetDD, 0,2)

        with app.tab("Calculator", inPadding = (5,5)):
            app.label("calculator", "", bg="grey", relief="sunken", anchor="e")
            buttons=[["1", "2", "3", "C"], ["4", "5", "6", "+"], ["7", "8", "9", "-"], ["0", "*", "/", "="]]
            app.buttons(buttons, calculator, width=3, height=3)

        with app.tab("Panes"):
            with app.panedFrame("a", sticky = "news"):
                app.label("Edit Pane", relief="groove")
                app.text("t1")
                with app.panedFrameVertical("b"): app.label("Pane 2")
                with app.panedFrame("c"): app.label("Pane 3")
                with app.panedFrame("d"): app.label("Pane 4")

        with app.tab("Labels", sticky = "news"):
            app.label("Yellow", rowspan=4, bg="yellow")
            app.label("Red", pos=('p', 1, 2), bg="red")
            app.label("Green", pos=('n', 1), bg="green")
            app.label("Blue", pos=('p', 2, 1, 2), bg="blue")
            app.label("Orange", pos=('n', 1), bg="orange")
            app.label("Pink", pos=('n', 1, 2), bg="pink")
            app.label("Purple", colspan=3, bg="purple")

    with app.subWindow("Statistics", transient=True, bg="yellow", sticky="news", size="300x330"):
        values={"German":20, "French":10, "English":60, "Dutch": 5, "Belgium":3, "Danish":2}
        app.addPieChart("Nationality", values)
        app.option("Nationality", values.keys(), label=True)
        app.entry("Percentage", kind="numeric")
        def changePie(btn):
            app.setPieChart("Nationality", app.getOptionBox("Nationality"), app.getEntry("Percentage"))
        app.button("Update", changePie)

    with app.subWindow("Maps", sticky="news"):
        app.addGoogleMap("g1")

    with app.subWindow("DatePicker", transient=True, modal=True):
        app.date("dp", "today")
        def getDate(btn=None):
            print(app.getDatePicker("dp"))
            return True
        app.addNamedButton("DONE", "DatePicker", app.hideSubWindow)
        app.setStopFunction(getDate)

    with app.subWindow("AddressBook", transient=True):
        app.sticky = 'news'
        app.stretch = 'both'
        app.size = (300,350)
        app.location = (600,50)
        with app.pagedWindow("AddressBook"):
            with app.page(): app.label("PP1")
            with app.page(): app.label("PP2")
            with app.page(): app.label("PP3")

    # start logged out
    logout()
