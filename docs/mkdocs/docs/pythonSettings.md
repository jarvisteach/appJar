# appJar Settings

appJar can remember variaous GUI settings, and restore them on launch.  

## Setup  
---

* `.go(useSettings=False)`
    This will enable settings, and cause them to be loaded & saved automatically.  

* `.loadSettings(fileName="appJar.ini", useSettings=True)`  
    This function can be called manually if you want to load settings at a later time.  
    An alternative file can be specified.  
    If `useSettings` is set to False, appjar won't save the settings back at the end.  

* `.saveSettings(fileName=appJar.ini")`  
    This will save the current settings, with an optional file name.  

* `.getSetting(name, default=None)`  
    This allows you to request a user setting of the specified name.  
    If no setting is found, the `default` value will be returned.  

* `.setSetting(name, value)`
    This will store the named setting, with the specified value.  
    You must make sure settings are being saved, for this to take effect.  

## Command Line Arguments  
---

It's possible to switch on settings from the command line.  
Simply use the `-s` flag, with an optional  file name:

```
python3 themes.py -s  # turn on settings
```
Turn on settings, with a specified filename:
```
python3 themes.py --s myFile.txt  # turn on settings with a specified filename
```
