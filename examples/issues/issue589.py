import sys
sys.path.append("../../")

from appJar import gui


app=gui("AppJar Calculator", "400x300")
app.setResizable(False)
app.setSticky('news')
app.setStretch('both')
app.addEmptyLabel("res", 0,1)
app.setLabelBg("res", "blue")

app.go()
