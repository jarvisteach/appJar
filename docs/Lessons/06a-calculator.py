# import library
from appJar import gui

# function to process button press
def press(btn):
    if btn == "Exit":
        win.stop()
    else:
        try:
            firstNum = int(win.getEntry("first"))
            secondNum = int(win.getEntry("second"))

            message =  "The results are as follows:\n\n"
            message += "Addition: " + str (firstNum + secondNum) + "\n"
            message += "Subtraction: " + str (firstNum - secondNum) + "\n"
            message += "Multiplication: " + str (firstNum * secondNum) + "\n"
            message += "Division: " + str (firstNum / secondNum) + "\n"

            if btn == "Result":
                win.setLabel("Result", message)
            elif btn == "MessageBox Result":
                win.infoBox("Result", message)
                    
        except ValueError as e:
            win.errorBox("Error", "Invalid number")
            win.setFocus ( "first" )

win = gui("Calculator")

# add 2 labels & buttons - this time specify row & column
win.addLabel ( "fn", "First Number", 0, 0 )
win.addEntry ( "first", 0, 1 )
win.addLabel ( "sn", "Second Number", 0, 2 )
win.addEntry ( "second", 0, 3 )
win.setFocus ( "first" )

# add the result label - specify row/column/colspan
win.addEmptyLabel("Result", 1, 0, 4)

# format the label
win.setLabelRelief("Result", win.GROOVE)
win.setLabelAlign("Result", win.NW)
win.setLabelHeight("Result", 8)

# add the buttons
win.addButtons(["Result", "MessageBox Result", "Exit"], press, 2, 0, 4)
# start the GUI
win.go()
