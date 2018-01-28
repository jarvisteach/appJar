##RadioButton
____
A group of round boxes, only one of which can be selected.  
These are great for getting a single value, for a multiple choice question.  

![Radios](../img/t_radios.png)  

```python
from appJar import gui

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.addRadioButton("song", "Parklife")
app.go()
```

####Add RadioButtons
* `.addRadioButton(title, name)`  
    This will create a RadioButton grouped by the specified title.  
    This button will have the value of name.  
    Radio buttons are usually used in groups.  

####Set RadioButtons
* `.setRadioButton(title, value, callFunction=True)`  
    This will tick the specified RadioButton.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.setRadioTick(title, tick=True)`  
    It is possible to use tick-boxes instead of the classic circular radio-button.  
    Setting tick to True will convert all the radio-buttons for this title to tick boxes.  

* `.clearAllRadioButtons(callFunction=False)`  
    This will reset all RadioButtons in the app to their first value.  
    Set ```callFunction``` to be True, if you want to call any associated functions.  

####Get RadioButtons
* `.getRadioButton(title)`  
    Gets the value of the selected RadioButton, for the specified title.
```python
    from appJar import gui

    def press(rb):
        print(app.getRadioButton("song"))

    app=gui()
    app.addRadioButton("song", "Killer Queen")
    app.addRadioButton("song", "Paradise City")

    # call this function, when the RadioButton changes
    app.setRadioButtonChangeFunction("song", press)

    app.addButton("PLAY", press)
    app.go()
```

* `.getAllRadioButtons()`  
    This will return the contents of all RadioButtons in the app, as a dictionary.  
