# import the library
from appJar import gui

def loadDetails(theFile="myFile.txt"):
      with open ( theFile, "r") as inFile :
            data = inFile.read ( ) # read the file into data
            return data.splitlines ( ) # make a list of lines

def writeDetails(user, pwd, theFile="myFile.txt"):
      with open ( theFile, "a" ) as outFile :
            outFile.write ( user+ "," + pwd + "\n" )

def checkPass(name, pwd):
      for a in myList:
            n = a.split(",")
            if n[0] == name and n[1] == pwd:
                  return True
      return False

def checkUser(name):
      for a in myList:
            n = a.split(",")
            print("Comparing:", n[0], "with:", name)
            if n[0] == name:
                  return True
      return False

def press(btn):
      
      global myList
      print(btn, "pressed")

      if btn == "Add":
            username = win.getEntry("Username")
            password = win.getEntry("Password")
            if checkUser(username):
                  win.errorBox("Duplicate", "Duplicate username, please try a different name")
            else:
                  writeDetails(username, password)
                  myList = loadDetails()
                  win.infoBox("Update", "User added")

      elif btn == "Reset":
            win.setStatus("Reset")
            win.clearEntry("Username")
            win.clearEntry("Password")
            win.setFocus("Username")

      elif btn == "Submit" or btn == "Password":
            username = win.getEntry("Username")
            password = win.getEntry("Password")

            print (username, " : ", password)

            if checkPass(username, password):
                  win.setStatus("Success")
                  win.infoBox("Success", "Valid password")
            else:
                  win.setStatus("Error")
                  win.errorBox("Error", "Invalid password")

# create the list of users
myList = loadDetails()

# create the GUI
win = gui("Login")

win.setBg("Green")
win.setFont(16)

win.addLabel("title", "Login Window")
win.setLabelFg("title","white")

win.addLabelEntry("Username")
win.setLabelFg("Username","white")

win.addSecretLabelEntry("Password")
win.setLabelFg("Password","white")

win.addButtons(["Submit", "Reset", "Add"], press)
win.setEntryFunc ( "Password", press )
win.addStatus()

win.go()
