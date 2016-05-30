#Widgets
----

Below is a comprehensive list of all the widgets that can be included in a GUI.

They are all used in the same way:

* First, ADD a widget
* Then, SET any paramters for the widget
* Finally, if needed, GET the contents of the widget

##Label

Labels are used for displaying basic text on the screen.

####Add Labels

* `.addLabel(title, text=None)`

    At a minimum, a title must be provided - to identify the label. This is then followed by an optional piece of text to display.

* `.addEmptyLabel(title)`

    Does the same as add a label, except there''s no parameter to set any text.

* `.addFlashLabel(title, text=None)`

    This adds a flashing label, that will alternate between the foreground and background colours.


####Change Labels

* `.setLabel(title, text)`

    Change the contents of the label.

* `.clearLabel(title)`

    Clear the contents of the label.

####Get Labels

* `.getLabel(title)`

    Get the contents of the label.

##Entry
Entries are used to capture input from the user. They take a single parameter - a title.

####Add Entries

* `.addEntry(title)`
* `.addNumericEntry(title)`
* `.addSecretEntry(title)`
* `.addLabelEntry(title)`
* `.addNumericLabelEntry(title)`
* `.addSecretLabelEntry(title)`

#### Change Entries

* `.setEntry(title, text)`
* `.setEntryDefault(title, text)`
* `.clearEntry(title)`
* `.clearAllEntries()`
* `.setFocus(title)`

#### Get Entries

* `.getEntry(title)`


##Button
A clickable button, that will call a function

####Add Buttons

* `.addButton(title, function)`
* `.addButtons(titles, functions)`
* `.addNamedButton(name, title, function)`

####Change Buttons

* `.setButton(name, text)`
* `.setButtonImage(title, image)`

##RadioButton
A group of round boxes, only one of which can be selected

####Add RadioButtons

* `.addRadioButton(title, name)`

####Change RadioButtons

* `.setRadioButton(title, value)`
* `.setRadioTick(title, tick)`

####Get RadioButtons

* `.getRadioButton(title)`

##CheckBox
A box, with a label, that can be either ON or OFF

####Add CheckBoxes

* `.addCheckBox(title)`

####Change CheckBoxes

* `.setCheckBox(title, ticked)`

####Get CheckBoxes

* `.getCheckBox(title)`

##ListBox
A box containing a list of items, single or multi-select

####Add ListBoxes

* `.addListBox(title, values)`
* `.addListItem(title, item)`
* `.addListItems(title, items)`

####Change ListBoxes

* `.setListBoxRows(title)`
* `.setListSingle(list, single)`
* `.selectListItem(title, item)`
* `.updateListItems(title, items)`
* `.removeListItem(title, item)`
* `.clearListBox(title)`

####Get ListBoxes

* `.getListItems(title)`

##SpinBox
A scrollable option

####Add SpinBoxes

* `.addSpinBox(title, vals)`
* `.addSpinBoxRange(title, from, to)`
* `.addLabelSpinBox(title, vals)`
* `.addLabelSpinBoxRange(title, from, to)`

####Change SpinBoxes

* `.setSpinBox(title, val)`
* `.setSpinBoxPos(title, pos)`

####Get SpinBoxes

* `.getSpinBox(title)`

##Scale
A slider, that has a minimum & maximum value

####Add Scales

* `.addScale(title)`

####Change Scales

* `.setScaleRange(title from, to, curr=0)`
* `.orientScaleHor(title, hor=True)`
* `.setScale(title, pos)`
* `.showScaleValue(title, show=True)`

####Get Scales

* `.getScale(title)`

##OptionBox
A drop-down single-select option

####Add OptionBoxes

* `.addOptionBox(title, values)`
* `.addLabelOptionBox(title, values)`

####Change OptionBixes

* `.changeOptionBox(title, newOptions)`
* `.setOptionBox(title, position)`

####Get OptionBoxes

* `.getOptionBox(title)`

##Message
Like a multi-line label

####Add Messages

* `.addMessage(title, text)`
* `.addEmptyMessage(title)`

####Change Messages

* `.clearMessage(title)`
* `.setMessage(title, text)`

##TextArea
A multi-line box for typing text

####Add TextAreas

* `.addTextArea(title)`
* `.addScrolledTextArea(title)`

####Change TextAreas

* `.setTextArea(title, text)`
* `.clearTextArea(title)`
* `.logTextArea(title)`
* `.textAreaChanged(title)`

####Get TextAreas

* `.getTextArea(title)`

##Meter
Used for showing progress

* ###Meter

    Shows a simple progress meter

    * `addMeter(name)`

        Adds a meter with the specified name.

    * `setMeter(name, value, text=None)`

        Changes the specified meter to the specified value, between 0 and 100, with the optional text.

    * `setMeterFill(name, colour)`

        Changes the fill colour of the specified meter.

    * `getMeter(name)`

        Gets the value of the specified meter.

* ###SplitMeter

    Shows two values, left & right

* ###DualMeter

    Shows percentage left & right

##Separator
Shows a horizontal line

* `.addSeparator()`

##Link/WebLink
Clickable text to call a function or launch a URL

####Add Links

* `.addLink(title, func)`
* `.addWebLink(title, page)`

##Image
Shows an image, there are lots of things you can do with an image.

####Add Images

* `.addImage(name, file)`
* `.addAnimatedImage(name, file)` 

####Change Images

* `.setImage(name, image)`
* `.setImageSize(name, width, height)`
* `.zoomImage(name, mod)`

    Negative will shrink, positive will grow.

* `.shrinkImage(name, mod)`
* `.growImage(name, mod)`

####Change Image Animation

* `.setAnimationSpeed(name, speed)`
* `.stopAnimation(name)`
* `.startAnimation(name)`

####Change Background Images

* `.setBgImage(image)`
* `.removeBgImage(image)`

