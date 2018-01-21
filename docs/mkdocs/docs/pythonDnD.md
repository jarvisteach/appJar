#Drag'n Drop
---
Drag and Drop functionality is something we're accustomed to in most software.  
By default, python and tkinter don't provide it.

We've incorporated a couple of ways to include drag and drop functionality in **appJar**.  

##Drag'n Drop Between Widgets
---
There is a beta version of drag and drop **between labels**.  

* `.set XXX DragFunction(name, [startDragFunction, stopDragFunction]`)  
    Set functions to call when the mouse button is dragged from the named widget, or released over any widget.  
    The first function will be called when the mouse is initially dragged.  
    The second function will be called when the mouse is released.  

```python
from appJar import gui

def drag(widget):
    print("Dragged from:", widget)

def drop(widget):
    print("Dropped on:", widget)

app = gui("dnd Demo")

app.setFont(20)
app.setBg("SlateGrey")
app.setFg("yellow")

app.addLabel("dragLab", "Drag Me")
app.addHorizontalSeparator()
app.addLabel("dropLab", "Drop Here")

app.setLabelDragFunction("dragLab", [drag, drop])

app.go()
```

---
<div style='text-align: center;'>
*Advertisement&nbsp;<sup><a href="/advertising">why?</a></sup>*
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
    style="display:block"
    data-ad-format="fluid"
    data-ad-layout-key="-gw-13-4l+6+pt"
    data-ad-client="ca-pub-6185596049817878"
    data-ad-slot="5627392164"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
---

##Drag'n Drop Between Applications
---
There is also a beta version of drag and drop between applications - at the moment, this has been seen to work on Mac OSX 10.11, Raspberry Pi, and Windows 7 & 10 - let us know of success on other distributions!  

```python
from appJar import gui

def externalDrop(data):
    print("Data dropped:", data)

app = gui("External dnd Demo")

app.setFont(20)
app.setBg("SlateGrey")
app.setFg("yellow")

app.addLabel("dropLab", "Drop Here")
app.setLabelDropTarget("dropLab", externalDrop)

app.go()
```


Only certain widgets can be registered to receive *Drop* events:  

* `.setEntryDropTarget(title, function=None, replace=True)`  
* `.setTextAreaDropTarget(title, function=None, replace=True)`  
* `.setImageDropTarget(title, function=None, replace=True)`  
* `.setLabelDropTarget(title, function=None, replace=True)`  
* `.setMessageDropTarget(title, function=None)`  
* `.setListBoxDropTarget(title, function=None, replace=True)`  

Then, if you drag a file or a URI onto one of these widgets, the filename/URI will be copied.  
Or, if it's an image, the image will be replaced.  

If no function has been set, the contents of the widget will be replaced with the filename/URI.  
If you'd rather append the URI/filename - set `replace` to be False.  
If a function has been set, it will be called, passing in the filename/URI as the only parameter.  

There is currently no support for registering *Drag* events.  

* `.set XXX DragSource(title, function=None)`  

##Beta
---
**NB.** This is all in beta - long term, the plan is to combine all of this into one set of functions, and provide a unified drag and drop model, that will work across all widgets both within the application and between applications.  
