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
    If you want to disable the icon, set the `showIcon` flag to False, when you call appJar's constructor.  

* `.setTransparency(percentage)`  
    Sets how transparent the GUI is.  
    Between 0 and 100%.  

* `.setOnTop(stay=True)`  
    Configure the GUI to always stay on top of other windows.  

###Size & Location

* `.hide()` & `.show()`  
    Used to hide and show the main window.  
    Useful in conjunction with [SubWindows](/pythonWidgetGrouping/#sub-window)  
    You can have a menu or logon SubWindow that hides/shows the main window as necessary.  
    **NB.** hiding the window, effectively minimizes it, it is still there...

* `.setSize(size)` & `.setSize(width, height)`  
    Sets the height & width of the GUI:  
    * Either as a single String `.setSize("200x100")` (widthxheight)  
    * As two separate parameters `.setSize(200,100)`  
    * Or to go *Fullscreen* `.setSize("Fullscreen")`  

* `.exitFullscreen()`  
    Leave fullscreen, if set in the above.  
    Returns True/False - if the app was able to leave fullscreen.  
    Can be called safely, even if app is not in fullscreen:  
    `<Escape>` will call this automatically, while in fullscreen.  

```python
if app.exitFullscreen():
    # do something
else:
    app.setSize("fullscreen")
    # do something else
```   

* `.setResizable(canResize=True)`  
    Sets whether the GUI can be resized or not.  

* `.setLocation(x, y=None)`  
    Sets the position of the GUI.  
    If you want to position the widget in the center of the screen, set `x` to CENTER:
```python
app.setLocation("CENTER")
```

* `.setGuiPadding(x, y)`  
    Sets the size of the border inside the GUI - defaults to 2.  

* `.hideTitleBar()` & `.showTitleBar()`  
    Hides/shows the GUI's title bar.  
    Note, if the title bar is removed, it's not possible to move or resize the GUI.  

##GUI Design
---
It's possible to change the default colours and fonts for widgets in the GUI.

###Colour

* `.setFg(colour, override=False)`  
    Set a foreground colour for the entire GUI. By default, this will only apply to labels (including on RadioButtons & CheckButtons).  
    **NB.** To change the colour inside interactive widgets (Entry, TextArea, SpinBox, OptionMenu, etc), set `override` to be True.  

* `.setBg(colour, override=False, tint=False)`  
    Set the background colour for the GUI. This should affect all widgets, and will override any backgrounds set before.  
    **NB.** this doesn't change the background colour of interactive widgets (Entry, TextArea, etc). If you also want to update those, set `override` to True.  
    It's also possible to set a `tint` - this will determine an appropriate colour to set mouse-over, highlight colours, etc. It is set automatically if `override` is True.  

###Font

When configuring a font, the following style options can be set:

* `size` - the height in points  
* `family` - the family name, such as: *Arial*, *Courier*, *Comic Sans*, *Sans Serif*, *Times* or *Verdana*  
* `weight` - *bold* or *normal*  
* `slant` - *italic* or *roman*  
* `underline` - *True* or *False*  
* `overstrike` - *True* or *False*  

```python
app.setFont(size=16, family="Times", underline=True, slant="italic")
app.setButtonFont(size=14, family="Verdana", underline=False, slant="roman")
```

#### Setting a font  

* `.setFont(**style)`  
    This can be used to set the font for all widgets.  
    Pass in any of the above styles that are required.  

* `.setLabelFont(**style)`  
    This can be used to set the font for all label-type widgets.  
    Pass in any of the above styles that are required.  

* `.setButtonFont(**style)`  
    This can be used to set the font for all button-type widgets.  
    Pass in any of the above styles that are required.  

#### Modifying fonts

* `.decreaseFont()` & `.increaseFont()`  
    These can be used to increase or decrease the font of all widgets.

* `.increaseLabelFont()` & `.decreaseLabelFont()`  
    These can be used to increase or decrease the font of all label-type widgets.

* `.increaseButtonFont()` & `.decreaseButtonFont()`  
    These can be used to increase or decrease the font of all butotn-type widgets.

