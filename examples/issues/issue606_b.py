import sys
sys.path.append("../../")

from appJar import gui
# global variable to store the count
counter = 20

def redirect(btn):
    if btn == 'REDIRECT': 
        app.redirectOutput('message', end=False)
    else:
        app.cancelRedirectOutput()

def loop(btn):
    global counter
    counter = 20
    if btn == 'START':
        app.registerEvent(countdown)
    else:
        app.unregisterEvent(countdown)

def countdown():
    global counter
    if counter > 0:
        print("counter" + str(counter))
        counter -= 1
    else:
        app.unregisterEvent(countdown)

with gui() as app:
    app.label('Logging Test')
    app.text('message', redirect=True)
    app.buttons(['REDIRECT', 'CANCEL'], redirect)
    app.buttons(['START', 'STOP'], loop)
