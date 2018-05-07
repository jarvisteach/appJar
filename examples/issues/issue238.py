import sys
sys.path.append("../../")

from appJar import gui

with gui("Entry Demo") as app:
    app.addEntry("e1").bind("<Return>", app._gui__focusNextWindow)
    app.addEntry("e2").bind("<Return>", app._gui__focusNextWindow)
    app.addEntry("e3").bind("<Return>", app._gui__focusNextWindow)
