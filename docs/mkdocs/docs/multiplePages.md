# Multiple Pages  
---

A common question is how to have different *pages* of widgets in the same GUI.  
There are lots of ways to acheive this.  

All of the below are using a 2D list of data:  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4], 
        ["Bart", "Simpson", "America", 14]]
```

## Updating Labels  
---

One option is to reuse the existing widgets, and change their contents.  
This involves creating a single set of widgets, and then calling a function to change their contents:  

```python
pos = -1

def changeCharacter(btn):
    global pos 
    if btn == "Next": pos += 1
    elif btn == "Previous": pos -= 1

    if pos == 0:
        app.disableButton("Previous")
    elif pos == len(data)-1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

    app.entry("First Name", data[pos][0])
    app.entry("Last Name", data[pos][1])
    app.entry("Country", data[pos][2])
    app.entry("Age", data[pos][3])

with gui("Updating Labels") as app:
    app.entry("First Name", label=True)
    app.entry("Last Name", label=True)
    app.entry("Country", label=True)
    app.entry("Age", kind='numeric', label=True)
    app.buttons(["Previous", "Next"], changeCharacter)
    changeCharacter("Next")
```

## PagedWindow  
---

[PagedWindows](/pythonWidgetGrouping/#paged-window) were introduced to allow easy navigation through multiple *pages* of similar data - think address books or music collections. They provide navigation buttons, a title and a page number:  

```python
with gui("Updating Labels") as app:
    with app.pagedWindow("Address Book"):
        for pos in range(len(data)):
            with app.page():
                app.entry(str(pos)+"fName", data[pos][0], label="First Name")
                app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
                app.entry(str(pos)+"country", data[pos][2], label="Country")
                app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")
```

## TabbedFrames  
---

[TabbedFrames](/pythonWidgetGrouping/#tabbed-frame) are another common way of presenting multiple pages of data in a single widget:  

```python
with gui("Updating Labels") as app:
    with app.tabbedFrame("Address Book"):
        for pos in range(len(data)):
            with app.tab(data[pos][0]):
                app.entry(str(pos)+"fName", data[pos][0], label="First Name")
                app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
                app.entry(str(pos)+"country", data[pos][2], label="Country")
                app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")
```

## Overlayed Frames  
---

A clever trick for solving this problem is to group your widgets in a [Frame](/pythonWidgetGrouping/#frame), and then have multiple frames in the same place.  
Frames are not transparent, so only the last added frame will be visible.  
It's possible to then *raise* another frame to the top. This works well, but requires keeping track of the frame:

```python
pos = -1

def changeCharacter(btn):
    global pos 
    if btn == "Next": pos += 1
    elif btn == "Previous": pos -= 1

    if pos == 0:
        app.disableButton("Previous")
    elif pos == len(data)-1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

    app.raiseFrame(str(pos))

with gui("Updating Labels") as app:
    for loop in range(len(data)):
        with app.frame(str(loop), 0, 0):  # put all the frames in grid pos 0,0
            app.entry(str(loop)+"fName", data[loop][0], label="First Name")
            app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
            app.entry(str(loop)+"country", data[loop][2], label="Country")
            app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")

    app.buttons(["Previous", "Next"], changeCharacter)
    changeCharacter("Next")
```

## FrameStacks  
---

To take away some of the work from the above option, we created [FrameStacks](/pythonWidgetGrouping/#frame-stack).  
They provide extra functions for navigating, and checking which *Frame* is being displayed:  

```python
def changeCharacter(btn):
    if btn == "Next": app.nextFrame("address book")
    elif btn == "Previous": app.prevFrame("address book")

    if app.frameStackAtStart("address book"):
        app.disableButton("Previous")
    elif app.frameStackAtEnd("address book"):
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

with gui("Updating Labels") as app:
    with app.frameStack("address book", start=0):
        for loop in range(len(data)):
            with app.frame():
                app.entry(str(loop)+"fName", data[loop][0], label="First Name")
                app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
                app.entry(str(loop)+"country", data[loop][2], label="Country")
                app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")

    app.buttons(["Previous", "Next"], changeCharacter)
    app.disableButton("Previous")
```

## Hiding/Showing  
---

Instead of putting multiple frames in the same grid cell, you can have them in different rows, and [hide them](/pythonWidgetOptions/#widget-manipulation):  
```python
def showCharacter(btn):
    for pos in range(len(data)):
        if data[pos][0] == btn:
            app.showFrame(str(pos))
        else:
            app.hideFrame(str(pos))
                
with gui("Updating Labels") as app:
    for loop in range(len(data)):
        with app.frame(str(loop)):
            app.entry(str(loop)+"fName", data[loop][0], label="First Name")
            app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
            app.entry(str(loop)+"country", data[loop][2], label="Country")
            app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")
        app.hideFrame(str(loop))

    app.buttons([d[0] for d in data], showCharacter)
    showCharacter("Homer")
```

## Destroying/Recreating
---

An alternative to the above is to be a bit more aggresive and [*destroy* & *recreate*](/pythonWidgetOptions/#widget-manipulation) your widgets each time.  
This can be less efficient in terms of time, but more efficient in terms of memory...  
```python
def showCharacter(btn):
    for pos in range(len(data)):
        if data[pos][0] == btn:
            app.removeAllWidgets()
            makeCharacter(pos)

def makeCharacter(pos):
    with app.frame("character", 0, 0): 
        app.entry("fName", data[pos][0], label="First Name")
        app.entry("lName", data[pos][1], label="Last Name")
        app.entry("country", data[pos][2], label="Country")
        app.entry("age", data[pos][3], kind='numeric', label="Age")
    app.buttons([d[0] for d in data], showCharacter)
        
# just call the function to make the widgets in the main GUI
with gui("Updating Labels") as app:
    makeCharacter(0)
```

## SubWindows  
---

Finally, you could try creating [SubWindows](/pythonSubWindows) for each set of widgets.  

```python
with gui("Updating Labels") as app:
    for pos in range(len(data)): # create the hidden subWindows
        with app.subWindow(data[pos][0]):
            app.entry(str(pos)+"fName", data[pos][0], label="First Name")
            app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
            app.entry(str(pos)+"country", data[pos][2], label="Country")
            app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")

    # this is in the main GUI
    app.label("Pick a Character")
    app.buttons([d[0] for d in data], app.showSubWindow)
```
