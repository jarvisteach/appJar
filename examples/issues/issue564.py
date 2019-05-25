import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('counter')

    # global variable to store the count
    counter = 10

    def acceleratingCountdown():
        global counter
        if counter > 0:
            app.setLabel("counter", str(counter))
            counter -= 1
            app.after(100*counter, acceleratingCountdown)

    app.after(0, acceleratingCountdown)
