import sys
sys.path.append("../")
from appJar import gui

def press(btn=None): print(btn)
toppings={"Cheese":False, "Tomato":False, "Bacon":False,
            "Corn":False, "Mushroom":False}

with gui(bg="lightBlue", font=15) as app:
    app.guiPadding=5
    with app.toggleFrame("Toppings", bg="orange"):
        app.properties("Toppings", toppings, change=press, bg="blue", pos=(0, 0))
        app.setProperty("Toppings", "Pepper", callFunction=False)
        app.setProperty("Toppings", "Mushroom", True, callFunction=False)
        app.setProperty("Toppings", "Oranges", True, callFunction=False)
        app.properties("Bottoms", toppings, change=press, bg="green", pos=(0, 1))
