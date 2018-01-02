import sys
sys.path.append("../../")
from appJar import gui

with gui("appJar") as app:#, useTtk=True) as app:

#    app.setBg("blue")
#    app.ttkStyle.configure("TFrame", background="blue")
#    app.ttkStyle.configure("TLabelframe", background="blue")
#    app.ttkStyle.configure('TLabelframe.Label', background='blue')
#
#    app.ttkStyle.configure("TLabel", background="blue")
#    app.ttkStyle.configure("TCheckbutton", background="blue")
#
#    app.ttkStyle.configure('.', background="blue")


    with app.labelFrame("Text"):
#        app.setLabelFrameStyle("Text", "TLabelFrame")
        app.addCheckBox("Option here...")
        app.setCheckBoxStyle("Option here...", "TCheckbutton")

    app.addCheckBox("Another option...")
#    app.setCheckBoxStyle("Another option...", "TCheckbutton")

    with app.subWindow("sub"):
        app.setSticky("news")
        with app.frame("f", 0, 0):
            app.setBg("green")
            app.label("subLab1", "Testing sub")
            app.label("subLab2", "Testing sub")
            app.label("subLab3", "Testing sub")
        with app.frame("ff", 0, 1):
            app.setBg("green")
            app.label("subLab12", "Testing sub")
            app.label("subLab22", "Testing sub")
            app.label("subLab32", "Testing sub")

    app.showSubWindow("sub")
