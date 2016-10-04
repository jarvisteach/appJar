#Events  
---
It's possible to call functions when the user performs certain actions.  
It's also possible to configure functions to be called automatically, in a loop.  

###Widget Interaction
----
The following allow widgets to be interacted with:

* `.set XXX Function(name, value, key=None)`  
    This binds a function to the widget.  
    The function will be called every time an interactive-widget changes.  
    The function will be called when some widgets are clicked.  

```python
from appJar import gui

def songChanged(rb):
    print(app.getRadioButton(rb))

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.setRadioButtonFunction("song", songChanged)
app.go()
```

* `.set XXX OverFunction(name, values)`  
    Set functions to call whenever the mouse enters (goes over) or leaves the specified widget.  
    The first function is called when the mouse first enters the widget.  
    The second function is called when the mouse leaves the widget.  
    If you only want a function to be called when the mouse leaves the widget, pass an array like: `[None, leave]`  

```python
    from appJar import gui

    def enter(wdgt): 
        print("IN", wdgt)
    def leave(wdgt):
        print("OUT", wdgt)

    app=gui()
    app.addLabel("l1", "Testing...")
    app.setLabelOverFunction("l1", [enter, leave])
    app.go()
```  
* `.set XXX DragFunction(name, values)`  
    Set functions to call whenever the mouse button is clicked and dragged.  
    The first function will be called when the mouse is initially clicked.  
    The second function will be called when the mouse is released.  
    The same rules for passing functions apply as above.  

###GUI Interaction
----
####Repeated Events
When you start the GUI, it kicks off an infinte loop that is waiting for the user to do something.  
That means, you should never have your own loops running, as that will stop the GUI from working properly.  
Instead, if you want your own loop to run, you need to ask the GUi to run it for you:  

* `.registerEvent(func)`  
Pass this a function, and the GUI will call that function every second.

* `.setPollTime(time)`  
If you want your events to be called more or less frequently, set the frequency here.

####Enter Key
* `.enableEnter(func)`  
Link a function to the `<Enter>` key

* `.disableEnter()`  
Unlink a function form the `<Enter>`  key

####Other Keys
* `.bindKey(key, func)`  
Link the specified key to the specified function.

* `.unbindKey(key)`  
Unlink the specified key from any functions bound to it.
