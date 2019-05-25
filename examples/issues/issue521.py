import sys
sys.path.append("../../")

from appJar import gui

def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

def started():
    print('GUI is going...')

while True:
    with gui('Stop test') as app:
        app.label('Stop Test')
        app.button('quit', app.stop)
        app.stopFunction = checkStop
        app.startFunction = started
