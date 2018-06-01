import sys
sys.path.append("../../")

from appJar import gui

def login():
    app.popUp("Invalid login", kind="error", parent="Login")

with gui("Test Program", '200x200', bg="#3B3B98", fg="#F8EFBA", font={'family':'skia', 'size':20}) as app:
    app.label("Main App")
    app.button("Login", app.showSubWindow)

    with app.subWindow("Login", modal=True, bg="#2C3A47", fg="#B33771"):
        app.label("Login Page")
        app.button("OK", login)
