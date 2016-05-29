#Widget Library

##Label
Labels are used for displaying basic text on the screen.

* `.addLabel(title, text=None)`

    At a minimum, a title must be provided - to identify the label. This is then followed by an optional piece of text to display.

* `.addEmptyLabel(title)`

    Does the same as add a label, except there''s no parameter to set any text.

* `.addFlashLabel(title, text=None)`

    This adds a flashing label, that will alternate between the foreground and background colours.

* `.setLabel(title, text)`

    Change the contents of the label.

* `.getLabel(title)`

    Get the contents of the label.

* `.clearLabel(title)`

    Clear the contents of the label.

##Entry
Entries are used to capture input from the user. They take a single parameter - a title.

* `.addEntry(title)`
* `.addNumericEntry(title)`
* `.addSecretEntry(title)`
* `.addLabelEntry(title)`
* `.addNumericLabelEntry(title)`
* `.addSecretLabelEntry(title)`
* `.setEntry(title, text)`
* `.setEntryDefault(title, text)`
* `.getEntry(title)`
* `.clearEntry(title)`
* `.clearAllEntries()`
* `.setFocus(title)`

##Button
A clickable button, that will call a function

* `.addButton(title, function)`
* `.addButtons(titles, functions)`
* `.addNamedButton(name, title, function)`
* `.setButton(name, text)`
* `.setButtonImage(title, image)`

##RadioButton
A group of round boxes, only one of which can be selected

* `.addRadioButton(title, name)`
* `.getRadioButton(title)`
* `.setRadioButton(title, value)`
* `.setRadioTick(title, tick)`

##CheckBox
A box, with a label, that can be either ON or OFF

* `.addCheckBox(title)`
* `.getCheckBox(title)`
* `.setCheckBox(title, ticked)`

##ListBox
A box containing a list of items, single or multi-select

* `.addListBox(title, values)`
* `.setListBoxRows(title)`
* `.setListSingle(list, single)`
* `.selectListItem(title, item)`
* `.updateListItems(title, items)`
* `.addListItem(title, item)`
* `.addListItems(title, items)`
* `.getListItems(title)`
* `.removeListItem(title, item)`
* `.clearListBox(title)`

##SpinBox
A scrollable option

* `.addSpinBox(title, vals)`
* `.addSpinBoxRange(title, from, to)`
* `.addLabelSpinBox(title, vals)`
* `.addLabelSpinBoxRange(title, from, to)`
* `.getSpinBox(title)`
* `.setSpinBox(title, val)`
* `.setSpinBoxPos(title, pos)`

##Scale
A slider, that has a minimum & maximum value

* `.addScale(title)`
* `.setScaleRange(title from, to, curr=0)`
* `.orientScaleHor(title, hor=True)`
* `.setScale(title, pos)`
* `.getScale(title)`
* `.showScaleValue(title, show=True)`

##OptionBox
A drop-down single-select option

* `.addOptionBox(title, values)`
* `.addLabelOptionBox(title, values)`
* `.getOptionBox(title)`
* `.changeOptionBox(title, newOptions)`
* `.setOptionBox(title, position)`

##Message
Like a multi-line label

* `.addMessage(title, text)`
* `.addEmptyMessage(title)`
* `.clearMessage(title)`
* `.setMessage(title, text)`

##TextArea
A multi-line box for typing text

* `.addTextArea(title)`
* `.addScrolledTextArea(title)`
* `.setTextArea(title, text)`
* `.getTextArea(title)`
* `.clearTextArea(title)`
* `.logTextArea(title)`
* `.textAreaChanged(title)`

##Meter
Used for showing progress

###SplitMeter
Shows two values, left & right

###DualMeter
Shows percentage left & right

##Image
Shows an image, there are lots of things you can do with an image.

* `.addImage(name, file)`
* `.setImage(name, image)`
* `.setBgImage(image)`
* `.removeBgImage(image)`
* `.setImageSize(name, width, height)`
* `.zoomImage(name, mod)`

    Negative will shrink, positive will grow.

* `.shrinkImage(name, mod)`
* `.growImage(name, mod)`
* `.addAnimatedImage(name, file)` 
* `.setAnimationSpeed(name, speed)`
* `.stopAnimation(name)`
* `.startAnimation(name)`

##PieChart
Shows a pie chart

* `.addPieChart(name, values, size=100)`

##Separator
Shows a horizontal line

* `.addSeparator()`

##Link/WebLink
Clickable text to call a function or launch a URL

* `.addLink(title, func)`
* `.addWebLink(title, page)`

##Tree
This widget is still in development. It takes an arbitrary XML string, and converts it into a tree structure.

* `.addTree(title, xml_data)`

    Create a tree from the xml data

* `.addTreeFunction(title, func)`

    Register he function with double click

* `.getTree(title)`

    Return the tree

##Grid
This widget is still in development.  

* `.addGrid(title, data, action=None, addRow=False)`  

    Receives a (jagged) 2D list of values. The first list should be the headers for the grid, the rest will contain each row of values.  
    If action is set, a button will be created, calling the specified function. If addRow is True, then an additional row will appear, at the end, with Entry boxes.

* `.updateGrid(title, data, addRow=False)`
* `.setGridGeom(title, width, height)`
* `.getGridEntries(title)`
* `.setGridBackground(title, colour)`


#Additional Widgets

##ToolBar
Adds a toolbar along the top of the GUI

* `.addToolbar(names, funcs)`

    Will add a list of buttons along the top, in a toolbar. Each button will call the corresponding function.  
    If only one function is supplied, they will all call the same function.  
    A bundle of free images is available, if the name used for the toolbar matches the nam of an image, an image will be used.  

* `.setToolbarImage(name, image)`
Will set an image for the corresponding button in the toolbar.

##Menu
Adds a standard Menu bar along the top of the GUI
The menu bar will show, once the first menu has been added.
You can add a single menu option, or a list of menu options.

* `.addMenu(title, function)`

    Adds a single menu option, that will call the specified function.

* `.addMenuList(title, names, functions, tearable=False)`

    Will add a drop-down menu with the specified title.  
    Within the menu will be the list of names, each calling the corresponding function in the function list.  
    If only one function is provided, all menus will call the same function.  
    If the menu name is a '-', then a separator will be added to the menu.  
    If tearable is set to True, then the menu can be undocked.  

##Status
Adds a status bar along the bottom of the GUI.
This can be used for easy debugging, or as info for the user.

* `.addStatus(header="")`

    This turns the status bar on, and if a header is supplied, will prepend the header before every message.

* `.setStatus(text)`

    This updates the contents of the status bar. Again, if a header was set when adding the status bar, that will be prepended to the message.

* `.clearStatus()`
    
    Clear anything displayed in the status bar, along with any header that might be set.

