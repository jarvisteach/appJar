# ttk (very BETA)

appJar includes experimental support for *ttk*,  a [tk themed widget set](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk).  

## Setup
---

* `.go(useTtk=True)`  
    Enabling ttk in the appJar constructor also sets the topLevel Frame to be a ttk.Frame - the preferred option.  

* `.useTtk()`  
    Calling this at the start of your program will tell it to use ttk widgets where possible.  

* `.setTtkTheme(theme)`  
    This allows you to choose which theme to use.  

* `.set XXX Style(style)`  
    This lets you specify the name of a style for a widget.  

## Additional Themes  
---
Additional themes can be installed using [ttk extensions](github.com/RedFantom/ttkthemes).  

These can be installed via pip: `pip install ttkthemes`  
And then used the same as any other theme: `app.setTtkTheme("black")`.  

---
<div style='text-align: center;'>
*Advertisement*  
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
    style="display:block"
    data-ad-format="fluid"
    data-ad-layout-key="-gw-13-4l+6+pt"
    data-ad-client="ca-pub-6185596049817878"
    data-ad-slot="5627392164"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
---

## Modifying ttk Styles  
---
appJar stores the ttk style as `app.ttkStyle` this can be modified or changed directly as required.  

To modify individual widgets, create a new style and apply it to the widget:  
```python
app.ttkStyle.configure("BW.TEntry", foreground="green")
app.setEntryStyle("Name", "BW.TEntry")
```

To modify all widgets of a particular type:  
```python
app.ttkStyle.configure("TLabel", foreground="green", backgroun="blue")
```

To change the BG of the GUI & all labels:  
```python
app.ttkStyle.configure("TLabel", backgroun="blue")
app.ttkStyle.configure("TFrame", backgroun="blue")
```

Or, you can call the `.setFg()` and `.setBg()` functions:  
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
