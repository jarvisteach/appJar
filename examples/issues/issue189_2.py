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
    app.ttkStyle.configure('.', background="blue")


    with app.labelFrame("Text"):
#        app.setLabelFrameStyle("Text", "TLabelFrame")
        app.addCheckBox("Option here...")
        app.setCheckBoxStyle("Option here...", "TCheckbutton")

    app.addCheckBox("Another option...")
#    app.setCheckBoxStyle("Another option...", "TCheckbutton")
