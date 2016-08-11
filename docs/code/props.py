from appJar import gui

def getEm(btn=None):
    if btn=="DELETE":
        app.deleteProperty("The props", app.getOptionBox("Prop"))
        # TODO: remove from OptionBox

    else:
        print(app.getProperties("The props"))
        print(app.getProperty("The props", app.getOptionBox("Prop")))

def change(btn=None):
    app.setProperty("The props", app.getOptionBox("Prop"), app.getCheckBox("Value"))

props = {
            "Name":True, "Age":False,
            "Name1":True, "Age1":False,
            "Name2":True, "Age2":False,
            "Name3":True, "Age3":False
        }

app=gui()

app.setBg("lightBlue")

app.addProperties("The props", props)
app.addButtons(["GET EM", "DELETE"], getEm)
app.addLabelOptionBox("Prop", ["Name", "Age", "Name1", "Age1", "Name2", "Age2", "Name3", "Age3"])
app.addCheckBox("Value")
app.setCheckBoxFunction("Value", change)

app.go()
