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

The starting language must be set in the call to `.go(language)` or provided as a command line argument.  
To change the language, call `.changeLanguage(language)`  

These will look for a file called `LANGUAGE.ini`

#### Command Line Arguments  
It is possible to set the starting language as a [command line argument](/pythonCommandLine):  

```sh
python3 languages.py -l english
```

This will override any language set in the call to `.go()`, and removes the need to set one at all.  

### Widget Support
Not all widget's are supported yet, and some require a bit more effort to get them to work properly.  
Note, changing the text of a widget through `setXXX()` method's will work, but will not be remembered if the language is changed.  

* **Auto-labelled Widgets**  
    The labels of any widgets created with an **auto-label** can be changed under the `[LABEL]` option below.  

* `[LABEL]`, `[BUTTON]`, `[CHECKBOX]`, `[MESSAGE]`, `[LINK]`, `[LABELFRAME]`, `[TOGGLEFRAME]`  
    The widget ID, followed by the text to update it with.  
    Any widgets added with auto-labels (`.addLabelEntry()`) are also changed here.  

* `[TITLE]`  
    This allows you to change the GUI's title, or the title of any SubWindows.
```
[TITLE]
appJar: Main GUI Title
sub1: SubWindow 1 Title
sub2: SubWindow 2 Title
```

* `[RADIOBUTTON]`, `[TABBEDFRAME]`  
    For these, the ID must be in two parts: the name of the frame or radio button group, followed by the name of the tab or radio button.  
    The two should be joined together with a dash, for example:  
```
[TABBEDFRAME]
    mainFrame-Tab 1: Information
    mainFrame-Tab 2: Extras
    mainFrame-Tab 3: Help

[RADIOBUTTON]
    Food-rb1: baguettes
    Food-rb2: fromage
    Food-rb3: vin
```

* `[ENTRY]`  
    The text provided here will be used for the default value, if one is being used.  

* `[SCALE]`, `[TEXTAREA]`, `[METER]`  
    These widgets have no text to change.  

* `[LISTBOX]`, `[SPIN]`, `[OPTION]`  
    Each value should be on a new line  
    Doesn't work for SpinBoxes, when generated from a range.  
```
[LISTBOX]
fruits:
    apples
    pears
    grapes
    bananas
```

* The following are currently in development:  
    `[PROPERTIES]`, `[POPUP]`, `[PIECHART]`, `[TREE]`, `[GRID]`  
    `[MENUBAR]`, `[STATUSBAR]`, `[TOOLBAR]`, `[TOOLTIP]`  
    `[PAGEDWINDOW]`  
    `[SOUND]` & `[IMAGE]`  

* `[EXTERNAL]`  
    It will be possible to request translations for non appJar data.  

### Platform Support
Note, your platform might not support the characters you want to display.  
In which case, you'll need to install the relevant font.  
For example, to get Korean characters to show on raspberry Pi, try:  
`sudo apt-get install fonts-nanum`  

If you're after other languages, you can try:  
`apt-cache search chinese` and then install a likely looking font...  
