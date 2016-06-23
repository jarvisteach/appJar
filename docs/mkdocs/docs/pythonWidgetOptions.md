#Widget Options
----
There are a lot of things that can be configured on a widget.  
There is a pattern to how this works, you simply specify the widget type and the parameter, eg:

* `.setLabelBg(name, value)`
* `.setButtonFg(name, value)`
* `.setListBoxState(name, value)`

The list of widgets is defined in `gui.WIDGETS`, it contains:
Label, Message, Button, Entry, Scale, SpinBox, OptionBox, TextArea, Link, Meter, Image, RadioButton, CheckBox, ListBox, LabelFrame, PanedWindow, NoteBook

###Basic Appearance
----
The following options are available for all widgets:

* `set XXX Bg(name, value)`  
    Sets the background colour of the named widget.

* `set XXX Fg(name, value)`  
    Sets the foregound colour (usually the text) of the named widget.

* `set XXX DisabledFg(name, value)`  
    Sets the disabled foreground colour (usually the text) of the named widget.

* `set XXX Width(name, value)`  
    Sets the width of the named widget.

* `set XXX Height(name, value)`  
    Set the height of the named widget.

###Extended Appearance
---
* `set XXX Tooltip(name, value)`  
    Sets a tooltip for the widget.
    The specified text will be displayed in a small pop-up, when the mouse is left over the widget.

* `set XXX Cursor(name, value)`  
    Sets the cursor shown, when the mouse goes over this widget.  
    There are lots of cursors avalable, for different platforms, see [here](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html)

* `set XXX Relief(name, value)`  
    Sets the border for the widget. One of: `SUNKEN`, `RAISED`, `GROOVE`, `RIDGE`, `FLAT`  

* `set XXX State(name, value)`  
    Sets the state of the named widget. One of: `NORMAL`, `ACTIVE`, `DISABLED`  

###Advanced Appearance
----
The following are supported by most widgets:

* `set XXX Align(name, value)`  
    Specifies how to align text within the widget: `LEFT`, `RIGHT`, `CENTER`

* `set XXX Anchor(name, value)`  
    Sets where the text is positioned within the widget. One of: `CENTER`, `N`, `S`, `E`, `W`, `NE`, `NW`, `SE`, `SW`  

* `set XXX Sticky(name, value)`  
    Specifies which side of the cell to stick the widget to, as the GUI expands: `LEFT`, `RIGHT`, `BOTH`

###Widget Interaction
----
The following allow widgets to be interacted with:

* `set XXX Focus(name)`  
    Gives focus to the specified widget. This is the widget where the user will be able to start typing.

* `set XXX Function(name, value, key=None)`  
    This binds a function to the widget.  
    The function will be called every time an interactive-widget changes. 
    The funcion will be called when some widgets are clicked.  

* `set XXX OverFunction(name, values)`  
    Set functions to call whenever the mouse enters (goes over) or leaves the specified widget.  
    The first function is called when the mouse first enters the widget.  
    The second function is called when the mouse leaves the widget.  
    If you only want a function to be called when the mouse leaves the widget, pass an array like: `[None, leave]`  

```python
    from appJar import gui

    def enter(wdgt): 
        print("IN", wdgt)
    def leave(wdgt):
        print("OUT", wdgt)

    app=gui()
    app.addLabel("l1", "Testing...")
    app.setLabelOverFunction("l1", [enter, leave])
    app.go()
```  
* `set XXX DragFunction(name, values)`  
    Set functions to call whenever the mouse button is clicked and dragged.  
    The first function will be called when the mouse is initially clicked.  
    The second function will be called when the mouse is released.  
    The same rules for passing functions apply as above.  


###Widget Manipulaiton
----
The following allow widgets to be manipulated on screen:

* `.hide XXX (name)`  
    Temporarily hides the widget form view.

* `.show XXX (name)`  
    Show the widget, if it was already hidden.

* `.remove XXX (name)`  
    Permanently remove the widget (deletes it).

* `.removeAllWidgets()`  
    Permanenently remove all widgets.

* `.disable XXX (name)`  
    Disable the widget - stops the user from interacting with it, but keeps it visible.

* `.enable XXX (name)`  
    Enable a disabled widget.

###Grouped Options
----
The following are convenience functions, for modifying a group of widgets:

* `set XXX Widths(names, val)`  
* `set XXX Heights(names, val)`  
    Sets the widths/heights of the specified widgets.

* `setAll XXX Widths(val)`  
* `setAll XXX Heights(val)`  
    Sets the widths/heights of all widgets of the specified type.
