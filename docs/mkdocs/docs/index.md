# appJar  
*The easiest way to create GUIs in Python.*  

---

Written by a teacher, in the classroom, for students.  

**appJar** is designed to run on as many versions of [Python](https://www.python.org/downloads/) as possible - so it should work in your school.  

There are no other dependencies - simply [download](https://github.com/RWBA/appJar/blob/appJar/releases/appJar.zip?raw=true), unzip, and put it in your code folder.  
Check out the [installation](/install) instructions for other ways to get **appJar** working.  

GUIs in Python are hard, there's a huge amount of [boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code) required to get things working - so we hide all that.  
We're also not big fans of lots of parameters, so we keep them to a minimum, instead giving functions to get & set most things.  

### Hello World  
---

[GUIs](https://en.wikipedia.org/wiki/Graphical_user_interface) in **appJar** require three steps.  

* Import the library & create a GUI variable.  
    ( From now on, we do everything to the GUI variable. )  

```python
# import the library
from appJar import gui
# create the GUI
app = gui()
```

* Add and configure some widgets:  
    ( If you've tried [turtle](https://docs.python.org/3.6/library/turtle.html) this will all look very familiar. )  

```python
# add & configure widgets
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
```

* Start the GUI:  
    ( **NB.** don't put any code after this line! )  

```python
# start the GUI
app.go()
```

* And, that's it: 

    ![simpleApp](img/simpleApp.png)

### Interactivity    
---
Of course, the whole point of making a GUI, is to be interactive - this requires **events**.  

The idea behind [event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming) is that each time the user clicks, presses or drags something (the event) the GUI should respond.  

* This requires making a function - a block of code to call, when the event happens:  

```python
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
```

* Then add some more widgets, for the user to interact with:

```python
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
```

* And, widgets to create events:  

```python
# give the name of the function - press
app.addButtons(["Submit", "Cancel"], press)
```
* We now have an interactive GUI: 

    ![testLog](img/testLog.png)


Now, when the user presses a button, the `press()` function is called, passing the name of the button as a parameter.  

### Appearance counts
---
As well as changing widgets, you can also change the way the [GUI looks](/pythonGuiOptions).  

For starters, you can specify a name and size for your GUI when you make it:  

```python
app = gui("Login Window", "400x200")
```

And, change the general appearance:  

```python
app.setBg("orange")
app.setFont(18)
```

You can even specify where you want the cursor to be when the user starts typing:

```python
app.setFocus("Username")
```

![testLog](img/testLog2.png)

( **NB.** We also set some other colours on the label - see [below](#full-code-listing). )  

###  Make your own  
---  
And, that's all you need to know. Check out:  

* All the different [widgets](/pythonWidgets) available.  
* Our support for [images](/pythonImages) and [sound](pythonSound).  
* How to include [toolbars, menubars & statusbars](/pythonBars).  
* How to create simple [pop-ups](/pythonDialogs).  
* How to use a [grid layout](/pythonWidgetLayout).  
* How to use [containers](/pythonWidgetGrouping) for more advanced layouts.  

### Full code-listing  
---  

Below is the full code-listing created on this page:  

```python
# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

# create the GUI
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
# give the name of the function - press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

# start the GUI
app.go()
```
