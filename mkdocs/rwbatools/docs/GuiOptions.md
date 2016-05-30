# GUI Options
____

###GUI Configuration

Some basic configuration for the size, position, transparency, etc. of the GUI.

* `setGeometry(geom)`
* `setGeometry(width, height)`

    Sets the height & width of the GUI, either as a single String widthxheight.  
    Or, sets it fullscreen

* `exitFullscreen()`

    Leave fullscreen, if set in the geometry.  
    `<Escape>` will call this automatically, while in fullscreen.

* `setTitle(title)`

    Sets the title of the GUI. By default it is the name of the script.

* `setResizable(canResize=True)`

    Sets whether the GUI can be resized or not.

* `setTransparency(percentage)`

    Sets how transparent the GUI is. Between 0 and 100%.

* `setIcon(fileName)`

    Sets an icon for the GUI.

* `setLocation(x, y)`

    Sets the position of the GUI

### GUI Actions
----

####Repeated Events
When you start the GUI, it kicks off an infinte loop that is waiting for the user to do something.  
That means, you should never have your own loops running, as that will stop the GUI from working properly.  
Instead, if you want your own loop to run, you need to ask the GUi to run it for you:  

* `registerEvents(func)`

    Pass this a function, and the GUI will call that function every second.

* `setPollTime(time)`

    If you want your events to be called more or less frequently, set the frequency here.

####Enter Key

* `enableEnter(func)`

    Link a function to the `<Enter>`  key

* `disableEnter()`

    Unlink a function form the `<Enter>`  key

####Other Keys

* `bindKey(key, func)`

    Link the specified key to the specified function.

* `unbindKey(key)`

    Unlink the specified key from any functions bound to it.

### Widget Positioning
----

* `setPadX()`
* `setPadY()`
* `setSticky()`
* `setExpand()`
* `getRow()`
* `getNextRow()`

### GUI Design
----

* `setBg()`
* `setLabelFont()`
* `increaseLabelFont()`
* `decreaseLabelFont()`
* `setButtonFont()`
* `increaseButtonFont()`
* `decreaseButtonFont()`
* `setFont()`
* `decreaseFont()`
* `increaseFont()`
