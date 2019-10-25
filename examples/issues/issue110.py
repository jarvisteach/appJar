import sys
sys.path.append("../../")
from appJar import gui



app = gui()
options=["apple", "ape", "apricot", "applause", "add", "address", "adept"]
app.sticky = 'w'
app.addAutoEntry('Entry', options, row=0, column=0)
app.setAutoEntryNumRows('Entry', 3)

app.setEntryTooltip('Entry', 'sldfknsldjsdl')
app.addLabel("l1", "l1", row=1, column=0)
app.stretch = 'both'
app.sticky = 'n'
app.addLabel("l2", "l2", row=0, column=1)
app.addAutoEntry('Entry2', options, row=1, column=1)
app.setEntryTooltip('Entry2', 'sldfknsldjsdl')
app.setFocus('Entry')
app.go()
