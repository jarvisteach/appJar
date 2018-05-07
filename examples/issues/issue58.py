import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "TEXT":
        app.textBox(btn, btn)
    elif btn == "NUMBER":
        app.numberBox(btn, btn)
    elif btn == "OK":
        app.okBox(btn, btn)

with gui("POPUPS") as app:
    app.buttons(["TEXT", "NUMBER", "OK"], press)
