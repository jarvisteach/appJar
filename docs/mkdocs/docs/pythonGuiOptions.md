#GUI Options
---
There are a number of generic configurations available, which will affect the whole GUI.  
Some of these are also available at a widget level, where you can specify individual configurations tor specified widgets.  

##GUI Configuration
---

Some basic configuration for the size, position, transparency, etc. of the GUI.

###Look & Feel  
* `.setTitle(title)`  
    Sets the title of the GUI. By default, it is the name of the script.

* `.setIcon(fileName)`  
    Sets an icon for the GUI.

* `.setTransparency(percentage)`  
    Sets how transparent the GUI is. Between 0 and 100%.

###Size & Locaiton

* `.setGeometry(geom)` & `.setGeometry(width, height)`  
    Sets the height & width of the GUI:  
    * Either as a single String `.setGeometry("200x100")` (widthxheight)  
    * As two seperate parameters `.setGeometry(200,100)`
    * Or to go *Fullscreen* `.setGeometry("Fullscreen")`  

* `.exitFullscreen()`  
    Leave fullscreen, if set in the geometry.    
    Returns True/False - if the app was able to leave fullscreen.
    Can be called safely, even if app is not in fullscreen:
    `<Escape>` will call this automatically, while in fullscreen.  

```python
if app.exitFullscreen():
    # do something
else:
    app.setGeometry("fullscreen")
    # do something else
```   

* `.setResizable(canResize=True)`  
    Sets whether the GUI can be resized or not.  

* `.setLocation(x, y)`  
    Sets the position of the GUI.  

* `.setGuiPadding(x, y)`  
    Sets the size of the border inside the GUI - defaults to 2.  

* `.hideTitleBar()` & `.showTitleBar()`  
    Hides/shows the GUI's title bar.  
    Note, if the title bar is removed, it's not possible to move or resize the GUI.  

##GUI Design
----
It's possible to change the default colours and fonts for widgets in the GUI.

###Colour

* `.setBg(colour)`  
    Set the background colour for the entire GUI. This should affect all widgets, and will override any backgrounds set before.

###Font
* `.setFont(size, font=None)`  
    This can be used to set the font size and style for all widgets.

* `.decreaseFont()` & `.increaseFont()`  
    These can be used to increase or decrease the font of all widgets.

* `.setLabelFont(size, family=None)`  
    This can be used to set the font size and style for all label-type widgets.

* `.increaseLabelFont()` & `.decreaseLabelFont()`  
    These can be used to increase or decrease the font of all label-type widgets.

* `.setButtonFont()`  
    This can be used to set the font size and style for all button-type widgets.

* `.increaseButtonFont()` & `.decreaseButtonFont()`  
    These can be used to increase or decrease the font of all butotn-type widgets.

