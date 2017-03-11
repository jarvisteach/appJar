import sys
sys.path.append("../../")
from appJar import gui



app = gui()
options=["apple", "ape", "apricot", "applause", "add", "address", "adept"]
app.addAutoEntry('Entry', options)
app.setFocus('Entry')
app.addLabel("l1", "l1")
app.go()
