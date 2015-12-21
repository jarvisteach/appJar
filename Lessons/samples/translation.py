# import the library
from rwbatools import gui
win = gui("Translate")

trans = {"lol":"laugh out loud"}
canAdd = False

def press(name):
      word = win.getEntry("Word")
      if word in trans:
            ans = trans[word]
      else:
            ans = "Unknown..."

      win.setLabel("l1", ans)

def newV(name):
      global trans
      trans[win.getEntry("nw")] = win.getEntry("nv")

def checkAdd(name):
      if canAdd: disableAdd()
      else: enableAdd()


def disableAdd():
      global canAdd
      canAdd = False
      win.disableEntry("nw")
      win.disableEntry("nv")
      win.disableButton("Add")
      win.setFocus("Word")

def enableAdd():
      global canAdd
      canAdd = True
      win.enableEntry("nw")
      win.enableEntry("nv")
      win.enableButton("Add")
      win.setFocus("nw")

win.addEntry("Word")
win.setFocus("Word")
win.setEntryCommand("Word", press)
win.addButton("Translate", press)
win.setButtonCursor("Translate", "hand1")
win.addEmptyLabel("l1")
win.addCheckBox("Add Translation")
win.setCbCommand("Add Translation", checkAdd)
win.addEntry("nw")
win.addEntry("nv")
win.addButton("Add", newV)
disableAdd()
win.go()
