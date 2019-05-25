import sys
sys.path.append("../../")

from appJar import gui

toppings={"Cheese":False, "Tomato":False, "Bacon":False, "Corn":False, "Mushroom":False}

with gui() as app:
    app.bg = "lightBlue"
    app.fg = 'white'
    app.font = 20

    rb = app.radio('a', 'b')
    cb = app.checkBox('a', selectcolor='blue')
    app.setCheckBoxSelectColour('a', 'green')
    # the bg colour of the box
    
    p = app.properties("Toppings", toppings)#, boxbg='black', foreground='white', background='blue', activebackground='pink', activeforeground='blue', indicatoron=True)
    #p.config(selectcolor='black', foreground='white', background='blue', activebackground='pink', activeforeground='blue', indicatoron=True)
    app.setPropertiesSelectColour('Toppings', 'red')
    app.setPropertiesBoxBg('Toppings', 'red')
    
    app.setProperty("Toppings", "Bacon", True)
