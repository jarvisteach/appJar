import sys
sys.path.append("../../")

from appJar import gui

def externalDrop(data):
    print("Data dropped:", data)

def press():
    app.showSubWindow('sub')

with gui("External dnd Demo") as app:
    with app.frame('f1'):
        app.font = 20
        app.bg = "SlateGrey"
        app.fg = "yellow"
        app.label("dropLab", "Drop Here", drop=externalDrop)
        app.button('PRERSS', press)

    with app.subWindow('sub', bg='red'):
        with app.frame('f2'):
            app.label('some text here')
            app.label("dropLab2", "Drop Here", drop=externalDrop)
