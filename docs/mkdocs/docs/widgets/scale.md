##Scale
____
A slider, that has a minimum & maximum value.  

![Scale](../img/1_scale.png)  

```python
from appJar import gui

app=gui()
app.setFont(20)
app.addLabelScale("scale")
app.go()
```

####Add Scales
* `.addScale(title)`  
    Adds a horizontal scale, with a default range between 0 and 100.  

####Set Scales
* `.setScale(title, pos, callFunction=True)`  
    Sets the selected pos for the specified Scale.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.setScaleRange(title from, to, curr=None)`  
    Allows you to change the range available in the Scale.  
    If ```curr``` is provided, then the Scale will be set to that value.  

* `.setScaleIncrement(title, increment)`  
    Configures how much the scale jumps, when the trough is clicked.  
    It defaults to 10%.  

* `.showScaleIntervals(title, intervals)`  
    Configures the Scale to show interval labels along its length.  
    `intervals` should be how often to show a value, eg. `25` would show 0, 25, 50, and so on...  
    ![Scale](../img/4_scale.png)  

* `.showScaleValue(title, show=True)`  
    Configures the Scale to show the currently selected value.  
    ![Scale](../img/2_scale.png)  

* `.setScaleHorizontal(title)` & `.setScaleVertical(title)`  
    Changes the Scale's orientation to the specified value.  

    ![Scale](../img/3_scale.png)  

* `.setScaleWidth(title, width)` & `.setScaleLength(title, length)`  
    Sets a width/length for the scale's slider.  

* `.setScaleChangeFunction(title, func)`  
    Sets a function to call, each time the scale is changed.  
    The function must take one parameter, which will be populated with the scale's title.  

* `.clearAllScales(callFunction=False)`  
    This will set all Scales in the app to their minimum value.  
    Set ```callFunction``` to be True, if you want to call any associated functions.  

####Get Scales

* `.getScale(title)`  
    Gets the currently selected value from the scale.  

* `.getAllScales()`  
    This will return the contents of all Scales in the app, as a dictionary.  
