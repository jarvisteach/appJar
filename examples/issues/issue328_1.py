import sys
sys.path.append("../../")
from appJar import gui

def reset():
    print("breaking?")
    app.removeAllWidgets()
    app.label("Some text")
    app.button("Accessibility", app.showAccess, icon="ACCESS", tip="Click here for accessibility options")
    app.button("RESET", reset)

with gui("COLOUR TEST", "400x400") as app:
    reset()
