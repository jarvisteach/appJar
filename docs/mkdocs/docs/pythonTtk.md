#ttk

appJar includes experimental support for *ttk*,  a [tk themed widget set](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk).  
This is very **BETA**, and most stuff will break!

## Setup
---

* `.go(useTtk=True)`  
    Enabling ttk in the appJar constructor also sets the topLevel Frame to be a ttk.Frame - the preferred option.  

* `.useTtk()`  
    Calling this at the start of your program will tell it to use ttk widgets where possible.  

* `.setTtkTheme(theme)`  
    This allows you to choose which theme to use.  

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
