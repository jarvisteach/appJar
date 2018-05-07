# appJar  
*The easiest way to create GUIs in Python.*  

---

Written by a teacher, in the classroom, for students.  

**appJar** is designed to run on as many versions of [Python](https://www.python.org/downloads/) as possible - so it should work in your school.  

There are no other dependencies - simply [download](https://github.com/jarvisteach/appJar/blob/appJar/releases/appJar.zip?raw=true), unzip, and put it in your code folder.  
Check out the [installation](/Install) instructions for other ways to get **appJar** working.  

### Hello appJar  
---

[GUIs](https://en.wikipedia.org/wiki/Graphical_user_interface) in **appJar** require three steps.  

* First, import the library & create a GUI variable.  
    (from now on, we do everything to the GUI variable)  

```python
# import the library
from appJar import gui
# create a GUI variable called app
app = gui()
```

* Then, using the gui variable, add and configure an output widget:  
    (if you've tried [turtle](https://docs.python.org/3.6/library/turtle.html) this will all look very familiar)  

```python
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
```

* Finally, start the GUI:  
    (**NB.** don't put any code after this line)  

```python
# start the GUI
app.go()
```

* And, that's it: 

    ![simpleApp](img/simpleApp.png)  

### Interactivity    
---
Of course, the whole point of making a GUI, is to be interactive - this requires **events**.  

The idea behind [event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming) is that each time the user clicks or types (an event) the GUI should respond.  

* So, we add some input widgets ([Entry Boxes](/inputWidgets/#entry)), for the user to type in:

```python
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
```

* Then, we need a **function** - a block of code to call, when an event happens:  

```python
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
```


* Finally, a [button](/inputWidgets/#button) to create the event:  

```python
# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)
```

* We now have an interactive GUI:  

    ![testLog](img/testLog.png)

When the user presses a button, the `press` function is called, passing the name of the button as a parameter.  

### Appearance counts
---
We also want to change the way the [GUI looks](/pythonGuiOptions):  

* For starters, you can specify a name and size for your GUI, when you create it:  

```python
app = gui("Login Window", "400x200")
```

* You can change the general appearance of the GUI:  

```python
app.setBg("orange")
app.setFont(18)
```

* You can even specify where you want the cursor to be when the GUI starts:  

```python
app.setFocus("Username")
```

* It now looks a bit better:  

    ![testLog](img/testLog2.png)  

    (**NB.** We also set the fg/bg colours on the label - see [below](#full-code-listing)) 

###  Make your own  
---  

And, that's all you need to know. Check out:  

* All the different [input widgets](/inputWidgets) & [output widgets](/outputWidgets) available.  
* Our support for [images](/pythonImages) and [sound](pythonSound).  
* How to include [toolbars, menubars & statusbars](/pythonBars).  
* How to create simple [pop-ups](/pythonDialogs).  
* How to use a [grid layout](/pythonWidgetLayout).  
* How to use [containers](/pythonWidgetGrouping) for more advanced layouts.  

### Full code-listing  
---  

Below is the full code-listing for the above GUI:  

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

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

# start the GUI
app.go()
```

### Upcoming in v1.0  
---

In the upcoming 1.0 release, we're formally introducing a new set of options for buiding your GUI.  

These are targetted at our more experienced users:  

* [Context Managers](/pythonContextManager) allow you to create the GUI and any containers, in a visibly more understandable way.  
* New [functions](/simpleAppJar) that allow you to add/get/set widgets all with the same command, including passing configuration paramters.  
* New [properties](/simpleProperties) for configuring the GUI.  

Most of these are already live, and can be used, reducing the above GUI code to:  

```python
from appJar import gui 

def press():
    print("User:", app.entry("Username"), "Pass:", app.entry("Password"))

with gui("Login Window", "400x200", bg='orange', font={'size':18}) as app:
    app.label("Welcome to appJar", bg='blue', fg='orange')
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.buttons(["Submit", "Cancel"], [press, app.stop])
```
