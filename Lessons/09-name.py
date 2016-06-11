from appJar import gui

def press(btn):

    if btn == "Exit":
        win.stop()

    elif btn == "Reset":
        win.clearEntry("Name")
        win.setLabel("Results", "")

    elif btn == "Get Info":
        name = win.getEntry("Name")
        nameLen = len(name)

        if nameLen == 0:
            win.errorBox("Error", "No name entered.")

        else:
            spacePos = name.find(" ")
            
            if spacePos == -1:
                win.errorBox("Error", "No space found")
            else:
                fName = name[0:spacePos]
                lName = name[spacePos+1:nameLen]

                message = "Your first name is " + fName + "\n"
                message += "Your last name is " + lName + "\n"
                message += "There are " + str(nameLen-1) + " characters in your name"

                win.setLabel("Results", message)

win = gui("Names")

win.setFont(16)
win.setBg("green")

win.addLabelEntry("Name")
win.addEmptyLabel("Results")
win.addButtons(["Get Info", "Reset", "Exit"], press)

win.setLabelWidth("Results", 35)
win.setLabelHeight("Results", 5)
win.setLabelRelief("Results", win.RAISED)

win.go()
