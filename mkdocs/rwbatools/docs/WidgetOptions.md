#Widget Options
----

There are a lot of things that can be configured on a widget.

There is a pattern to how this works, you simply specify the widget type and the parameter, eg:

* `.setLabelBg(name, value)`
* `.setButtonFg(name, value)`
* `.setListBoxState(name, value)`

The list of widgets is defined in `gui.WIDGETS`, it contains:
Label, Message, Button, Entry, Scale, SpinBox, OptionBox, TextArea, Link, Meter, Image, RadioButton, CheckBox, ListBox, LabelFrame, PanedWindow, NoteBook

###Basic Configuration
----

The following options are available for all widgets:

* `set XXX Bg(name, value)`

    Sets the background colour of the named widget.

* `set XXX Fg(name, value)`

    Sets the foregound colour (usually the text) of the named widget.

* `set XXX DisabledBg(name, value)`

    Sets the disabled background colour of the named widget.

* `set XXX EnabledFg(name, value)`

    Sets the disabled foreground colour (usually the text) of the named widget.

* `set XXX Width(name, value)`

    Sets the width of the named widget.

* `set XXX Height(name, value)`

    Set the height of the named widget.

* `set XXX State(name, value)`

    Sets the state of the named widget.  
    One of: NORMAL, ACTIVE, DISABLED  

###Advanced Configuration
----

The following are supported by most widgets:

* `set XXX Relief(name, value)`

    Sets the border for the widget.  
    One of: SUNKEN, RAISED, GROOVE, RIDGE, FLAT  

* `set XXX Align(name, value)`
* `set XXX Anchor(name, value)`

    Sets where the text is positioned within the widget.  
    One of: CENTER, N, S, E, W, NE, SE, SW, NW  

* `set XXX Tooltip(name, value)`

    Sets a tooltip for the widget.
    The specified text will be displayed in a small pop-up, when the mouse is left over the widget.

* `set XXX Function(name, value, key=None)`

    This binds a function to the widget.  
    The function will be called every time an interactive-widget changes. 
    The funcion will be called when some widgets are clicked.  

* `set XXX DragFunction(name, value, key=None)`
* `set XXX OverFunction(name, value, key=None)`
* `set XXX Cursor(name, value)`
* `set XXX Focus(name)`

    Gives focus to the specified widget.

* `set XXX Sticky(name, value)`

###Widget Manipulaiton
----

The following allow widgets to be manipulated:

* `.show XXX (name)`
* `.hide XXX (name)`
* `.remove XXX (name)`
* `.removeAllWidgets()`
* `.enable XXX (name)`
* `.disable XXX (name)`

###Grouped Options
----

* `set XXX Widths(names, val)`
* `set XXX Heights(names, val)`
* `setAll XXX Widths(val)`
* `setAll XXX Heights(val)`
