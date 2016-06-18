#Widgets Under Development
----
The following widgets are **under development**. They're included in the library, but offer limited functionality, and are stilll quite buggy.

###PieChart
---
Shows a pie chart  

* `.addPieChart(name, values, size=100)`  
    Takes a list of integers, which will be converted to percentages, and plotted on the chart.  
    An optional size parameter can be passed, to adjust the size of the chart.  

![PieChart](img/dev/pie.png)  

```python
    from appJar import gui

    app=gui()
    app.addPieChart("p1", [50, 200, 75, 300, 150], size=300)
    app.go()
```

###Tree
---
Takes an arbitrary XML string, and converts it into a tree structure.  

* `.addTree(title, xml_data)`  
    Create a tree from the specified XML data  
* `.addTreeFunction(title, func)`  
    Register a function to call when an item is double-clicked  
* `.getTree(title)`  
    Return the tree as XML  

![TreeWidget](img/dev/tree.png)

```python
from appJar import gui

app=gui()
app.addTree("t1",
            """<people>
            <person><name>Fred</name><age>45</age><gender>Male</gender></person>
            <person><name>Tina</name><age>37</age><gender>Female</gender></person>
            <person><name>CLive</name><age>28</age><gender>Male</gender></person>
            <person><name>Betty</name><age>51</age><gender>Female</gender></person>
            </people>""")
app.go()
```

###Grid
---
Used to create a spreadsheet like interface.  
* `.addGrid(title, data, action=None, addRow=False)`  
    Receives a (jagged) 2D list of values. The first list should be the headers for the grid, the rest will contain each row of values.  
    If action is set, a button will be created, calling the specified function. If addRow is True, then an additional row will appear, at the end, with Entry boxes.  

* `.updateGrid(title, data, addRow=False)`  
* `.setGridGeom(title, width, height)`  
* `.getGridEntries(title)`  
* `.setGridBackground(title, colour)`  

![Grid](img/dev/grid.png)  

```python
    from appJar import gui

    app=gui()
    app.setFont(20)
    app.addGrid("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]])
    app.go()
```

###Meters
Working on some different styles for the Meter.  
And, a better look - gradiated colour...  
####SplitMeter
Shows two values, left & right  

![SplitMeter](img/1_splitMeter.png)

####DualMeter
Shows percentage left & right  

###Properties
---
A quick-to-create set of radio/check boxes.  

* `.addProperties(props)`  
    Creates the properties box, with the list of properties.  
    The properties can be passed in as dictionary, but the order will be random.  
* `.addProperty(title, value=False)`  
    Adds the named property to the end of the properties list.  
* `.getProperties()`  
    Returns the properties as a dictionary.  
* `.getProperty(title)`  
    Gets the named property.  
* `.setProperty(title, value=True)`  
    Sets the named property.
