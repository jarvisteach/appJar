#Drag'n Drop
---
Drag and Drop functionality is something we're accustomed to in most software.  
By default, python and tkinter don't provide it.

We've incorporated a couple of ways of including drag and drop functionality in **appJar**.  

##Drag'n Drop Between Widgets
---
There is a beta version of drag and drop between labels.  

* `.set XXX DragFunction(name, [startDragFunction, stopDragFunction]`)  
    Set functions to call whenever the mouse button is clicked and dragged.  
    The first function will be called when the mouse is initially clicked.  
    The second function will be called when the mouse is released.  

##Drag'n Drop Between Applications
---
There is also a beta version of drag and drop between applications - at the moment, this is only working on Mac OSX.  

**Entries** and **TextAreas** have been registered to receive *Drop* events automatically.  
If you drag a file from the *Finder* or a URI form *Safari* onto either widget, then the filename/URI will be copied.  

If you set a function to receive the dnd event:  

* `.setEntryDndFunction(title, function)`  
* `.setTextAreaDndFunction(title, function)`  

Then the filename/URI will be passed to your function.  
Otherwise, the filename/URI will be pasted into the **Entry**/**TextArea**.  

There is currently no support for registering *Drag* events.  

##Beta
---
Note, this is all in beta - long term, the plan is to combine all of this into one set of functions, and provide a unified drag and drop model, that will work across all widgets both within the application and between applications.  
