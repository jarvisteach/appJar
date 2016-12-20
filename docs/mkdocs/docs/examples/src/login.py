from appJar import gui

# create the GUI & set a title
app = gui("Login Form")

def press(btnName):
    if btnName == "Cancel":
        app.stop()
        return

    if app.getEntry("userEnt") == "rjarvis":
        if app.getEntry("passEnt") == "abc":
            app.infoBox("Success", "Congratulations, you are logged in!")
        else:
            app.errorBox("Failed login", "Invalid password")
    else:
        app.errorBox("Failed login", "Invalid username")

# add labels & entries
# in the correct row & column
app.addLabel("userLab", "Username:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addLabel("passLab", "Password:", 1, 0)
app.addSecretEntry("passEnt", 1, 1)

# changed this line to call a function
app.addButtons( ["Submit", "Cancel"], press, colspan=2)

# add some enhancements
app.setFocus("userEnt")
app.enableEnter(press)

# start the GUI
app.go()


