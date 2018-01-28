##TextArea
____
Similar to an Entry, but allows you to type text over multiple lines.  

![TextArea](../img/1_textArea.png)  

```python
from appJar import gui

app=gui()
app.addTextArea("t1")
app.go()
```

####Add TextAreas
* `.addTextArea(title)`  
    Adds an empty TextArea, with the specified title.  

* `.addScrolledTextArea(title)`  
    Adds a scrollable TextArea with the specified title.  

![ScrolledTextArea](../img/2_textArea.png)  

####Set TextAreas
* `.setTextArea(title, text, end=True, callFunction=True)`  
    Adds the supplied text to the specified TextArea.  
    By default, the text is added to the end.  
    Set `end` to be False if you want to add at the beginning.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.clearTextArea(title, callFunction=True)`  
    Clears the contents of the specified TextArea.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.clearAllTextAreas(callFunction=False)`  
    This will clear the contents of all TextAreas in the app.  
    Set ```callFunction``` to be True, if you want to call any associated functions.  

####Get TextAreas

* `.getTextArea(title)`  
    Gets the contents of the specified TextArea.  

* `.getAllTextAreas()`  
    This will return the contents of all TextAreas in the app, as a dictionary.  
