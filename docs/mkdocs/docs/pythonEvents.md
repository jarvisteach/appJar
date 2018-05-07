# Events  
---
An [event](https://en.wikipedia.org/wiki/Event-driven_programming) is just calling a function - you want an event to be generated every time the user does something, such as clicking a button, dragging a scale, or pressing a key...  

The `Button` has an event automatically linked to it - whenever you press it, a function gets called. The other widgets don't.  


## Built-in Events  
---
appJar currently has four basic types of event you can register:  

* `.set XXX ChangeFunction(title, function)` call a function whenever the widget *changes*  
* `.set XXX SubmitFunction(title, function)` call a function when the widget is *submitted*    
* `.set XXX OverFunction(title, functions)` call function(s) when the mouse *enters/leaves* the widget  
* `.set XXX DragFunction(title, functions)` call function(s) when the mouse is *dragged in/out* of the widget  

### Change & Submit Events  
These do similar things, so probably shouldn't both exist, but have evolved from a single `.set XXX Function()` which is now deprecated.  

* `.set XXX ChangeFunction(title, function)`  
    Bind the specified function to the named widget:  
    * Scales, OptionBoxes, SpinBoxes, ListBoxes, RadioButtons & CheckBoxes, Entries & TextAreas, and Properties - the function will be called each time the widget is changed.  
    * Buttons, Labels & Images - it is not available.  
    * Other widgets - it will set the *command* property for the underlying tkinter widget; this may or may not do anything...  
<br>

* `.set XXX SubmitFunction(title, function)`  
    Creates a *submit* option for some widgets:  
    * Labels & Images - it binds a function to the ```<Left-Mouse-Button>```, making the widget clickable.  
    * Entries & Buttons - it binds a function to the ```<Enter>``` key  
    * TextAreas - it's not available
    * Other widgets - it does the same as `ChangeFunction`  

```python
from appJar import gui

def songChanged(rb):
    print(app.getRadioButton(rb))

def reset(btn):
    # set back to the default, but don't call the change function
    app.setRadioButton("song", "Killer Queen", callFunction=False)

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.setRadioButtonChangeFunction("song", songChanged)
app.addButton("Reset", reset)
app.go()
```

**WARNING** - it's possible to generate a RuntimeError. If you've got two widgets changing the same variable, say a Scale and a SpinBox, and you want a change in one widget to cause an update in the other, you might inadvertently end up stuck in a recursive loop, until the [stack overflows](https://en.wikipedia.org/wiki/Stack_overflow).  

In this case, make sure you set the optional parameter ```callFunction = False``` when you  call the ```set XXX Function()``` of a widget.  


### Over Events  
---
Set functions to call whenever the mouse enters (goes over) or leaves the specified widget.  

* `.set XXX OverFunction(name, [inFunction, outFunction])`  
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

* `.setImageMouseOver(title, image)`  
    Additional function, specific to [images](/pythonImages/#change-images), to change the specified image, while the mouse is over it.

### Drag Events  

Set functions to call when the mouse button is clicked and dragged on a Label, then released.  

* `.set XXX DragFunction(name, [startDragFunction, stopDragFunction])`  
    The named Label will be the only one that can start a drag event.  
    The first function will be called when the mouse is initially clicked on the Label.  
    The second function will be called when the mouse is released, this can happen anywhere.  
    The same rules for passing functions apply as above.  

## Registering Other Events  

It's possible to register any of the other [tkinter event types](http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm) with appJar widgets.  
Just get the widget, then call the tkinter `bind()` function, passing in the event name and function to call.  
**NB.** The function you register must receive a single parameter, the event object.  

```python
# either grab the widget when it's created, and bind the event
ent = app.addEntry("e1")
ent.bind("<FocusOut>", function_name, add="+")

# or do the above in one line
app.addEntry("e1").bind("<FocusOut>", function_name, add="+")

# or, if doing later on, get the widget from appJar and bind the event
ent = app.getEntryWidget("e1")
ent.bind("<FocusOut>", function_name, add="+")

# or do the above in one line
app.getEntryWidget("e1").bind("<FocusOut>", function_name, add="+")
```

## Binding Keys
---
We also sometimes want keys to trigger events.  
The classic example is the ```<Enter>``` key, we often want to be able to hit the ```<Enter>``` key to submit a form...

* `.enableEnter(function)`  
Link a function to the ```<Enter>``` key

* `.disableEnter()`  
Unlink a function from the ```<Enter>```  key

You may also want to bind other keys to events.  
See [here](http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm) for a detailed list of the *Event Formats*.  

```python
from appJar import gui
def keyPress(key):
    if key == "<Up>":
        app.increaseFont()
    elif key == "<Down>":
        app.decreaseFont()
    elif key == "<F1>":
        app.setFont(12)

app = gui("Button Demo")
app.addLabel("title", "Press the arrow keys to change the font")
app.bindKey("<Up>", keyPress)
app.bindKey("<Down>", keyPress)
app.bindKey("<F1>", keyPress)
app.go()
```

* `.bindKey(key, function)`  
Link the specified key to the specified function.

* `.bindKeys(keys, function)`  
Link the specified keys to the specified function.

* `.unbindKey(key)`  
Unlink the specified key from any functions bound to it.

* `.unbindKeys(keys)`  
Unlink the specified keys from any functions bound to them.

## Starting the GUI
---

If you want to call a function once the GUI starts, you can register it with the following call:  

* `.setStartFunction(function)`  
    Set a function to call when the GUI starts up.  

## Stopping the GUI
---
Usually the user just presses the **close icon** to stop the GUI.  
However, you might want to let them do it in other ways - maybe by pressing a button...  

To stop the GUI, simply call `app.stop()`  

If you want to add a feature to confirm the user really wants to exit, or to save some data, then you'll need a **stop function**.  

* `.setStopFunction(function)`  
    Set a function to call, before allowing the GUI to be stopped.  
    This function should return True/False to confirm if the GUI should stop.  

```python
def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

app.setStopFunction(checkStop)
```

If you have a **LOT** of widgets (maybe a Table with hundreds of rows), stopping the GUI can take a while...  
In which case, you should enable `fastStop` on the GUI.  
**NB.** this doesn't work from IDLE.  

```python
app.setFastStop(True)
```
