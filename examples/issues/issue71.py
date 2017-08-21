import sys
sys.path.append("../../")

def press(btn):
    if btn == "PRESS":
#        app.playSound("notify.wav")
        print(app.translate("msg1"))
        app.okBox("OK", "EMPTY")
    elif btn == "PRESS2":
#        app.playSound("ringout.wav")
        print(app.translate("msg2", "the default"))
        app.okBox("OTHER", "STILL EMPTY")
    elif btn == "RENAME":
        app.renameMenu("MENU1", "NEW NAME")
        app.renameMenuItem("MENU1", "ITEM1", "Did it...")

from appJar import gui

app=gui()

app.addMenuList("MENU1", ["ITEM1", "ITEM2", "ITEM3", "ITEM4"], None)
app.addMenuList("MENU2", ["ITEM1", "ITEM2", "ITEM3", "ITEM4"], None)

app.setLogLevel("DEBUG")
#app.setSoundLocation("C:\Windows\Media")
app.addLabel("l1", "DEFAULT")
app.addLabel("l2", "DEFAULT")
app.addLabel("l3", "DEFAULT")
app.addButtons(["PRESS", "PRESS2", "RENAME"], press)
app.addButtons(["ENGLISH", "FRENCH"], app.changeLanguage)
app.go("ENGLISH")
