# ttk (very BETA)

appJar includes experimental support for *ttk*,  a [tk themed widget set](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk).  

If you run appJar in ttk mode, some of the widgets will be replaced with more native looking widgets.  

**NB.** appJar has a lot of built in styling for standard widgets, supporting ttk has required changing how all this is done. When you come across issues, please log them in GitHub.  

## Enabling ttk
---

* `.gui(useTtk=True)`  
    To enable ttk, set the `useTtk` flag in the appJar constructor to `True`.  
    If you want to specify a particular theme, set it to the name of the theme.  

* `.setTtkTheme(theme)`  
    This allows you to choose a different theme to use.  

* `.getTtkTheme()`  
    Returns the currently selected ttk theme as a string. 

## Themes  
---
ttk will default to a theme similar to the operating system.  
A list of additional themes can be displayed by calling:

* `.getTtkThemes()`  
    Returns a list of theme names.  

Additional themes can be installed using [ttk extensions](github.com/RedFantom/ttkthemes).  

These can be installed via pip: `pip install ttkthemes`  
And then used the same as any other theme: `app.setTtkTheme("black")`.  

## Styling ttk Widgets
---
appJar stores the ttk style as `app.ttkStyle` this can be modified or changed directly as required.  

### Default Widget Style
Each widget type has its own style, such as `TLabel` or `TButton`.  
To change the style for all widgets of a certain type, reconfigure these styles:

```python
app.ttkStyle.configure("TLabel", foreground="green", background="blue")
```

### Root Style
All widgets inherit their style from the root style, known simply as `.`  
If you want to change the style of all widgets, you can modify the root style.  
**NB.** if particular widget types have set their own styles, modifying the root style won't change them.  

```python
app.ttkStyle.configure(".", background="black", foreground="white")
```

### Create Your Own Styles
Finally, it's possible to create your own styles, and use them for particular widgets.  
Your new style should inherit from the widget's style: `MyButton.TButton`  

```python
app.ttkStyle.configure("MyButton.TButton", foreground="red")
```

You can also create dynamic appearance changes to the widgets, called 'maps'.
These allow you to change the properties of the widget in response to certain events, such as changing the colour of a button when the cursor is over it.

```python
app.ttkStyle.map("MyButton.TButton", background=[("active", "blue")])
```

You'll need to pass a list, which contains tuples as a parameter.
* Each tuple is responsible for changing one aspect of the widget in a particular state.

* To have multiple changes, you can have more than one tuple within the list.

* The first item in the tuple should be the *state*.
    In this case, it is `active`. This means that something will be changed when the cursor is within the widget.

* The second item will be the *value*.
    In this case, the button will have a blue background when the cursor is over it.

* You can learn more about ttk maps [here](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html).


You then need to apply this style (which includes both `ttkStyle.configure` and `ttkStyle.map`) to the relevant widgets:

* `.set XXX Style(style)`  
    This lets you specify the name of a style for a particular widget.  

```python
app.setEntryStyle("Name", "BW.TEntry")
```

## Built in Setters
---
You can still use the existing setters for background `.setBg()` and foreground `.setFg()`:  

```python
app.setBg("blue")
app.setFg("yellow")
```

## Command Line Arguments
---

It's possible to switch on ttk theming from the [command line](/pythonCommandLine).  
Simply use the `--ttk` flag, with an optional theme name:  

```sh
python3 themes.py --ttk  # turn on ttk widgets
```  

Turn on ttk widgets and set a theme:  

```sh
python3 themes.py --ttk aqua # turn on ttk with the aqua theme
```
