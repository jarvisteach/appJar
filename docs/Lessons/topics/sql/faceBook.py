import sys
sys.path.append("../../../../")
from appJar import gui

from rwbatools import sql
con = sql('facebook.db')
maxLen = con.getNumRows("friends")
data = con.getData("friends")
pos = 1
print(data)

def updateScreen():
      name = data[pos][1]
      gender = data[pos][2]
      dob = data[pos][3]

      win.setLabel("name", name)
      win.setLabel("gender", gender)
      win.setLabel("dob", dob)

def press(btn):
      print(btn)
      print(data)
      print(pos)
      global pos
      if btn == "Back" and pos > 1:
            pos -= 1
            updateScreen()

      elif btn == "Forward" and pos < maxLen:
            pos += 1
            updateScreen()

win = gui("FaceBook")

win.setBg("Blue")
win.setFont(16)

win.addButton("Back", press, 0, 0, 0)
win.addLabel("lbl", "FaceBook", 0, 1, 0)
win.addButton("Forward", press, 0, 2, 0)

win.addLabel("lb2", "Name",1,0,1)
win.addLabel("name", "xxx",1,1,2)

win.addLabel("lb3", "Gender",2,0,1)
win.addLabel("gender", "xxx",2,1,2)

win.addLabel("lb4", "DoB",3,0,1)
win.addLabel("dob", "xxx",3,1,2)

updateScreen()

win.go()
