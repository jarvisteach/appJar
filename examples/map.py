import sys
sys.path.append("../")

def drop(btn):
    if btn == "Del":
        app.removeGoogleMapMarker("gq", app.entry("Del"))
    else:
        app.setGoogleMapMarker("gq", app.entry("Pin"), colour=app.option("colour"), label="B", replace=True)

def clear(btn):
    app.setGoogleMapMarker("gq", "")

from appJar import gui
app=gui()
app.addGoogleMap("gq", colspan=2)
app.entry("Pin", "Swindon, Morrisons", focus=True, label=True, submit=drop, column=0)
app.option("colour", ["0xFFFF00", "bbbbbb", "black", "red", "green", "yellow"], row=1, column=1, change=drop)
app.entry("Del", label=True, submit=drop, colspan=2)
app.button("CLEAR", clear, colspan=2)
app.go()
