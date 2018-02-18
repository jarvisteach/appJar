import sys
sys.path.append('../../')
#simple grid test from website
#http://appjar.info/pythonDevWidgets/#grid
#Paul Dymerski pdymersk@gmail.com

from appJar import gui
appjar = 'next'

#from appJar_3 import gui
#appjar = 'None'

app = gui()
app.setFont(size=7)

if (appjar == 'next'):
    app.addTable("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["TinTinTinTinTinaaaaaTina", 37, "Female"],
        ["Clive", 28, "MalMalMalMalMaleeeeeMale"],
        ["Betty", 555555551111111151, "Female"]])
else:
    app.addGrid("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]])
app.go()
