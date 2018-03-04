import sys
sys.path.append("../")

from appJar import gui

app=gui("FRAME DEMO", "250x150")
app.setBg("yellow")

app.startFrame("LEFT", row=0, column=0)
app.setBg("blue")
app.setSticky("NEW")
app.setStretch("COLUMN")

app.addLabel("LEFT LABEL", "Label on the left")
app.setLabelBg("LEFT LABEL", "red")
app.addLabel("LEFT LABEL2", "Label on the left")
app.setLabelBg("LEFT LABEL2", "orange")
app.addLabel("LEFT LABEL3", "Label on the left")
app.setLabelBg("LEFT LABEL3", "yellow")
app.stopFrame()

app.startFrame("RIGHT", row=0, column=1)
app.setBg("green")
app.setFg("white")
for x in range(5):
    app.addRadioButton("RADIO", "Choice " + str(x))
app.stopFrame()

app.go()
