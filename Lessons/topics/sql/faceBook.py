from rwbatools import gui
import sqlite3
con = sqlite3.connect('facebook.db')


def press(btn):
      print(btn)

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

win.go()
