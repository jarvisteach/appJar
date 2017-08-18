#ttk

appJar includes experimental support for *ttk*,  a tk themed widget set.  
This is very **BETA.*, and most stuff will break!

## Setup
---

* `.usettk()`  
    Calling this at the start of your program will tell it to use ttk widgets.  

* `.setTtkTheme(theme)`  
    This allows you to choose which theme to use.  

## Command Line Arguments
---

It's possible to switch on ttk theming from the [command line](/pythonCommandLine).  
Simply use the `--ttk` flag, with an optional theme name:  

```sh
python3 themes.py --ttk  # turn on ttk widgets
```  

It's also possible to set the file name to log to:

```sh
python3 themes.py --ttk aqua # turn on ttk with the aqua theme
```
