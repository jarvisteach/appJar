import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')

    app.startSubWindow('progress', modal=True)
    app.setSize('400x25')
    print("size set to 400x25")
    app.setResizable(False)
    app.setOnTop(stay=True)
    app.setStretch('both')
    app.setSticky('nsew')
    app.addMeter('progress')
    app.setMeter('progress', 0, text=None)
    app.setMeterFill('progress', 'Gray')
    app.stopSubWindow()

    app.showSubWindow('progress')
