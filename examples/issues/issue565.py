import sys
sys.path.append("../../")

from appJar import gui

g=True

def go():
    for i in range(0, 10):
        val = 10*(i)
        app.thread(app.setMeter, "m1", val)
        app.thread(app.setMeter, "m2", val)
        app.thread(app.setMeter, "m3", val)
        app.thread(app.setMeter, "m4", val)
    # End for-loop
    app.thread(app.setMeter, "m1", 100)
    app.thread(app.setMeter, "m2", 100)
    app.thread(app.setMeter, "m3", 100)
    app.thread(app.setMeter, "m4", 100)

with gui('test', '600x200') as app:
    app.label('hello world')
    app.meter("m1", sticky="ew", gradient=g, fill='blue')
    app.meter("m2", sticky="ew", gradient=g, fill='green')
    app.meter("m3", sticky="ew", gradient=g, fill='red')
    app.meter("m4", sticky="ew", gradient=g, fill='black')

    app.setMeterFill('m2', 'pink', False)

    app.button("go", go)
