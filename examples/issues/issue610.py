import sys
sys.path.append("../../")

from appJar import gui

with gui("aaa", "800x800") as app:
    app.label('hello world')
    with app.panedFrame("p0", vertical=True):
            app.addLabel("test1", "Test in new Pane")
            with app.panedFrame("p1", vertical=True):
                app.label("batLabel", "Battery Level", 0,0,fg="white")
                app.meter("battery-level",1,0, fill="green")
                app.label("battStatus","",fg="white", stretch="row", sticky="ew")
            with app.panedFrame("p2", sash=80):

                app.addLabelEntry("Inspection-Reference", 1,1)
                app.label("dummyLabel","This is a test" ,0,0,2, bg="red", fg="white")
