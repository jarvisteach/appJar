#Container Options
----
The standard way of using appJar, is simply to place all widgets into a single window.  
Everything is grouped into that single window, and any changes affect everything in that window.  

It's sometimes desirable to group widgets together within a window.  
A number of options are provided to make this easier.  

###Label Frame
----
A way of grouping widgets into a box, with a label at the top of the box.  
Position the *LabelFrame* within the grid, then position widgets inside the *LabelFrame*  
![LabelFrame](img/layouts/labelFrame.png)
```
from appJar import gui

app=gui()

app.startLabelFrame("Login Details")
app.setSticky("ew")
app.setFont(20)

app.addLabel("l1", "Name", 0, 0)
app.addEntry("Name", 0, 1)
app.addLabel("l2", "Password", 1, 0)
app.addEntry("Password", 1, 1)
app.addButtons(["Submit", "Cancel"], None, 2, 0, 2)
app.stopLabelFrame()

app.go()
```

####Start/Stop Label Frames  
* `.startLabelFrame(name)` & `.stopLabelFrame()`  
    Used to start and stop a LabelFrame  
    The specified title will be used as the label for the frame.  

####Set Label Frames  
* `.setSticky(coords)`  
    By default, widgets in the frame will align on the left.  
    If you want to change this, specify a different `sticky` value.  
    For example, `.setSticky("ew")` will cause the widgets to stretch to fit the width, aligning in the centre.  

###Toggle Frame
----
A collapsible container for a group of related widgets.  
By default, the contents of the frame are hidden.  
They can be revealed/hidden again by clicking an associated button.  
![ToggleFrame](img/layouts/1_toggleFrame.png)
![ToggleFrame](img/layouts/2_toggleFrame.png)
```
from appJar import gui

app=gui()
app.setFont(20)

app.startToggleFrame("Options")
app.addCheckBox("Show this")
app.addCheckBox("Show that")
app.addCheckBox("Show the other")
app.setCheckBox("Show that")
app.stopToggleFrame()

app.go()
```
####Start/Stop Toggle Frames  
* `.startToggleFrame(title)`  
* `.stopToggleFrame(title)`  
    Used to start and stop a ToggleFrame.  
    The `title` will be used as the title for the ToggleFrame.  
####Set Toggle Frames  
* `.toggleToggleFrame(title)`  
    Will toggle the state of the specified ToggleFrame.  
* `.disableToggleFrame(title, disabled=True)`  
    Will disable the specified ToggleFrame.  
    If `disabled` is set to False, the ToggleFrame will be re-enabled.  
####Get Toggle Frames  
* `.getToggleFrameState(title)`  
    Will return True if the ToggleFrame is open, else will return False.  

###Paged Window
---
A container that mimics a classic phone based interface.  
It provides **PREVIOUS**/**NEXT** buttons to navigate through a series of pages.  
It has an optional widget title, and shows the current page, in a page counter.  
Keyboard bindings are provided to navigate with arrow key presses. CTRL-arrow will navigate to the beginning/end.  
Events can be bound to page changes, the page can be changed via a funciton call, and the current page number can be queried.  
![PagedWindow](img/layouts/1_pagedWindow.png)
```
from appJar import gui

app=gui()

app.setBg("DarkKhaki")
app.setGeometry(280,400)

app.startPagedWindow("Main Title")
app.startPage()
app.addLabel("l13", "Label 1")
app.stopPage()

app.startPage()
app.addLabel("l21", "Label 2")
app.stopPage()

app.startPage()
app.addLabel("l3", "Label 3")
app.stopPage()

app.startPage()
app.addLabel("l4", "Label 4")
app.stopPage()
app.stopPagedWindow()

app.go()
```
####Start/Stop Paged Windows
* `.startPagedWindow(title)`  
* `.stopPagedWindow()`  
    Used to start and stop a PagedWindow.  
    The `title` will be used in the title section of the widget.  
* `.startPage()`  
* `.stopPage()`  
    Used to start and stop each new page.  
    Navigation, page count, etc are all dealt with automatically.  
####Set Paged Windows
* `.setPagedWindowTitle(title, title)`  
* `.setPagedWindowButtons(title, [buttons])`  
    Used to change the text in the title and buttons.  
    When changing the buttons, two values must be passed in: previous/next.  
* `.setPagedWindowButtonsTop(title, top=True)`  
    Used to position the navigation buttons.  By default, they are at the bottom.  
    Call this funtion to move them to the top.  
* `.setPagedWindowPage(title, pageNum)`  
    Used to display the selected page.  
* `.setPagedWindowFunction(title, function)`  
    Declare a function to call, each time the page is changed.  
* `.showPagedWindowPageNumber(title, show=True)`  
* `.showPagedWindowTitle(title, show=True)`  
    Use these to declare if you want the page title, page numbers to be shown.  
####Get Paged Windows
* `.getPagedWindowPageNumber(title)`  
    Used to get the page number currently being shown.  

###Tabbed Frame
---
A way to create a (basic) tabbed-style interface.  
Position the *TabbedFrame* within the grid, start a *Tab*, then position widgets inside the *Tab*  
![TabbedFrame](img/layouts/tabbedFrame.png)  
```
from appJar import gui

app=gui()

app.startTabbedFrame("TabbedFrame")
app.startTab("Tab1")
app.addLabel("l1", "Tab 1 Label")
app.stopTab()

app.startTab("Tab2")
app.addLabel("l2", "Tab 2 Label")
app.stopTab()

app.startTab("Tab3")
app.addLabel("l3", "Tab 3 Label")
app.stopTab()
app.stopTabbedFrame()

app.go()
```
####Start/Stop Tabbed Frames
* `.startTabbedFrame(name)` & `.stopTabbedFrame()`  
    Used to start & stop the a *TabbedFrame*, with the specified name.  

* `.startTab(name)` & `.stopTab()`  
    Used to start and stop each of the tabs in the *TabbedFrame*.  
    The title for the tab will be the specified *name*.  

####Set TabbedFrame
* `.setTabbedFrameTabExpand(title, expand=True)`  
    By default, the tabs take up the minimum amount of space necessary.  
    Set this to True, to have the tabs fill the entire row.  
![TabbedFrame](img/layouts/2_tabbedFrame.png)  

* `.setTabbedFrameSelectedTab(title, tab)`  
    Select the specified tab in the TabbedFrame.  

* `.setTabbedFrameDisabledTab(title, tab, disabled=True)`  
    Disable the specified tab in the TabbedFrame.  
    Set disabled to False to re-enable it.  
    This will also change the displayed tab, if the disaplyed tab is being disabled.  

* `.setTabbedFrameDisabledAllTabs(title, disabled=True)`  
    Will disable all tabs for the named TabFrame.  
    Or, enable them if disabled is set to False.  

####Changing Colours  
TabbedFrames have a set of colours that can be changed:  

* ActiveFg - Sets the colour of the text in the active tab  
* ActiveBg - Sets the background colour of the active tab  
* InactiveFg - Sets the colour of the text in all inactive tabs  
* InactiveBG - Sets the background colour of all inactive tabs  
* DisabledFg - Sets the colour of the text in all disabled tabs  
* DisabledBg - Sets the background colour of all disabled tabs  
* Bg - Sets the background colour behind the widget - only visible at the end of the tabs  

These are all changed via the standard property changing functions, eg:  

* `.setTabbedFrameBg("t1", "red")`
* `.setTabbedFrameActiveBg("t1", "yellow")`

It is also possible to change the colour of individual panes.  
Call `.setBg("colour")` while adding widgets to the specific pane.  
Or `.setTabBg(title, tab, 'colour')` at other times.  

####Get TabbedFrame
* `.getTabbedFrameSelectedTab(title)`  
    Gets the name of the currently selected tab, for the named TabFrame.  

###Paned Window
---
A way to arrange re-sizable frames, with drag-bars.  

* Call `.startPanedWindow(name)` to create the initial pane  
* Then keep calling it to add additional panes  
* Calling `.setPanedWindowVertical(name)` will change the layout to vertical, allowing more configurations.  
####Horizontal Panes
![Horizontal Panes](img/layouts/pane1.png)  

* Create an initial pane  
* Keep adding panes to the initial pane  
####Vertical Panes
![Vertical Panes](img/layouts/pane2.png)  

* Create an initial pane  
* Make it vertical  
* Add a second pane  
* Keep adding panes to the initial pane  
####E-Pane
![E-Panes](img/layouts/pane3.png)  

* Create an initial pane  
* Add a second pane
* Make the second pane vertical  
* The remaining panes are added to frame 2  
####T-Pane
![T-Panes](img/layouts/pane4.png)  

* Create an initial pane
* Make it vertical
* Add a second pane
* Add the remaining panes to pane 2  

###Sub Window
---
A way to add additional windows, which can be hidden and shown.  
![SubWindow](img/layouts/subWin.png)
```
from appJar import gui

def launch(win):
    app.showSubWindow(win)

app=gui()

app.startSubWindow("one", modal=True)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

app.startSubWindow("two")
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

app.addButtons(["one", "two"], launch)

app.go()
```

####Start/Stop Sub Windows
* `.startSubwindow(name, title=None, modal=False)`  
* `.stopSubwindow()`  
    Used to start and stop defining a *SubWindow*  
    Setting a `title` will override the `name` as a title for the SubWindow. 
    Setting `modal` to True, will prevent the user from interacting with the parent window until the SubWindow is closed.  
####Show/Hide Sub Windows
* `.showSubWindow(title)`  
    Will cause the specified SubWindow to be shown.  
    If it is set as *modal* the parent window will become uninteractive until the SubWindow is closed.  
* `.hideSubWindow(title)`  
    Used to hide the specified *SubWindow*.  
    This will not destroy the SubWindow, so it can be shown again later.  
* `.destroySubWindow(title)`  
    This will hide and permanently destroy the specified SubWindow.  
    It cannot be shown again.  
####Set Sub Windows
Note, all functions available on the main window are also available on Sub Windows.  
Simply call those functions after starting a Sub Window.  
```
app.startSubWindow("one", modal=True)
app.setBg("orange")
app.setGeometry("400x400")
app.setTransparency(25)
app.setStopFunction(checkDone)
app.addLabel("l1", "In sub window")
app.stopSubWindow()
```

#Under Development
---

###Scroll Pane  
---
A scrollable frame, to contain widgets.

* `.startScrollPane(title)`  
* `.stopScrollPane()`  
    Used to start and stop the ScrollPane.  
