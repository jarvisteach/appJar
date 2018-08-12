import sys
sys.path.append("../../")

from appJar import gui

toppings={"Cheese":False, "Tomato":False, "Bacon":False, "Corn":False, "Mushroom":False}

with gui() as app:
    app.bg = "lightBlue"
    app.fg = 'white'
    app.font = 20
    app.properties("Toppings", toppings, bg='green', fg='white')
    app.setProperty("Toppings", "Pepper")
