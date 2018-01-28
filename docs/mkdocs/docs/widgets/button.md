##Button
---

A clickable button, that will call a function.  
These are the key to starting an interactive application.  
The GUI is looping, waiting for something to happen.  
A button click is the classic way to start interacting with a GUI.

Whenever any function is called by the GUI, the title of the widget that called it is passed as a parameter.  
That way, multiple widgets can use the same function, but different actions can be performed, depending on the name passed as a parameter.

![Buttons](../img/1_buttons.gif)

```python
    from appJar import gui

    # the title of the button will be received as a parameter
    def press(btn):
        print(btn)

    app=gui()
    # 3 buttons, each calling the same function
    app.addButton("One", press)
    app.addButton("Two", press)
    app.addButton("Three", press)
    app.go()
```

####Add Buttons

* `.addButton(title, function)`  
    Add a single button to the GUI, the text on the button will be the same as the button's title.  
    A function should be specified, which will be called when the button is clicked, where the title is passed as a parameter to the function.  
    Alternatively, the function can have no parameter, and appJar will not supply an argument.     

* `.addButtons(titles, functions)`  
    It's possible to add a list of buttons to the GUI.  
    Pass a 1-dimensional or 2-dimensional list, and they will be rendered accordingly.  
    A single function can be passed, to use for all buttons.  
    Or a list of functions can be passed, which MUST correspond to the buttons.  

* `.addImageButton(title, function, imgFile, align=None)`  
    This creates the named button, as above, using the specified image.  
    If align is set, the image will be aligned relative to the text, otherwise the image will replace the text.  

* `.addIconButton(title, function, iconName, align=None)`  
    This creates the named button, as above, using the specified icon.  
    If align is set, the image will be aligned relative to the text, otherwise the image will replace the text.  

* `.addNamedButton(name, title, function)`  
    By default, it's not possible to have two buttons with the same text.  
    If that's required, a named button should be used.  
    This allows a name and title to be set for a button.  
    The name will be displayed on the button, and the title passed to the function.

####Set Buttons
* `.setButton(name, text)`  
    This will change the text displayed on a button, but **NOT** the value passed as a parameter to the function.  

* `.setButtonImage(title, image, align=None)`  
    This allows an image to be placed on a button, instead of the usual text.  
    If align is set, the image will be aligned relative to the text, otherwise the image will replace the text.  
