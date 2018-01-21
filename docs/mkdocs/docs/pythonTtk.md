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
app.ttkStyle.configure("TLabel", foreground="green", backgroun="blue")
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

You then need to apply this style to the relevant widgets:

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
