import sys
sys.path.append("../../")

from appJar import gui


def press(button):
    if button == "Cancel":
        app.stop()


def startGui():
    app.addLabel("title", "Testing")
    app.setFg("red", override=True) # should change text in option box to red

    app.addLabelOptionBox("Test Steps", ["Apple", "Orange", "Pear", "kiwi",
                                         "Dogs", "Cats", "Fish", "Hamsters"])
    app.addLabelEntry("MAC Address")

    app.addButtons(["Cancel"], press)
    app.setButtonFg("Cancel", "black") # should change button text to black
    app.setButtonBg("Cancel", "gray")
    app.go()

if __name__ == '__main__':
    app = gui("Testing")
    startGui()
