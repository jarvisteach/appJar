from appJar import gui  
def changeLabel(btn):  
      app.setLabel("l2", app.getEntry("text"))  
app = gui()  
app.addLabel("l1", "Simple Demo")
app.addEntry("text")
app.addButton("OK", changeLabel)
app.addEmptyLabel("l2")
app.go()
