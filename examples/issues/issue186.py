import sys
sys.path.append("../../")

from appJar import gui

app=gui()

app.addLabel("l1", u'\u23F8')
app.addLabel("l2", u'\u23F8')
app.addLabel("l3", u'\U0001F33B')


app.go()
