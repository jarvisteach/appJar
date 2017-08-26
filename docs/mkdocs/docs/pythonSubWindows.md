# Sub Window  
---  
A way to add additional windows, which can be hidden and shown.  

![SubWindow](img/layouts/subWin.png)

```python
from appJar import gui 

def launch(win):
    app.showSubWindow(win)

app=gui()

# this is a pop-up
app.startSubWindow("one", modal=True)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

# this is another pop-up
app.startSubWindow("two")
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

# these go in the main window
app.addButtons(["one", "two"], launch)

app.go()
```

#### Start/Stop Sub Windows  
* `.startSubwindow(name, title=None, modal=False, transient=False, blocking=False)` & `.stopSubwindow()`  
    Used to start and stop defining a *SubWindow*  
    Setting a `title` will override the `name` as a title for the *SubWindow*.  
    Setting `modal` to True, will prevent the user from interacting with the parent window until the *SubWindow* is closed.  
    Setting `transient` to True, will cause the *SubWindow* to respond to parent window events such as hide, show & move.  
    Setting `blocking` to True, will stop execution of your code once the *SubWindow* is shown, until the user closes it.  

* `.openSubWindow(title)`  
    Used to reopen the named *SubWindow*.  
    This lets you modify SubWindows in a different part of the code, for example in a function call.  

#### Show/Hide Sub Windows  

* `.go(startWindow=None)`  
    If you set a *SubWindow* as the ```startWindow``` *appJar* will start-up showing the named *SubWindow*.  
    The main window will be minimized.  

* `.showSubWindow(title)`  
    Will cause the specified *SubWindow* to be shown.  
    If it is set as *modal* the parent window will become uninteractive until the *SubWindow* is closed.  

* `.hideSubWindow(title)`  
    Used to hide the specified *SubWindow*.  
    This will not destroy the *SubWindow*, so it can be shown again later.  

* `.destroySubWindow(title)`  
    This will hide and permanently destroy the specified *SubWindow*.  
    It cannot be shown again.  

It's useful to be able to create a button that stops a SubWindow:  
If you define a button, that calls `.hideSubWindow()` or `.destroySubWindow()`, and give it the same name as the *SubWindow*, then it will hide/destroy the *SubWindow*, and call any associated `.stopFunction()`.  

```python
app.startSubWindow("Demo")
app.addLabel("l1", "Press the button to close this window")
# set the button's name to match the SubWindow's name
app.addNamedButton("CLOSE", "Demo", app.hideSubWindow)
app.stopSubWindow()
```

#### Set Sub Windows  
Note, all functions available on the main window are also available on *SubWindows*.  
Simply call those functions after starting a *SubWindow*.  

```python
app.startSubWindow("one", modal=True)
app.setBg("orange")
app.setGeometry("400x400")
app.setTransparency(25)
app.setStopFunction(checkDone)
app.addLabel("l1", "In sub window")
app.stopSubWindow()
```
