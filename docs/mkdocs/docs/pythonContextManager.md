# The power of WITH  
*Using ContextManagers to make GUIs even easier.*  

---

One thing I really wanted to get into appJar, was some indentation - I wanted the code for the GUI to look more like the actual GUI.  

I also wanted to simplify the creation of containers, and even the GUI itself.  

```python
with gui("My first GUI") as app:
    app.addLabel("lab", "Hello world!")
```

**That's it - 2 lines to create a GUI.**  

If you want to add containers, it's the same process:

![Power of With](img/powerOfWith.png)
```python
from appJar import gui
with gui("My first GUI") as app:
    app.setBg("lightblue")

    with app.labelFrame("Left"):
        app.addLabel("left", "Hello world!")

    with app.labelFrame("Right", row=0, column=1):
        app.addLabel("right", "Hello world again!")

    app.addNamedButton("PRESS ME", "Pop-up", app.showSubWindow, colspan=2)

    with app.subWindow("Pop-up"):
        app.addLabel("popLab", "Here's a pop-up!")
```

And, that's all there is to it - this feature is available on all containers, and I think it's going to make things a lot simpler!

The old start/stop functions all still exist, so there is no need to use the `with` command. But if you prefer this method, it's there.  

An added bonus, is that the same syntax works for starting a container or opening a container!

## Available Containers
---

```python
from appJar import gui

def press(btn):
    with app.page(windowTitle="pages", pageNumber=1):
        app.addLabel("newLab", "New Label")

with gui() as app:
    app.setSize(250, 300)
    with app.pagedWindow("pages"):
        with app.page():
            app.addLabel("l1", "Page One")
            app.addButton("PRESS", press)
        with app.page():
            app.addLabel("l2", "Page Two")
        with app.page():
            app.addLabel("l3", "Page Three")
```

The following can all be used in the same format to *start* or *open* a container:  
Have a look on the [containers page](/pythonWidgetGrouping) for usage information.  

* `.frame(title)`  
* `.frameStack(title)`  
* `.labelFrame(title, hideTitle=False)`  
* `.toggleFrame(title)`  
* `.scrollPane(title)`  
* `.tabbedFrame(title)`  
* `.tab(title, tabTitle=None)`  
* `.panedFrame(title)`  
* `.panedFrameVertical(title)`  
* `.pagedWindow(title)`  
* `.page(windowTitle, pageNumber)` - **NB.** only provide the named parameters if *opening* a page  
* `.subWindow(name, title=None, modal=False, blocking=False, transient=False, grouped=True)`  

If you're playing with **ttk**, you can try:  

* `.notebook(title)`  
* `.note(title, tabTitle=None)`  
