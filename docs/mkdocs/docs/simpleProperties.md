# GUI Properties  
---

Most of the setters & getters for GUI/widget configuration are now available as properties.  
This allows them to be set in a slightly simpler way:

```python
app.title = "Property Demo"
app.bg = "red"
app.fg = "yellow"
```

If you want to set multiple properties at once, there is a `configure()` function to support this:

* `.configure(**kwargs)`  
    Pass in a list of properties to configure.

```python
app.configure(bg='red', fg='yellow', font={'size':20, 'family':'Helvetica'})
```

## Property List
---

| Property | Data type | GET/SET |Description |
| --------- | --------- | --------- | ------------|
| title | string | GET & SET | Pass a string for the title of the GUI |
| icon | string | GET & SET | Pass the path to an icon file |
| transparency | SET | integer | Pass a percentage (between 0 & 100) to set the transparency |
| visible | GET & SET | boolean | Pass either `True` or `False` |
| | | | |
| padding | integer (list) | SET | Pass a tuple containing the x & y padding or a single integer for both x & y |
| inPadding | integer (list) | SET | Pass a tuple containing the x & y padding or a single integer for both x & y |
| guiPadding | integer (list) | SET | Pass a tuple containing the x & y padding or a single integer for both x & y |
| | | | |
| size | integer (list) | GET & SET | Pass a tuple containing the width & height (or the string `fullscreen`) |
| location | integer (list) | GET & SET | Pass a tuple containing the x & y coordinates (or the string `CENTER`) |
| fullscreen | boolean | GET & SET | Pass either `True` or `False` |
| resizable | boolean | GET & SET | Pass either `True` or `False` |
| | | | |
| sticky | string | GET & SET | Pass a string describing which sides to stick to (news). |
| stretch | string | GET & SET | Pass a string describing if rows/columns should stretch. |
| row | integer | GET & SET | Gets or sets the next row number to be used. |
| | | | |
| fg | string | SET | Pass a colour to use for the text colour of all label style widgets. |
| bg | string | SET | Pass a colour to use for the background of all label style widgets. |
| font | integer/dict | SET | Pass either a font size, or a dictionary of font properties to use for all widgets. |
| buttonFont | integer/dict | SET | Pass either a font size, or dicitonary of font properties to use for all button style widgets. |
| labelFont | integer/dict | SET | Pass either a font size, or a dictionary of font properties to use for all label style widgets. |
| fonts | string (list) | GET | Returns a list of available fonts. |
| ttkTheme | string | GET & SET | Only available in ttk mode - pass the name of the ttk theme you want to use. |
| | | | |
| editMenu | Boolean | SET | Enables and disables the right-click edit menu for text based widgets. |
| stopFunction | function | SET | Sets a function to call when the GUI is closed. |
| enterKey | function | SET | Sets or disables (pass None) a function bound to the enter key. |
| logLevel | string | GET & SET | Sets the logging level. |
| logFile | string | GET & SET | Sets a file to log messages to. |
| language | string | GET & SET | Sets the current language. |
| | | | |
