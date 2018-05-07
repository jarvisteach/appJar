# Command Line Arguments

appJar supports a number of [command line arguments](https://en.wikipedia.org/wiki/Command-line_argument_parsing).  
These are values that can be set when appJar is initially run.  

### Options  

* `--help` `-h`  
    This will display a help message, then exit.  

* `--version` `-v`  
    This will display the version of appJar, then exit.  

* `-l [filename.ini]`  
    This allows you to set the starting language, only useful if using [internationalisation](/pythonInternationalisation/).  
    It will override any language configured in the `.go()` function call.  

* `-c`, `-e`, `-w`, `-i`, `-d`, `t`  
    This sets the [logging level](/pythonLogging/):  
    * `-c`   only log CRITICAL messages  
    * `-e`   log ERROR messages and above  
    * `-w`   log WARNING messages and above
    * `-i`   log INFO messages and above  
    * `-d`   log DEBUG messages and above  
    * `-t`   log TRACE messages and above  

* `-f [filename.log]`  
    This allows you to specify a [file](/pythonLogging/#logging-to-file) to log messages to.  

* `-s [appJar.ini]`  
    This allows you to specify a [settings file](/pythonSettings/) to load/save settings to.  

* `--ttk [theme name]`  
    This allows you to request appJar uses [ttk widgets](/pythonTtk/) where possible.  
    It can followed by an optional theme name, to declare which style to use for ttk widgets.  

---
<div style='text-align: center;'>
*Advertisement&nbsp;<sup><a href="/advertising">why?</a></sup>*
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

### Example  
---
The following example will start the app logging DEBUG messages, and using an ENGLISH language file:  

```sh
    python3 demoApp.py -d -l ENGLISH
```

### Disabling  

If you want to provide your own command line argument handling, then you will need to disable it in appJar, as appJar will show an error message if invalid arguments are found.  

To do this, you can set the `handleArgs` flag to False in the appJar constructor:  

```python
from appJar import gui
app = gui(handleArgs=False) # disable argument handling
app.addLabel("l1", "No argument handling")
app.go()
```
