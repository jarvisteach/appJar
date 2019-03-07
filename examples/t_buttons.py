import sys
sys.path.append("../")
from appJar import gui

def press(btn):                 # the title of the button will be received as a parameter
    print(btn)

app=gui()
app.setFont(20)
app.addButton("One", press)     # 3 buttons, each calling the same function
app.addButton("Two", press)
app.addButton("Three", press)
app.go()
