import sys
sys.path.append("../../")

from appJar import gui

def press():
    print("std output")

def press2():
    import sys
    sys.stderr.write("std output")

with gui() as app:
    app.label('hello world')
    t = app.text('message')
    app.redirectOutput(t)
    app.button('text', press)
    app.button('error', press2)
