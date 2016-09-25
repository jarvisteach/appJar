from appJar import gui

def changed(props):
    print("Changed", props)

toppings={"Cheese":False, "Tomato":False, "Bacon":False,
            "Corn":False, "Mushroom":False}

app=gui()
app.setBg("lightBlue")
app.setFont(20)

app.startToggleFrame("Toppings")
app.addProperties("Toppings", toppings)
app.addProperties("Toppings2", toppings)
app.addProperties("Toppings3", toppings)
app.setPropertiesFunction("Toppings", changed)
app.stopToggleFrame()

app.go()
