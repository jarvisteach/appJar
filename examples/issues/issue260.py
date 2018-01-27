import sys
sys.path.append("../../")
#!/usr/bin/python3 
from appJar import gui

# create the GUI & set a title 
app = gui("Boat Log", useTtk=True)

def blExit(x):
    app.stop()

#app.useTtk()


app.addLabelEntry("Daily Checks")

app.addButtons( ["Exit", "b"], blExit)   


# start the GUI 
app.go() 
