from appJar import gui
#####################################
## MAIN - for testing
#####################################
if __name__ == "__main__":
    progress = 0
    main = True
    meter = True
    def a(btn): print("a")
    def b(btn): print("b")
    def tb_press(name):
        global main, meter
        win.setStatus("TB Press:"+name)
        try:
              if name == "Save": win.setStatus(win.saveBox())
              elif name == "Open": win.setStatus(win.openBox())
              elif name == "Dir": win.setStatus(win.directoryBox())
              elif name == "Close": win.stop()
              elif name == "Colour":
                    col = win.colourBox()
                    if col is not None:
                        win.setStatus(col)
                        win.setBg(col)
              elif name == "Resizable": win.setResizable(not win.getResizable())
              elif name == "RBCheck":
                    win.setStatus(win.getRadioButton("Test") + str(win.getCheckBox("Click Me")))
              elif name == "SetRB":
                    win.setStatus(win.getEntry("RB"))
                    win.setRadioButton("Test", win.getEntry("RB"))
              elif name == "IncreaseB": win.increaseButtonFont()
              elif name == "DecreaseB": win.decreaseButtonFont()
              elif name == "IncreaseL": win.increaseLabelFont()
              elif name == "DecreaseL": win.decreaseLabelFont()
              elif name == "GetList": win.infoBox("List", win.getListItems("Bits"))
              elif name == "H-Widget":
                    name = win.textBox("Hide Widget", "Enter widget name:")
                    win.hideWidget(getWidget(), name)
              elif name == "S-Widget":
                    name = win.textBox("Show Widget", "Enter widget name:")
                    win.showWidget(getWidget(), name)
              elif name == "R-Widget":
                    name = win.textBox("Remove Widget", "Enter widget name:")
                    win.removeWidget(getWidget(), name)
              elif name == "Sticky":
                    name = win.textBox("Sticky Widget", "Enter widget name:")
                    pos = win.getOptionBox("Option")
                    win.configureWidget(getWidget(), name, 'sticky', pos)
                    #win.setEntrySticky(name, pos)
              elif name == "FullScreen": win.setGeom("fullscreen")
              elif name == "Submit":
                    if win.retryBox("Submit", "Are you sure?"):
                          win.setStatus ( str(win.getScale("Scale")) )
                    win.removeAllWidgets()
              elif name == "Clear":
                    if win.yesNoBox("Clear", "Are you sure?"):
                          win.setCheckBox("Click Me", False)
                          win.clearAllEntries()
                          win.setFocus("Name")
                    win.removeScale("Scale")
              elif name == "Scale":
                    win.setStatus("Scale: " + str(win.getScale("Scale")))
                    win.setTransparency(win.getScale("Scale")/100)
              elif name == "Test":
                    win.setStatus("RB: " + win.getRadioButton("Test"))
              elif name == "spins1":
                    win.setStatus("SPIN: " + win.getSpinBox("spins1"))
              elif name == "Click Me":
                    win.setStatus("CLICK"+ str(win.getCheckBox("Click Me")))
              elif name == "stop-start":
                    meter = not meter

        except Exception as e:
              win.errorBox("Exception", e)

    def getWidget():
        kind = win.getOptionBox("Widgets")
        if kind == "WINDOW": return 0
        elif kind == "LABEL": return 1
        elif kind == "ENTRY": return 2
        elif kind == "BUTTON": return 3
        elif kind == "CB": return 4
        elif kind == "SCALE": return 5
        elif kind == "RB": return 6
        elif kind == "LB": return 7
        elif kind == "MESSAGE": return 8
        elif kind == "SPIN": return 9
        elif kind == "OPTION": return 10
        elif kind == "TEXTAREA": return 11
        elif kind == "LINK": return 12
        elif kind == "METER": return 13
        else: return 0

    def widgetChanged():
        print("HERE")


    def meter():
        global progress
        if meter:
              progress += .1
              win.setMeter("Meter", progress)
              print("ping: ", progress)
              if progress >1: progress = 0

    print ( "Making GUI" )
    win = gui("Details")
    #win.setExpand("all")
    #win.setSticky(False)
#      win.addEntry("Empty")
#      win.addLabelEntry("Name")
#      win.setLabelBg("Name", "red")
#      win.setLabelFg("Name", "yellow")
    #win.setLabelWidth("Name", "40")
    #win.setLabelHeight("Name", "20")
#      win.disableEntry("Name")
#      win.setFocus("Name")
#      win.addLabelEntry("Age")
#      win.addLabelEntry("Gender")
#      win.addButtons(["Submit","Clear", "Resizable"], tb_press)
#      win.setButtonBg("Resizable", "red")
#      win.setButtonFg("Resizable", "yellow")
#      win.setButtonWidth("Resizable", "40")
#      win.setButtonHeight("Resizable", "30")
#      win.setButtonState("Resizable", "disabled")
    win.addButtons(["IncreaseB", "DecreaseB"], tb_press)
    win.addButtons(["IncreaseL", "DecreaseL"], tb_press)
    win.addButtons(["a", "b"], [a,b])
    win.addLabels(["a", "b", "c", "d", "e"])
    win.addCheckBox("Click Me")
    win.setCbCommand("Click Me", tb_press)
    win.addButton("RBCheck", tb_press)
    win.addScale("Scale")
    win.orientScaleHor("Scale", True)
    win.setScaleCommand("Scale", tb_press)
    win.setScaleRange("Scale",0, 100, 100)
    #win.addImage("8ball.gif", win.getNextRow(), 0, 2)
    win.startLabelFrame("Radios")
    win.addRadioButton("Test", "Oneeeeeeeeeeeeeeeeeeeee")
    #win.addRadioButton("Test", "Four")
    win.setRbAlign("Test", win.SE)
    win.setRbCommand("Test", tb_press)
    win.addEntry("RB")
    win.setEntryFg("RB", "yellow")
    win.setEntryBg("RB", "blue")
    win.addButtons(["SetRB", "GetList"], tb_press)
    #win.addListBox("Bits", [1,2,3,4,5])
    #win.setListSingle("Bits", False)
    #win.setLbBg("Bits", "green")
    #win.setLbFg("Bits", "pink")
    #win.setLbState("Bits", "disabled")
    win.addOptionBox("opt",[7,2,3,4,5])
    win.setOptionBoxCommand("opt", tb_press)
    win.addLabelOptionBox("Option",["left", "right", "both"])
    win.addLabelOptionBox("opt2",["a","b","c"])
    win.startLabelFrame('spins', sticky="ew")
    win.addSpinBox("spins1", (3,6,9,1,2,4))
    win.setSpinBoxPos("spins1", 3)
    win.addLabelSpinBoxRange("spins2", 1, 10)
    win.addLabelSpinBoxRange("superSpinsAre", 1, 10)
    win.setSpinBoxCommand("spins1", tb_press)
    win.setSpinBox("superSpinsAre", 4)
    win.stopLabelFrame()
    win.addLabelOptionBox("Widgets",[ "WINDOW", "LABEL", "ENTRY", "BUTTON", "CB", "SCALE", "RB", "LB", "MESSAGE", "SPIN", "OPTION", "TEXTAREA", "LINK", "METER"])
    win.addMeter("Meter")
    win.setPollTime(2000)
    win.registerEvent(meter)
    win.addWebLink("link", "http://www.google.com")
    win.addLink("stop-start", tb_press)
    win.addEmptyMessage("fred2")
    win.addEmptyLabel("fff")
    win.setLabelBg("fff", "pink")
    win.setMessageBg("fred2", "yellow")
    #win.addMessage("fred", "Help somebody zsdf asdf asdf asdgfasdgasdfg asdgfasdfasdf asdfasdf . asdfasdf ")
    #win.setMessageBg("fred", "Green")
    #win.setMessageWidth("fred", 100)

    win.addToolbar(["H-Widget", "S-Widget", "R-Widget", "Sticky", "Download", "Open", "Close", "Colour", "FullScreen"], tb_press)
    win.addStatus("Status")
    win.setStatusBg("green")
    win.setStatusFg("orange")
    win.addMenuList("Fonts", ["IncreaseB", "DecreaseB", "IncreaseL", "DecreaseL"], tb_press)
    win.addMenu("Close", tb_press)
    win.addMenu("ThisOne", tb_press)
    #win.setIcon("/Users/jarvismail/Downloads/PYLIB/icons/default/left.png")
    win.go()
    print ("Done making GUI" )
