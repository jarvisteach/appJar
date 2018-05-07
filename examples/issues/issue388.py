import sys
sys.path.append('../../')
#simple grid test from website
#http://appjar.info/pythonDevWidgets/#grid
#Paul Dymerski pdymersk@gmail.com

from appJar import gui

def size(size):
    app.font = {'size':int(size)}

def family():
    app.font = {'family':app.option('family')}

with gui("men", font={'size':12}) as app:

    app.addTable("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]], border="SUNKEN")

    app.buttons([7, 8, 9, 10, 12, 14, 20], size)
    app.option('family', app.fonts, submit=family)
