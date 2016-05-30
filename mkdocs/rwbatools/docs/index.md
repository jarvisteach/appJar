##To Begin
To build a GUI, requires a minimum of three steps:

1) **IMPORT** the library  
2) **CREATE** the GUI  
3) **START** the GUI  

```python
from rwbatools import gui   # import the library
app = gui()                 # create the GUI
app.go()                    # start the GUI  
```
In-between creating & starting the GUI, you **ADD** any widgets you want, and **SET** their properties.  

When adding a widget, you usually have to give it a title - this is used later if you want to change the widget.  

Then, you set any appropriate properties, for the widget, using its title.

```python
from rwbatools import gui

app = gui()
app.addLabel("title", "Welcome to RWBAtools")   # add a label
app.setLabelBg("title", "red")                           # set the label's background to be red
app.go()
```

Widgets will be added consecutively, each on a new line:
[Simple Layout](Layout#simple-layout)

If you want more than that, you will need to consider their layout.
[Grid Layout](Layout#grid-layout)

Widgets can be positioned in a grid, simply by providing a **ROW** and **COLUMN** position for each widget. It's also possible to specify how many columns to **SPAN**.

There are also a number of things you can configure about the GUI:
[GUI Options](GuiOptions)

---
##Widgets
The following widgets are available:

* [Label](Widgets#label) - Used for displaying writing
    * FlashLabel - a label that flashes
* [Entry](Widgets#entry) - A single line box for typing text
    * SecretEntry - an entry box that displays stars as the user types
    * NumericEntry - an entry box that only accepts numbers
* [Button](Widgets#button) - A clickable button, that will call a function
* [RadioButton](Widgets#radiobutton) - A group of round boxes, only one of which can be selected
* [CheckBox](Widgets#checkbox) - A box, with a label, that can be either ON or OFF
* [ListBox](Widgets#listbox) - A box containing a list of items, single or multi-select
* [SpinBox](Widgets#spinbox) - A scrollable option
* [Scale](Widgets#scale) - A slider, that has a minimum & maximum value
* [OptionBox](Widgets#optionbox) - A drop-down single-select option
* [Message](Widgets#message) - Like a multi-line label
* [TextArea](Widgets#textarea) - A multi-line box for typing text
* [Meter](Widgets#meter) - Used for showing progress
    * [SplitMeter](Widgets#splitmeter) - Shows two values, left & right
    * [DualMeter](Widgets#dualmeter) - shows percentage left & right
* [Image](Widgets#image) - shows an image
* [Separator](Widgets#separator) - shows a horizontal line
* [Link/WebLink](Widgets#linkweblink) - Clickable text to call a function or launch a URL

The following widgets are under deveopment

* [PieChart](devWidgets#piechart) - shows a pie chart
* [Tree](devWidgets#tree) - in development
* [Grid](devWidgets#grid) - in development

---
##Special Widgets
Some special widgets are available:

* [ToolBar](Toolbars#toolbar) - adds a toolbar along the top of the GUI
* [Menu](Toolbars#menu) - adds a standard Menu bar along the top of the GUI
* [Status](Toolbars#status) - adds a status bar along the bottom of the GUI

---
##Dialogs
A number of dialogs are available:

* [infoBox](Dialogs#infobox)
* [errorBox](Dialogs#errorbox)
* [warningBox](Dialogs#warningbox)
* [yesNoBox](Dialogs#yesnobox)
* [questionBox](Dialogs#questionbox)
* [okBox](Dialogs#okbox)
* [retryBox](Dialogs#retrybox)
* [openBox](Dialogs#openbox)
* [saveBox](Dialogs#savebox)
* [directoryBox](Dialogs#directorybox)
* [colourBox](Dialogs#colourbox)
* [textBox](Dialogs#textbox)
* [numBox](Dialogs#numbox)

---
##Layouts
Finally, a number of layouts are available:

* [LabelFrame](Layout#labelframe) - will put a border around the widgets, with a title
* [NoteBook](Layout#notebook) - will create a tabbed interface, with a number of pages
* [PanedWindow](Layout#panedwindow) - will create a split view, with draggable panes
* [SubWindow](Layout#subwindow) - used to create additional windows

---
##Sound
The GUI can also make SOUND (on Windows)

* `.playSound(sound, wait=False)`
* `.stopSound()`
* `.loopSound()`
* `.soundError()`
* `.soundWarning()`
* `.playNote(note, duration=200)`
