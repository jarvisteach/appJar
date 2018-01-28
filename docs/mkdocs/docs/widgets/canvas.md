### Canvas ([beta](https://en.wikipedia.org/wiki/Software_release_life_cycle#BETA))  
---
This lets you embed a canvas in appJar

![Canvas](../img/1_canvas.png)  

```python
from appJar import gui
app=gui()
canvas = app.addCanvas("c1")
canvas.create_oval(10, 10, 100, 100, fill="red", outline="blue", width=3)
canvas.create_line(0, 0, 255, 255, width=5)
canvas.create_line(0, 255, 255, 0, dash=123)
app.go()
```

* `.addCanvas(title)`  
    Creates a canvas widget.  

* `.getCanvas(title)`  
    Gets the specified canvas widget.  

#### Drawing on a Canvas  

* `.addCanvasCircle(title, x, y, diameter, **kwargs)`  
    Draws a circle on the canvas.  

* `.addCanvasOval(title, x, y, xDiam, yDiam, **kwargs)`  
    Draws an oval on the canvas.  

* `.addCanvasRectangle(title, x, y, w, h, **kwargs)`  
    Draws a rectangle on the canvas.  

* `.addCanvasLine(title, x, y, x2, y2, **kwargs)`  
    Draws a line on the canvas.  

* `.addCanvasText(title, x, y, text, **kwargs)`  
    Draws text on the canvas.  

* `.clearCanvas(title)  
    Removes all drawings from the canvas.  
