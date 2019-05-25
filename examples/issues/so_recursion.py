import sys
sys.path.append("../../")

from appJar import gui

def loginButton(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        login(usr,pwd)

def login(usr,pwd):

    if usr == "1" and pwd == "1":
        app.hide()
        print ("Success go to next gui")
        app.showSubWindow('Custom IRC')
    else:
        addLoginErrorMessage()

def addLoginErrorMessage():
    app.opengui("Custon IRC Login")
    app.addLabel("ErrorLabel", "Wrong username or password.")

def chatGUI(usr):
    app = chatGUI("Custom IRC")
    ##app.addLabelOptionBox("Select Server", ["127.0.0.1"], 0, 0, 1)
    ##app.addListBox("chatBox",1, 0, 3, 2)
    ##app.addEntry("chatInput", 3, 0, 3)
    app.go()

app = gui("Custom IRC Login")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit", "Cancel"], loginButton)

#app.startSubWindow("Custom IRC")
#app.addLabel('aaa')
#app.stopSubWindow()
app.go()
