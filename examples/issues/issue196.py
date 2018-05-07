import sys
sys.path.append("../../")

from appJar import gui

def changeCol(col):
    app.setBg(col)
    app.setFg(col, True)
#    app.setTextAreaFg("st1", col)
#    app.setTextAreaFg("t1", col)

app=gui()
app.setBg("blue")
app.addTextArea("t1")
app.addScrolledTextArea("st1")
app.setTextAreaRelief("st1", "raised")
app.setTextAreaRelief("t1", "raised")
app.setBg("yellow")
app.addButtons(["Red", "Yellow", "Green", "Blue", "Pink"], changeCol)
app.go()
