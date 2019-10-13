import sys
sys.path.append("../../")

from appJar import gui

def press2():
    app.enableButton('press')

def press():
    app.disableButton('press')

with gui() as app:
    app.label('hello world')
    app.button('press', press)
    app.button('press2', press2)

    app.setButtonDisabledFg('press', 'green')
    app.setButtonDisabledBg('press', 'purple')
    app.setButtonBg('press', 'yellow')
