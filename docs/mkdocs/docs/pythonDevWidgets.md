#Beta Widgets  
----
The following widgets are in [beta](https://en.wikipedia.org/wiki/Software_release_life_cycle#BETA) - they're available and being used, they're just not quite finished...  

###MicroBit Emulator  
---  
Widget to emulate a [MicroBit](http://microbit.org)

![MicroBit Emulator](img/mb.png)

```python
from appJar import gui

app = gui()
app.addMicroBit("mb1")
app.setMicroBitImage("mb1", "09090:90909:90009:09090:00900")
app.go()
```

####Add MicroBits
* ```.addMicroBit(title)```  
    Will create a 5x5 grid emulating the MicroBit LEDs.  

####Set MicroBits
* ```.setMicroBitImage(title, image)```  
    This sets each pixel to the specified brightness (0 to 9).  
    Each set of 5 digits represents a row of pixels, from top to bottom.  

* ```.setMicroBitPixel(title, x, y, brightness)```  
    Will set the brightness of the specified pixel.  
    ```x``` & ```y``` should be between 0 & 4.  
    ```brightness``` should be a value between 0 & 9 to represent how **bright** to make the pixel.  

* ```.clearMicroBit(title)```  
    Will turn off all of the pixels - setting their brightness to 0.  

###GoogleMaps
---
A self-contained GoogleMaps widget.  
It provides useful functionality for finding somewhere on Earth.  
All requests for map data are performed in the background, so the UI shouldn't become unresponsive.  

![GoogleMaps](img/gmap_2.png)

```python
from appjar import gui

app = gui()
app.addGoogleMap("m1")
app.setGoogleMapSize("m1", "300x500")
app.go()
```

#### Add GoogleMaps  

* `.addGoogleMap(title)`  
    Creates a GoogleMap widget.  
    Displays a map image, and provides functionality to search, zoom, and change terrain, as well as a link to the original image.  

#### Set GoogleMaps  

* `.searchGoogleMap(title, location)`  
    Update the named GoogleMap widget to show the specified location.  

* `.zoomGoogleMap(title, mod)`  
    Change the zoom level of the named GoogleMap.  
    Providing a **+** or **-** will cause the map to zoom in or out one level.  
    Otherwise, a digit between 0 and 22 should be provided, to set the zoom level.  

* `.setGoogleMapTerrain(title, terrain)`  

* `.setGoogleMapSize(title, size)`  
    Set the size of the GoogleMap. Should be in the format `"300x300"`.  
    Note, if you set it too small, the control widgets won't look good...  

* `.setGoogleMapMarker(title, location, size=None, colour=None, label=None, replace=False)`  
    Will drop a marker on the specified location.  
    The marker will only be visible if the current `location` & `zoom level` permit.  
    If an empty `location` is provided, all markers will be removed.  
    `colour` can be set to any of (black, brown, green, purple, yellow, blue, gray, orange, red, white) or a hex value (starting '0x').  
    `size` can be set to any of (tiny, mid, small).  
    `label` can be set to a single letter or digit.  
    If `replace` is `True` this marker will replace the last one added.  

* `.removeGoogleMapMarker(title, label)`  
    Will remove the specified marker, if found.  

#### Get GoogleMaps  

* `.getGoogleMapLocation(title)`  
    Returns the current displayed location.  
    Will return an empty String, if the user clicked the **H** button.  

* `.getGoogleMapZoom(title)`  
    Returns the current zoom level of the map tile.  

* `.getGoogleMapTerrain(title)`  
    Returns the current terrain setting for the map tile.  

* `.getGoogleMapSize(title)`  
    Returns the current size of the map tile.  

#### Save GoogleMaps  

* `.saveGoogleMap(title, fileName)`  
    Saves the currently displayed map to the named location.  
    By default, all map tiles are GIFs.  

###PieChart
---
Widget to depict a Pie Chart.  
It will automatically calculate percentages, and draw a pie chart, given a dictionary of items and their amount.  
The PieChart is purely for display purposes, and is not interactive, other than a simple mouse-over effect with a tooltip.  
![PieChart](img/dev/pie.png)  

```python
from appJar import gui

app = gui()
app.addPieChart("p1", {"apples":50, "oranges":200, "grapes":75,
                        "beef":300, "turkey":150})
app.go()
```

####Add PieCharts  
* `.addPieChart(title, values)`  
    Takes a dictionary of names and values, which will be converted to percentages, and plotted on the chart.  
    The names will be used as part of tooltips that appear over each wedge of the PieChart.  

####Set PieCharts  
* `.setPieChart(title, name, value)`  
    Will update the PieChart, by either changing an existing value, adding a new value, or removing a value if it's set to 0.  

###Tree
---
Takes an arbitrary XML string, and converts it into a tree structure.  

![TreeWidget](img/dev/tree.png)

```python
from appJar import gui

app = gui()
app.addTree("t1",
            """<people>
            <person><name>Fred</name><age>45</age><gender>Male</gender></person>
            <person><name>Tina</name><age>37</age><gender>Female</gender></person>
            <person><name>CLive</name><age>28</age><gender>Male</gender></person>
            <person><name>Betty</name><age>51</age><gender>Female</gender></person>
            </people>""")
app.go()
```

####Add Trees
* `.addTree(title, xml_data)`  
    Create a tree from the specified XML data  

####Set Trees
* `.setTreeDoubleClickFunction(title, func)`  
    Register a function to call when an item is double-clicked  
* `.setTreeEditFunction(title, func)`  
    Register a function to call when an item is edited  
* `.setTreeEditable(title, value)`  
    Set whether the tree can be edited  
* `.setTreeColours(title, fg, bg, fgH, bgH)`  
    Set the fg/bg/fg highlight/bg highlight colours of the tree  
* `.setTreeBg(title, colour)`  
    Set the background colour of the tree  
* `.setTreeFg(title, colour)`  
    Set the foreground colour of the tree  
* `.setTreeHighlightBg(title, colour)`  
    Set the background colour of the highlighted node    
* `.setTreeHighlightFg(title, colour)`  
    Set the foreground colour of the highlighted node  

####Get Trees  
* `.getTreeXML(title)`  
    Return the tree as XML  
* `.getTreeSelected(title)`  
    Return the selected node as a String
* `.getTreeSelectedXML(title)`  
    Return the selected node (and any children) as XML

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

###Grid
---
Used to create a spreadsheet like interface.  
The grid has mouse interactivity, with mouse-over highlighting, and mouse-click highlighting.  
It is possible to include buttons at the end of each row, and an additional row of entry boxes, with their own button.  

![Grid](img/dev/grid.png)  

```python
from appJar import gui

app = gui()
app.setFont(20)
app.addGrid("g1",
    [["Name", "Age", "Gender"],
    ["Fred", 45, "Male"],
    ["Tina", 37, "Female"],
    ["Clive", 28, "Male"],
    ["Betty", 51, "Female"]])
app.go()
```

####Add Grids  

* `.addGrid(title, data, action=None, addRow=None)`  
    Receives a (jagged) 2D list of values. The first list should be the headers for the grid, the rest will contain each row of values.  

    If `action` is set, a button will be created, at the end of each row, calling the specified function. It will pass the row number (starting at 0).  

    ![Grid](img/dev/grid_2.png)   

    If `addRow` is set, then an additional row will appear at the end of the grid, with entry boxes and a button to call the specified function.  
    The button will pass the string `newRow` to the specified function.  

    ![Grid](img/dev/grid_3.png)   

    If both parameters are set to a function, then both buttons at the end of each row and a row of Entry boxes will be shown:  

    ![Grid](img/dev/grid_4.png)   

    It's also possible to set the following parameters:  
        * `actionHeading` - set the title of the right column  
        * `actionButton` - set the button text for each row  
        * `addButton` - set the button text for the Entry row  
        * `showMenu` - boolean to show a right-click menu  

    ![Grid](img/dev/1_gridMenu.png)   

#### Connecting to Databases

* `.addDbGrid(title, db, table)`  
    Will connect to the specified database, and show all rows in the specified table.  
    appJar will query the table to detect the PrimaryKey, and use this as the key when selecting the row.

* `.replaceDBGrid(title, db, table)`  
    Will replace the currently shown data in the grid, with the data found in the specified database/table.  

#### Get Grids  

* `.getGridRow(title, rowNumber)`  
    Returns a list of values representing the specified row.  

* `.getGridRowCount(title)`  
    Returns a count of how many rows are in the grid (not including the header row).  

* `.getGridSelectedCells(title)`  
    Gets a dictionary of booleans, indicating the status of each cell.  
    True indicates the cell is selected, False indicates the cell is not selected.  
    The name of each entry on the dictionary will be in the format ROW-COLUMN, eg. 0-2  

* `.getGridEntries(title)`  
    If `addRow` was set when the *Grid* was created, this function will get the contents of the entry boxes.  
    They will be returned as a list, in the same order as the entry boxes.  

####Set Grids  

* `.addGridRow(title, data)`  
    Adds a new row of data to the end of the existing grid.  
    It will be positioned at the bottom of the grid, above the entry boxes if present.  

To have the **Press** button on the entries row add a new row of data, try the following:  
```python
    def press(btn):
        if btn == "addRow":     # the button on the entries row
            data = app.getGridEntries("g1")
            app.addGridRow("g1", data)
``` 

* `.addGridRows(title, data)`  
    Adds the new rows of data to the end of the existing grid.  

* `.replaceGridRow(title, rowNum, data)`  
    Replace the values in the specified row with the new data.  
    If the new data has fewer items, the remaining cells will be emptied.  

* `.replaceAllGridRows(title, rowNum, data)`  
    Removes all existing rows, before adding the new rows.  

* `.setGridHeaders(title, data)`  
    Replace the values in the header row.  
    If the new data has fewer items, the remaining header cells will be emptied.  

* `.deleteGridRow(title, rowNum)`  
    Delete the specified row from the specified grid.

* `.deleteAllGridRows(title)`  
    Delete all rows from the specified grid (except the header row).  

* `.addGridColumn(title, columnNumber, data)`  
    Add the column of data to the named grid, in the specified position.  

* `.deleteGridColumn(title, columnNumber)`  
    Delete the specified column from the named grid.  

###MatPlotLib
---

Support for embedding very basic [MatPlotLib](http://matplotlib.org) plots.  

![Plot](img/1_plot.png)  
```python
from numpy import sin, pi, arange
from appJar import gui 
import random

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    return x,y 
    
def generate(btn):
    # *getXY() will unpack the two return values
    # and pass them as separate parameters
    app.updatePlot("p1", *getXY())
    showLabels()
    
def showLabels():
    axes.legend(['The curve'])
    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
    app.refreshPlot("p1")
    
app = gui()
axes = app.addPlot("p1", *getXY())
showLabels()
app.addButton("Generate", generate)
app.go()
```

* `.addPlot(title, x, y)`  
    Create a plot with the specified x and y values.  
    Returns the plot object, to allow further customisation.  

* `.addPlotFig(title)`  
    Create an empty Figure, so that you can add your own plots.  
    Returns the figure object, to allow further customisation.  

```python
from appJar import gui 
from mpl_toolkits.mplot3d import Axes3D

with gui() as app:
    fig = app.addPlotFig("p1")
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([1,2],[1,2],[1,2])
```

* `.updatePlot(title, x, y, keepLabels=False)`  
    Update the specified plot with the specified x and y values.  
    **NB.** if you do this you will lose any customisations applied to the axes.  
    If you set `keepLabels` to True, then the axis labels & title will be retained.  
    Also, your app will crash, if you call this after `.addPlotFig()`  

* `.refreshPlot(title)`  
    Call this any time you modify the axes.  

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

### Canvas
---
This lets you embed a canvas in appJar

![Canvas](img/1_canvas.png)  

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
    Removes all drawings from the canavs.  

### Turtle
---
This lets you embed a [turtle](https://docs.python.org/3.6/library/turtle.html) widget in appJar.  

![Turtle](img/1_turtle.png)  

```python
from appJar import gui 

def press(b):
    s = app.getTurtleScreen("t1")
    t = app.getTurtle("t1")
    s.bgcolor("blue")
    t.pencolor("white")
    for i in range(20):
        t.forward(i * 10) 
        t.right(144)

app=gui()
app.addTurtle("t1")
app.addButton("DRAW", press)
app.go()
```

* `.addTurtle(title)`  
    Creates a turtle widget.  

* `.getTurtle(title)`  
    Gets the specified turtle widget.  

* `.getTurtleScreen(title)`  
    Gets the screen behind the turtle widget.  

