#Internationalisation
---

appJar offers a simple method for supporting multiple languages.  

###File Format  
A config file needs to be created, for each language, with translations for each widget:

```
>>> ENGLISH.ini
---
[LABEL]
l1: some text
l2: some more text

[BUTTON]
b1: button a
b2: button b

[LINK]
l1: New link title
```

When widgets are added, their ID will be used to look up a translation.  
If no translation is found, the widget's initial value will be used as a default.  

The filename should be in all uppercase, of type `.ini`  

###Implementation  
```python
from appJar import gui

app=gui("Languages")

app.addLabel("l1", "default text")
app.addLabel("l2", "default text")
app.addLabel("l3", "default text")

# as long as the language file has the same name as the button
# the button can call .changeLanguage directly
app.addButtons(["English", "Francais", "한글"], app.changeLanguage)

app.go("english")
```

The starting language must be set in the call to `.go(language)`  
To change the language, call `.changeLanguage(language)`  

These will look for a file called `LANGUAGE.ini`

### Widget Support
Not all widget's are supported, and some require a bit more effort to get them to work properly.  
Note, changing the text of a widget through `setXXX()` method's will work, bit will not be rememberd if the language is changed.  

* **Auto-labelled Widgets**  
    Any widgets created with an **auto-label** can be changed under the `[LABEL]` option below.  

* `[LABEL]`,  `[BUTTON]`, `[CHECKBOX]`, `[MESSAGE]`, `[LINK]`  
    The label id, followed by the text to put in it.  
    Any widgets added with labels `.addLabelEntry()` are also changed here.  

* `[SCALE]`, `[TEXTAREA]`, `[METER]`, `[ENTRY]`  
    These widgets have no text to change.  
    The `[ENTRY]` does have default text, which will be supprted in a later release.  

* `[LISTBOX]`, `[SPIN]`, `[OPTION]`, `[PROPERTIES]`, `[RADIOBUTTON]`  
    Contain lists of items, need additional development.  

* `[LABELFRAME]`, `[TABBEDFRAME]`, `[PAGEDWINDOW]`, `[TOGGLEFRAME]`  
    Not standard widgets, need additional development.  

* `[MENUBAR]`, `[STATUSBAR]`, `[TOOLBAR]`, `[TOOLTIP]`, `[TITLE]`  
    Not standard widgets, need additional development.  

* `[POPUP]`  
    Not supported yet.  

* `[SOUND]` & `[IMAGE]`  
    Not supported yet.  

* `[PIECHART]`, `[TREE]`, `[GRID]`  
    Widgets in developemnt - not supported yet.  

* `[EXTERNAL]`  
    It will be possible to request translations for non appJar data.  
