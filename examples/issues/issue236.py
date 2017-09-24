import sys
sys.path.append("../../")

def press(btn):
    print(app.topLevel.geometry())
    print(app.topLevel.attributes('-fullscreen'))

def show(btn=None):
    print("show", btn)


from appJar import gui
with gui() as app:
    app.addButton("Press", press)
    app.topLevel.bind('<Configure>', show)

