from appJar import gui

def press(btn=None): print(btn)
toppings={"Cheese":False, "Tomato":False, "Bacon":False,
            "Corn":False, "Mushroom":False}

app=gui()
app.setBg("lightBlue")
app.setFont(20)
app.addProperties("Toppings")
app.setProperties("Toppings", toppings)
app.setProperty("Toppings", "Pepper")
app.setPropertiesFunction("Toppings", press)
app.go()
