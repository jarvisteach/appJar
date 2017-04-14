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

* `.hide()` & `.show()`  
    Used to hide and show the main window.  
    Useful in conjunction with [SubWindows](/pythonWidgetGrouping/#sub-window)  
    You can have a menu or logon SubWindow that hides/shows the main window as necessary.  
    NB. hiding the window, effectively minimizes it, it is still there...

* `.setGeometry(geom)` & `.setGeometry(width, height)`  
    Sets the height & width of the GUI:  
    * Either as a single String `.setGeometry("200x100")` (widthxheight)  
    * As two separate parameters `.setGeometry(200,100)`
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

You can describe a font using a String or a Tuple. There are three properties that can be set:  

* Family - such as *Arial*, *Courier*, *Comic Sans*, *Sans Serif*, *Times* or *Verdana*  
* Size - the height in points  
* Style - one or more of *normal*, *bold*, *roman*, *italic*, *underline* & *overstrike*  

If the family has a space, then you should use a tuple, otherwise you can simply pass a space separated string:  
```python
font = "Times 16 bold underline"
font = ("Comic Sans", "20", "underline")
```

If the font can't be found, a default font will be used.  

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

