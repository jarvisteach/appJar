#Container Options
----
The standard way of using appJar, is simply to place all widgets into a simple window. Everything is grouped into that single window, and and changes affect everything in that window.

It's sometimes desirable to group widgets together within a window. A number of options are provided to make this easier.

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
* `.startLabelFrame(name)`  
* `.stopLabelFrame()`  
    Used to start and stop a LabelFrame  
    The specified title will be used as the label for the frame.  
####Set Label Frames  
* `.setSticky(coords)`  
    By default widgets in the frame will align on the left.  
    If you want to change this, specify a different `sticky` value.  
    For example, `.setSticky("ew")` will cause the widgets to stretch to fit the width, aligning in the centre.  

###Toggle Frame
----
A collapsable container for a group of related widgets.  
By default the contents of the frame are hidded.  
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
    Used to position the navigation buttons.  By default they are at the bottom.  
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
* `.startTabbedFrame(name)`  
* `.stopTabbedFrame()`  
    Used to start & stop the main *TabbedFrame*  
* `.startTab(name)`
* `.stopTab()`  
    Used to start and stop each of the tabs in the *TabbedFrame*.  
####Set TabbedFrame
* `.setTabbedFrameTabExpand(title, expand=True)`  
    By default, the tabs take up the minimum amount of space necessary.  
    Set this to True, to have the tabs fill the entire row.  
![TabbedFrame](img/layouts/2_tabbedFrame.png)  
* `.setTabbedFrameSelectedTab(title, tab)`  
    Select the specified tab in the TabbedFrame.  

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
* Keep adding panes to the inittial pane  
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

#Under Development
---

###Sub Window
---
A way to add additional windows, which can be hidden and shown.  
![SubWindow](img/layouts/subWin.png)

* `.startSubwindow(name)`  
* `.stopSubwindow()`  
    Used to start and stop defining a *SubWindow*  
* `.showSubWindow(name)`  
* `.hideSubWindow(name)`  
    Used to show and hide the specified *SubWindow*  

###Scroll Pane  
---
A scrollable frame, to contain widgets.

* `.startScrollPane(title)`  
* `.stopScrollPane()`  

