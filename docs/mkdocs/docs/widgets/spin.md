##SpinBox
____
A scrollable list of options. Up and down buttons are provided to scroll from one item to the next.  
Unlike the OptionBox, you do not get a drop-down of choices, instead it spins to the next/previous option.  

![SpinBox](../img/1_spinBox.png)  

```python
from appJar import gui

app=gui()
app.setFont(20)
app.addLabelSpinBox("options", ["Apple", "Orange", "Pear", "kiwi"])
app.go()
```

####Add SpinBoxes
* `.addSpinBox(title, values)`  
    This will create a SpinBox, adding the contents of the values list, in the order specified.

* `.addSpinBoxRange(title, from, to)`  
    This will create a SpinBox, with a numeric range of items.  

    ![SpinBox](../img/3_spinBox.png)  

```python
    from appJar import gui

    app=gui()
    app.setFont(20)
    app.addSpinBoxRange("Numbers", 1, 12)
    app.go()
```

####Set SpinBoxes
* `.setSpinBox(title, value, callFunction=True)`  
    This will select the specified value in the SpinBox.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.setSpinBoxPos(title, pos, callFunction=True)`  
    This will select the value at the specified position in the SpinBox.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.clearAllSpinBoxes(callFunction=False)`  
    This will set all SpinBoxes in the app to their first value.  
    Set ```callFunction``` to be True, if you want to call any associated functions.  

####Get SpinBoxes

* `.getSpinBox(title)`  
    This will get the selected value from the specified SpinBox.  

* `.getAllSpinBoxes()`  
    This will return the contents of all SpinBoxes in the app, as a dictionary.  
