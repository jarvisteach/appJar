#Grouping Widgets
---
Once you have got to grips with laying out your widgets, it is possible to group them together.  
Each of these groups is treated like an individual widget.  
When you **START** the group, you place it in a cell in your layout.  
Then, when you place widgets inside the group, you start a new grid.  
After you **STOP** the group, you go back to your previous grid layout.  
Three main styles are currently supported:

###LabelFrame
---
Will put a border around the widgets, with a title

* `.startLabelFrame(title)`
* `.stopLabelFrame()`
* `.setLabelFrameAnchor(title, anchor)`

![LabelFrame](img/10_lf_layout.png)

###NoteBook
---
Will create a tabbed interface, with a number of pages

* `.startNoteBook(note)`
* `.startNoteTab(tab)`
* `.stopNoteTab()`
* `.stopNoteBook()`
* `.setNoteTab(note, tab)`
* `.setNoteBookBg(note, active, inactive)`
* `.setNoteBookFg(note, active, inactive)`
* `.setNoteTabBg(note, tab, bg)`

![NoteBook](img/11_nb_layout.png)

###PanedWindow
---
Will create a split view, with draggable panes

* `.startPanedWindow(title)`
* `.stopPanedFrame()`
* `.setPanedWindowVertical(title)`

###SubWindow
---
Allows the creation of additional windows.
The window is hidden until `.showSubWindow(title)` is called.

* `.startSubWindow(name, title=None)`
* `.stopSubWindow()`
* `.showSubWindow(title)`
* `.hideSubWindow(title)`
* `.destroySubWindow(title)`
