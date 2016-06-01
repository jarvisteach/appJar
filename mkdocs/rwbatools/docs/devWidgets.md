#Widgets Under Development
----
The following widgets are **under development**. They're included in the library, but offer limited functionality, and are stilll quite buggy.

###PieChart
---
Shows a pie chart

* `.addPieChart(name, values, size=100)`

###Tree
---
This widget is still in development. It takes an arbitrary XML string, and converts it into a tree structure.

* `.addTree(title, xml_data)`

    Create a tree from the xml data

* `.addTreeFunction(title, func)`

    Register he function with double click

* `.getTree(title)`

    Return the tree

###Grid
---
This widget is still in development.  

* `.addGrid(title, data, action=None, addRow=False)`  

    Receives a (jagged) 2D list of values. The first list should be the headers for the grid, the rest will contain each row of values.  

    If action is set, a button will be created, calling the specified function. If addRow is True, then an additional row will appear, at the end, with Entry boxes.  

* `.updateGrid(title, data, addRow=False)`
* `.setGridGeom(title, width, height)`
* `.getGridEntries(title)`
* `.setGridBackground(title, colour)`
