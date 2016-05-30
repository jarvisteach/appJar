#Widgets
----

Below is a comprehensive list of all the widgets that can be included in a GUI.

They are all used in the same way:

* First, **ADD** a widget
* Then, **SET** any paramters for the widget
* Finally, if needed, **GET** the contents of the widget

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

There are two special-case entries:

* NumericEntry - this only allows numbrs to be typed in.
* SecretEntry - this will show stars, instead of the letters typed - useful for capturing passwords.

####Add Entries

* `.addEntry(title)`
* `.addNumericEntry(title)`
* `.addSecretEntry(title)`
* `.addLabelEntry(title)`
* `.addNumericLabelEntry(title)`
* `.addSecretLabelEntry(title)`

#### Change Entries

* `.setEntry(title, text)`

    This sets the contents of the specified entry box.

* `.setEntryDefault(title, text)`

    This sets a default value to display in an entry box.  
    Once the user starts typing, it will disappear.  
    The text is centered, shown in a light gray font, and will not be returned by `.getEntry(title)`  

* `.clearEntry(title)`

    This will clear the contents of the specified entry box.

* `.clearAllEntries()`

    This will clear all the entry boxes in the GUI.

* `.setFocus(title)`

    This will put the cursor in the specified entry box, so that the user can start typing without needing to click.

#### Get Entries

* `.getEntry(title)`

    This will return the contents of the spcified entry box.


##Button
A clickable button, that will call a function.  
These are the key to starting an interactive application.  
The GUI is looping, waiting for something to happen.  
A button click is the classic way to start interacting with a GUI.

Whenever any function is called by the GUI, the title of the widget that called it is passed as a parameter.  
That way, multiple widgets can use the same function, but diffrent actions can be performed, depening on the name passed as a parameter.

####Add Buttons

* `.addButton(title, function)`

    Add a single button to the GUI, the text on the button will be the same as the button's title.  
    A function should be specified, which will be called when the button is clicked.

```python
    from rwbatools import gui
    
    def press(btn):                 # the title of the button will be received as a parameter
        print(btn)

    app=gui()
    app.addButton("One", press)     # 3 buttons, each calling the same function
    app.addButton("Two", press)
    app.addButton("Three", press)
    app.go()
```

* `.addButtons(titles, functions)`

    It's possible to add a list of buttons to the GUI.  
    Pass a 1-dimensional or 2-dimensional list, and they will be rendered accordingly.
    A single funciton can be passed, to use for all buttons.
    Or a list of functions can be passed, which MUST correspond to the buttons.

* `.addNamedButton(name, title, function)`

    By default, it's not possible to have two buttons with the same text.  
    If that's required, a named button should be used.  
    This allows a name and title to be set for a button.  
    The name will be displayed on the button, and the title passed to the function.

####Change Buttons

* `.setButton(name, text)`

    This will change the text displayed on a button, but **NOT** the value passed as a paramter to the function.

* `.setButtonImage(title, image)`

    This allows an image to be placed on a button, instead of the usual text.

##RadioButton

A group of round boxes, only one of which can be selected.  
These are great for getting a single value, for a multiple choice question.

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

    Adds a **hyperlink**, that when clicked, will call the spcified function.

* `.addWebLink(title, page)`

    Adds a **hyperlink**, that when clicked, will launch the default browser, and load the page parameter.

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

