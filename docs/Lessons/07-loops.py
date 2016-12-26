from appJar import gui

# function to handle the button presses
def press(btn):
    # if quit button pressed - stop GUI
    if btn == "Quit":
        win.stop()
    # if clear button pressed - clear all entries
    elif btn == "Clear":
        win.clearEntry ( "Multiple" )
        win.clearListBox ( "list" )
    # else, if user pressed multiply button
    elif btn == "Multiply" or btn == "Multiple":
        # get the multiple value
        try:
            num = int ( win.getEntry ( "Multiple" ) )
        # show a dialog if an error
        except ValueError:
            win.errorBox ( "ValueError", "Invalid number." )
            win.clearEntry ( "Multiple" )
            return

        # now loop 10 times, and add items to the list...
        for loop in range(1, 11):
            line = str ( loop ) + "x" + str ( num ) + "=" + str ( loop * num )
            win.addListItem ( "list", line )

# create and configure the GUI
win = gui ( "Loops" )
win.setFont ( 16 )
win.setBg ( "yellow" )

win.addListBox ( "list" )
win.addLabelEntry ( "Multiple" )
win.setEntryWidth ( "Multiple", 5 )
win.setEntryFunc ( "Multiple", press )
win.setFocus ( "Multiple" )

win.addButton ( "Multiply", press )
win.addButtons ( [ "Clear", "Quit" ] , press )
win.go ( )
