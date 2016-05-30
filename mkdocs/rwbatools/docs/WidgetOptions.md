#Widget Options
----

There are a lot of things that can be configured on a widget.

There is a pattern to how this works, you simply specify the widget type and the parameter, eg:

* `.setLabelBg(name, value)`
* `.setButtonFg(name, value)`
* `.setListBoxState(name, value)`


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

###Advanced Configuration
----

The following are supported by most widgets:

* `set XXX Relief(name, value)`
* `set XXX Align(name, value)`
* `set XXX Anchor(name, value)`
* `set XXX Tooltip(name, value)`
* `set XXX Function(name, value, key=None)`
* `set XXX DragFunction(name, value, key=None)`
* `set XXX OverFunction(name, value, key=None)`
* `set XXX Cursor(name, value)`
* `set XXX Focus(name)`
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
