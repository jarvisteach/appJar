import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    val = app.popUp("a", "b", btn)
    print(val)
    app.label("title", bg="red")

def press2(btn):
    val = app.prompt("a", "b", btn)
    print(val)

def press3(btn):
    print(btn)

def fonts(btn):
    if btn == "BUT+": app.increaseButtonFont()
    elif btn == "BUT-": app.decreaseButtonFont()
    elif btn == "LAB+": app.increaseLabelFont()
    elif btn == "LAB-": app.decreaseLabelFont()
    elif btn == "ALL+": app.increaseFont()
    elif btn == "ALL-": app.decreaseFont()

with gui("Simple Demo") as app:
    app.setFont(size=16, family="Times", underline=True, slant="italic")
    app.setButtonFont(size=14, family="Verdana", underline=False, slant="roman")

    app.label("title", "TOOLTIP & MENU", bg="green", fg="blue", pos=(0, 0), tooltip="some info", menu=True, anchor="e")
    app.label("title2", "SUBMIT", bg="red", fg="white", pos=(0, 1), submit=press)
    app.label("title3", "CHANGE & OVER", bg="orange", fg="black", pos=(1,0), over=[press3, press3], change=press)
    app.label("title4", "DRAG & DROP", bg="pink", fg="yellow", pos=(1, 1), drop=True, drag=(press3, press3))
    app.label("title5", "FLASH", kind="flash", pos=(2, 0), bg="orange", drop=True, drag=press2)
    app.label("title6", "SELECTABLE", kind="selectable", pos=(2,1), bg="green", drop=True)
    app.message("mess1", pos=(None, 0, 2), drop=True, over=press3, bg="green", tooltip="message here")
    app.addButtons(["info", "error", "warning", "yesno", "question", "ok", "retry"], press, colspan=2)
    app.addButtons(["string", "integer", "float", "text", "number", "junk"], press2, colspan=2)

    app.addButtons(["BUT+", "BUT-", "LAB+", "LAB-", "ALL+", "ALL-"], fonts)
