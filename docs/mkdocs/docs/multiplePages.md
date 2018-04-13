# Multiple Pages  
---

A common question is how to have different *pages* of widgets in the same GUI.  
There are lots of ways to acheive this...

## Updating Labels  
---

The simplest option is to update the contents of existing widgets.  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]
pos = -1

def press(btn):
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
    app.buttons(["Previous", "Next"], press)
    press("Next")
```

## SubWindows  
---

Create multiple [SubWindows](/pythonSubWindows) and hide/show them as required.  

## PagedWindow  
---

Create a [PagedWindow](/pythonWidgetGrouping/#paged-window) and navigate back and forth between each page.  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4], 
        ["Bart", "Simpson", "America", 14]]

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

Create a [TabbedFrame](/pythonWidgetGrouping/#tabbed-frame) and have each set of widgets under a different tab.  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4], 
        ["Bart", "Simpson", "America", 14]]

with gui("Updating Labels") as app:
    with app.tabbedFrame("Address Book"):
        for pos in range(len(data)):
            with app.tab(str(pos)):
                app.entry(str(pos)+"fName", data[pos][0], label="First Name")
                app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
                app.entry(str(pos)+"country", data[pos][2], label="Country")
                app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")
```

## Overlayed Frames  
---

Create a number of [Frames](/pythonWidgetGrouping/#frame) in the same grid position and `raise()` the required Frame.  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4], 
        ["Bart", "Simpson", "America", 14]]

pos = -1

def press(btn):
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
        with app.frame(str(loop), 0, 0): 
            app.entry(str(loop)+"fName", data[loop][0], label="First Name")
            app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
            app.entry(str(loop)+"country", data[loop][2], label="Country")
            app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")

    app.buttons(["Previous", "Next"], press)
    press("Next")
```

## FrameStacks  
---

Works the same as overlayed frames, but provides extra navigation methods, and automatic placement.  
```python
data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4], 
        ["Bart", "Simpson", "America", 14]]


def press(btn):
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

    app.buttons(["Previous", "Next"], press)
    app.disableButton("Previous")
```

## Hiding/Showing  
---

You can [manipulate widgets](/pythonWidgetOptions/#widget-manipulation) using `hide()` & `show()` to temporarily hide them.  

## Destroying/Recreating
---

You can also [manipulate widgets](/pythonWidgetOptions/#widget-manipulation) using `remove()` or `removeAllWidgets()` and then creating new widgets.  
