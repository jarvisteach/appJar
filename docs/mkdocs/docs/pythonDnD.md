#Drag'n Drop
---
Drag and Drop functionality is something we're accustomed to in most software.  
By default, python and tkinter don't provide it.

We've incorporated a couple of ways to include drag and drop functionality in **appJar**.  

##Drag'n Drop Between Widgets
---
There is a beta version of drag and drop between labels.  

* `.set XXX DragFunction(name, [startDragFunction, stopDragFunction]`)  
    Set functions to call whenever the mouse button is clicked and dragged.  
    The first function will be called when the mouse is initially clicked.  
    The second function will be called when the mouse is released.  

##Drag'n Drop Between Applications
---
There is also a beta version of drag and drop between applications - at the moment, this is has been seen to work on Mac OSX and Windows 7 - let us know of success on other versions of Windows!  

Certain widgets can be registered to receive *Drop* events:  

* `.setEntryDropTarget(title, function=None, replace=True)`  
* `.setTextAreaDropTarget(title, function=None, replace=True)`  
* `.setImageDropTarget(title, function=None, replace=True)`  
* `.setLabelDropTarget(title, function=None, replace=True)`  

Then, if you drag a file or a URI onto one of these widgets, the filename/URI will be copied.  

If no function has been set, the contents of the widget will be replaced with the filename/URI.  
If you'd rather append the URI/filename - set `replace` to be False.  
If a function has been set, it will be called, passing in the filename/URI as the only paramter.  

There is currently no support for registering *Drag* events.  

##Beta
---
Note, this is all in beta - long term, the plan is to combine all of this into one set of functions, and provide a unified drag and drop model, that will work across all widgets both within the application and between applications.  
