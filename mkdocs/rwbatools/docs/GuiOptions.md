#GUI Options
---
There are a number of generic configurations available, which will affect the whole GUI.  
Some of these are also available at a widghet level, where you can specify individual configurations tor specified widgets.  

###Configuration
---

Some basic configuration for the size, position, transparency, etc. of the GUI.

####Size & Locaiton

* `setGeometry(geom)`
* `setGeometry(width, height)`

    Sets the height & width of the GUI, either as a single String widthxheight.  
    Or, sets it fullscreen

* `exitFullscreen()`

    Leave fullscreen, if set in the geometry.  
    `<Escape>` will call this automatically, while in fullscreen.

* `setResizable(canResize=True)`

    Sets whether the GUI can be resized or not.

* `setLocation(x, y)`

    Sets the position of the GUI

####Look & Feel

* `setTitle(title)`

    Sets the title of the GUI. By default it is the name of the script.

* `setIcon(fileName)`

    Sets an icon for the GUI.

* `setTransparency(percentage)`

    Sets how transparent the GUI is. Between 0 and 100%.

###Design
----

It's possible to change the default colours and fonts for widgets in the GUI.

####Colour

* `setBg(colour)`

    Set the background colour for the entire GUI. This should affect all widgets, and will override any backgrounds set before.

####Font

* `setFont(size, font=None)`

    This can be used to set the font size and style for all widgets.

* `decreaseFont()`
* `increaseFont()`

    These can be used to increase or decrease the font of all widgets.

* `setLabelFont(size, family=None)`

    This can be used to set the font size and style for all label-type widgets.

* `increaseLabelFont()`
* `decreaseLabelFont()`

    These can be used to increase or decrease the font of all label-type widgets.

* `setButtonFont()`

    This can be used to set the font size and style for all button-type widgets.

* `increaseButtonFont()`
* `decreaseButtonFont()`

    These can be used to increase or decrease the font of all butotn-type widgets.

### Widget Positioning
----

The below commands allow the user to change how RWBAtools lays out widgets on the screen.

####Location

* `setPadX()`
* `setPadY()`

    These set how much empty padding is included around a widget, within its grid-cell.

* `setSticky()`

    This determines which side of the grid-cell the widget will stick to:

    * ```left``` - stick to the left side
    * ```right``` - stick to the right side
    * ```both``` - stick to both sides, stretch the widget

####Resize

* `setExpand()`

    This tells widgets what to do when the GUI is resized.  
    It allows widgets to be configured to stretch or not:

    * ```none``` - don't expand
    * ```row``` - expand with rows only
    * ```column``` - expand with columns only
    * ```all``` - expand in all directions

####Row Helpers

* `getRow()`

    Returns the row number currently being used.

* `getNextRow()`

    Returns the current row number, before adding one to it.

###GUI Actions
----
####Repeated Events
When you start the GUI, it kicks off an infinte loop that is waiting for the user to do something.  
That means, you should never have your own loops running, as that will stop the GUI from working properly.  
Instead, if you want your own loop to run, you need to ask the GUi to run it for you:  

* `registerEvent(func)`

    Pass this a function, and the GUI will call that function every second.

* `setPollTime(time)`

    If you want your events to be called more or less frequently, set the frequency here.

####Enter Key

* `enableEnter(func)`

    Link a function to the `<Enter>` key

* `disableEnter()`

    Unlink a function form the `<Enter>`  key

####Other Keys

* `bindKey(key, func)`

    Link the specified key to the specified function.

* `unbindKey(key)`

    Unlink the specified key from any functions bound to it.

