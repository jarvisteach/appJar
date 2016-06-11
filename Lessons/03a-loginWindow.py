# import the library
from appJar import gui

def press(btn):
      if btn == "Cancel":
            win.stop()
      elif btn == "Reset":
            win.setStatus("Reset")
            win.clearEntry("Username")
            win.clearEntry("Password")
            win.setFocus("Username")
      # the Password Entry can also call submit
      elif btn == "Submit" or btn == "Password":
            username = win.getEntry("Username")
            password = win.getEntry("Password")

            print (username, " : ", password)

            if username == "rjarvis" and password == "password":
                  win.setStatus("Success")
                  win.infoBox("Success", "Valid password")
            else:
                  win.setStatus("Error")
                  win.errorBox("Error", "Invalid password")

win = gui("Login")

win.setBg("Green")
win.setFont(16)

win.addLabel("title", "Login Window")
win.setLabelFg("title","white")

win.addLabelEntry("Username")
win.setLabelFg("Username","white")

win.addSecretLabelEntry("Password")
win.setLabelFg("Password","white")

win.addButtons(["Submit", "Reset", "Cancel"], press)
win.setEntryFunc ( "Password", press )
win.addStatus()

win.go()
