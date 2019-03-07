import sys
sys.path.append("../../")

from appJar import gui

def go():
    for i in range(0, 10):
        val = 10*(i)
        app.thread(app.setMeter, "m1", val)
    # End for-loop
    app.thread(app.setMeter, "m1", 100)

with gui() as app:
    app.label('hello world')
    app.meter("m1", row=2, column=2, colspan=7, sticky="ew")
    app.setMeterFill("m1", "green")

    app.button("go", go)
