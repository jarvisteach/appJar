# appJar Properties  
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

Some properties support being got in the same way (see below for which ones):

```python
app.label('sizeLab', app.size)
app.label('locLab', app.location)
app.label('transLab', app.transparency)
```

### GUI Settings
---

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| title | string | Yes | Pass a string to display in the title bar of the GUI |
| icon | string | Yes | Pass the path to an icon file, to display in the title bar - only works on Windows. |
| transparency | integer | No | Pass a percentage (between 0 & 100) to set the transparency, of the GUI (not on Linux). |
| visible | boolean |  Yes | Pass either a boolean to hide or show the GUI. |
| | | | |

### Padding
---  

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| padding | integer (list) | No | Pass a tuple containing the x & y padding or a single integer for both x & y |
| inPadding | integer (list) | No | Pass a tuple containing the x & y padding or a single integer for both x & y |
| guiPadding | integer (list) | No | Pass a tuple containing the x & y padding or a single integer for both x & y |
| | | | |

### Size & Location
---  

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| size | integer (list) | Yes | Pass a tuple containing the width & height (or the string `fullscreen`) |
| location | integer (list) | Yes | Pass a tuple containing the x & y coordinates (or the string `CENTER`) |
| fullscreen | boolean | Yes | Pass either `True` or `False` |
| resizable | boolean | Yes | Pass either `True` or `False` |
| | | | |

### Grid Properties
---  

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| sticky | string | Yes | Pass a string describing which sides to stick to (news). |
| stretch | string | Yes | Pass a string describing if rows/columns should stretch. |
| row | integer | Yes | Gets or sets the next row number to be used. |
| | | | |

### Looks
---  

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| fg | string | No | Pass a colour to use for the text colour of all label style widgets. |
| bg | string | No | Pass a colour to use for the background of all label style widgets. |
| font | integer/dict | No | Pass either a font size, or a dictionary of font properties to use for all widgets. |
| buttonFont | integer/dict | No | Pass either a font size, or dicitonary of font properties to use for all button style widgets. |
| labelFont | integer/dict | No | Pass either a font size, or a dictionary of font properties to use for all label style widgets. |
| ttkTheme | string | Yes | Only available in ttk mode - pass the name of the ttk theme you want to use. |
| fonts | string (list) | Get only | Returns a list of available fonts. |
| | | | |

### Other
---  

| Property | Data type | Get? |Description |
| --------- | --------- | --------- | ------------|
| editMenu | Boolean | No | Enables and disables the right-click edit menu for text based widgets. |
| stopFunction | function | No | Sets a function to call when the GUI is closed. |
| enterKey | function | No | Sets or disables (pass None) a function bound to the enter key. |
| logLevel | string | Yes | Sets the logging level. |
| logFile | string | Yes | Sets a file to log messages to. |
| language | string | Yes | Sets the current language. |
| | | | |
