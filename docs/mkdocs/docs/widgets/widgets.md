#Widgets
----
In a GUI, the fillings are known as **widgets**.  
There are lots of different widgets to choose from, each suited to a specific task.  

Nearly every widget needs a **TITLE**.  
This is a unique name for the widget, so that later you can get information from that widget, or change it.  

Nearly all widgets in appJar provide the same three functions:

* (Always) - **ADD** a widget (with a unique title) - this creates the widget
* (Often) - **GET** the widget (using its unique title) - this gets the contents of the widget (usually done in a function)
* (Sometimes) - **SET** the widget (using its unique title) - this changes what's in the widget

On top of these, there is a common set of functions for [changing widgets](pythonWidgetOptions.md).  
As well as some specialist functions, unique to each widget (see below).  

##Auto-Labelled Widgets
___

It's possible to automatically include a *label* alongside a lot of the  widgets.  
Both the label and widget will be placed in the same grid space.  
Simply add the word `Label` to the command when adding the widget:  

* `.addLabelEntry(title)`
* `.addLabelNumericEntry(title)`
* `.addLabelSecretEntry(title)`
* `.addLabelAutoEntry(title, words)`
* `.addLabelScale(title)`
* `.addLabelOptionBox(title, values)`
* `.addLabelTickOptionBox(title, values)`
* `.addLabelSpinBox(title, values)`
* `.addLabelSpinBoxRange(title, from, to)`  

See the relevant section for a description of what the widget does.
