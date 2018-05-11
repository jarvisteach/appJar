# v1.0 Properties  
---

appJar includes a number of properties that can be configured to change how the GUI looks/acts.  
These are exposed as **properties**, so can be set uing the assignment operator, `=`.  

```python
app.title = "Property Demo"
app.bg = "red"
app.fg = "yellow"
```

If you want to set multiple properties at once, there is a `configure()` function to support this:

* `.configure(**kwargs)`  

```python
app.configure(bg='red', fg='yellow', font={'size':20, 'family':'Helvetica'})
```

Nearly all properties can be got in the same way:  

```python
app.label('sizeLab', app.size)
app.label('locLab', app.location)
app.label('transLab', app.transparency)
```

### GUI Settings
---

| Property | Data type | Description |
| --------- | --------- | ------------|
| title | string | Pass a string to display in the title bar of the GUI |
| icon | string | Pass the path to an icon file, to display in the title bar - only works on Windows. |
| transparency | integer | Pass a percentage (between 0 & 100) to set the transparency, of the GUI (not on Linux). |
| visible | boolean | Pass a boolean to hide or show the GUI. |
| top | boolean | Pass a boolean to keep the GUI on top or not. |
| | | | |

### Padding
---  

| Property | Data type | Description |
| --------- | --------- | ------------|
| padding | integer (list) | Pass a tuple containing the x & y padding or a single integer for both x & y |
| inPadding | integer (list) | Pass a tuple containing the x & y padding or a single integer for both x & y |
| guiPadding | integer (list) | Pass a tuple containing the x & y padding or a single integer for both x & y |
| | | | |

### Size & Location
---  

| Property | Data type | Description |
| --------- | --------- | ------------|
| size | integer (list) | Pass a tuple containing the width & height (or the string `fullscreen`) |
| location | integer (list) | Pass a tuple containing the x & y coordinates (or the string `CENTER`) |
| fullscreen | boolean | Pass either `True` or `False`, to enter/exit fullscreen. |
| resizable | boolean | Pass either `True` or `False`, to set the GUI resizable or not. |
| | | | |

### Grid Properties
---  

| Property | Data type | Description |
| --------- | --------- | ------------|
| sticky | string | Pass a string describing which sides widegts should stick to (news). |
| stretch | string | Pass a string describing if rows/columns should stretch, to fill the entire GUI. |
| row | integer | Gets or sets the next row number to be used. |
| | | | |

### Looks
---  

| Property | Data type | Description |
| --------- | --------- | ------------|
| fg | string | Pass a colour to use for the text colour of all label style widgets. |
| bg | string | Pass a colour to use for the background of all label style widgets. |
| font | integer/dict | Pass either a font size, or a dictionary of font properties to use for all widgets. |
| buttonFont | integer/dict | Pass either a font size, or dicitonary of font properties to use for all button style widgets. |
| labelFont | integer/dict | Pass either a font size, or a dictionary of font properties to use for all label style widgets. |
| ttkTheme | string | Only available in ttk mode - pass the name of the ttk theme you want to use. |
| fonts | string (list) | (no SETTER) Returns a list of all available fonts. |
| | | | |

### Other
---  

| Property | Data type | Description |
| --------- | --------- | ------------|
| editMenu | Boolean | Enables and disables the right-click edit menu for text based widgets. |
| stopFunction | function | (no GETTER) Sets a function to call when the GUI is closed. |
| startFunction | function | (no GETTER) Sets a function to call when the GUI starts up. |
| fastStop | Boolean | Set this to True if you have a **LOT** of widgets, and stopping appJar has gotten slow (doesn't work from IDLE). |
| enterKey | function | (no GETTER) Sets or disables (pass None) a function bound to the enter key. |
| logLevel | string | Sets the logging level. |
| logFile | string | Sets a file to log messages to. |
| language | string | Sets the current language. |
| | | | |
