import sys
sys.path.append("../../")

def press(btn):
    print(app.topLevel.geometry())
    print(app.topLevel.attributes('-fullscreen'))

def show(btn=None):
    print("show", btn)

def setts(btn):
    if btn == "LOAD":
        print(app.getSetting("aa"))
    elif btn == "SAVE":
        app.setSetting("aa", app.textBox())


from appJar import gui
with gui(useSettings=True) as app:
    app.addButton("Press", press)
    app.topLevel.bind('<Configure>', show)
    app.addButtons(["LOAD", "SAVE"], setts)

