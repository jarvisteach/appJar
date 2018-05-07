import sys
sys.path.append("../")

from appJar import gui

def press():
    print("User:", app.entry("Username"), "Pass:", app.entry("Password"))


with gui("Login Window", "400x300", bg='orange', font={'size':18}) as app:
    app.label("Welcome to appJar", bg='blue', fg='orange')
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.buttons(["Submit", "Cancel"], [press, app.stop])
