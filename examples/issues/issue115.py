import sys
sys.path.append("../../")

from appJar import gui

def trans(btn):
    t = app.getScale("t")
    print(t)
    print(type(t))
    app.setTransparency(t)

app=gui("T Test")
app.addLabel("l1", "Test transparency")
app.addScale("t")
app.setScaleRange("t", 100, 1, 100)
app.setScaleFunction("t", trans)
app.go()
