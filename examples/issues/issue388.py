import sys
sys.path.append('../../')
#simple grid test from website
#http://appjar.info/pythonDevWidgets/#grid
#Paul Dymerski pdymersk@gmail.com

from appJar import gui
appjar = 'next'

#from appJar_3 import gui
#appjar = 'None'

app = gui("men", "110x100")
app.setFont(size=7)

if (appjar == 'next'):
    app.addTable("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]])
else:
    app.addGrid("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]])
app.go()
