# Internationalisation
---

appJar offers a simple method for supporting multiple languages.  
A config file is created, for each supported language, containing a translation for each widget.  

### File Format  
The config file's name should be the language it represents, with an extension of `.ini`.  
Within that file will be a **[SECTION]** for each widget type, followed by a list of widget IDs and their translation, separated by colons.  

For example, a file called `ENGLISH.ini` might contain:  

```sh
[LABEL]
l1: some text
l2: some more text

[BUTTON]
b1: button a
b2: button b

[ENTRY]
e1: --default text--

[LINK]
l1: New link title
```

If no translation is found, the widget's initial value will be used as a default.  

**NB.** The filename should be in all uppercase, of type `.ini`  

### Coding It  
```python
from appJar import gui
app=gui("Language Demo")

app.addLabel("l1", "default text")
app.addLabel("l2", "default text")
app.addLabel("l3", "default text")

# as long as the language file has the same name as the button
# the button can call .changeLanguage directly
app.addButtons(["English", "Francais", "한글"], app.changeLanguage)

app.go("english")
```  

The starting language can be set in the call to `.go()` or provided as a [command line argument](/pythonCommandLine/).  

To change the language, call `.changeLanguage(language)`  

#### Command Line Arguments  
It is possible to set the starting language as a command line argument:  

```sh
    python3 languages.py -l ENGLISH
```

This will override any language set in the call to `.go()`, and removes the need to set one at all.  

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

### Widget Support
---
**NB.** changing the text of a widget through `setXXX()` method's will work, but will not be remembered if the language is changed.  

* `[LABEL]`, `[BUTTON]`, `[ENTRY]`, `[CHECKBOX]`, `[MESSAGE]`, `[LINK]`, `[LABELFRAME]`, `[TOGGLEFRAME]`  
    As demonstrated above, use the widget ID, followed by the text to update it with.  
    Any labels created by [auto-label](/inputWidgets/#auto-labelled-widgets) widgets are also set here.  
    **NB.** Only the *default value* of entries will be translated.  

* `[IMAGE]` & `[SOUND]`  
    For [images](/pythonImages/), you should provide a valid filename.  
    For [sounds](/pythonSound/), the filename will be translated when the sound function is called - it will be modified with the sound folder *after* translation.  

```sh
[IMAGE]
default-flag.jpg: mexican-flag.jpg

[SOUND]
default-anthem.wav: mexican-anthem.wav
default-speech.wav: mexaican-speech.wav
default-welcome.wav: mexican-welcome.wav
```  

* `[TITLE]`  
    This allows you to change the [GUI's title](/pythonGuiOptions/#look-feel), the [splashscreen's](/splash/) text, the [statusbar](/pythonBars/#statusbar)'s header or the title of any [SubWindows](/pythonWidgetGrouping/#sub-window).

```sh
[TITLE]
appJar: Main GUI Title
splash: New Splash Text
statusbar: DATA
sub1: SubWindow 1 Title
sub2: SubWindow 2 Title
```

* `[RADIOBUTTON]`, `[PROPERTIES]`, `[TABBEDFRAME]`  
    For these, the ID must be in two parts: the name of the button group/properties/frame followed by the name of the button/property/tab.  
    The two should be joined together with a dash:  

```sh
[RADIOBUTTON]
Food-rb1: baguettes
Food-rb2: fromage
Food-rb3: vin

[PROPERTIES]
props-prop1: Extra Cheese
props-prop2: Sweetcorn
props-prop3: Pineapple

[TABBEDFRAME]
mainFrame-Tab1: Information
mainFrame-Tab2: Extras
mainFrame-Tab3: Details
```

* `[GRID]` & `[PAGEDWINDOW]`  
    As above, the key is made of two parts.  
    There are three configurable items in a [Grid](/pythonDevWidgets/#table); the buttons & label in the right-hand column.  
    There are three configurable items in a [PagedWindow](/pythonWidgetGrouping/#paged-window); the title, previous & next buttons.  
    These should each be preceeded by the name of the widget:  
```sh
[GRID]
financesGrid-actionHeading: Update Row
financesGrid-actionButton: Update
financesGrid-addButton: Add

[PAGEDWINDOW]
Address Book-title: AddressBuch
Address Book-prevButton: Vorhergehend
Address Book-nextButton: Danach
```

* `[LISTBOX]`, `[SPINBOX]`, `[OPTIONBOX]`  
    These have multiple values for a single widget, so each value should be on a new line, after the ID.  
    **NB.** You can't translate a SpinBox that was generated from a range.  
```sh
[LISTBOX]
fruits:
    apples
    pears
    grapes
    bananas

[SPINBOX]
weekdays:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
```

* `[POPUP]`  
    Popups have two pieces of translatable text - the title & message, it's not possible to translate the buttons.  
    As with SpinBoxes & ListBoxes, the title & messages should be put on separate lines:  

```sh
[POPUP]
EXIT-POPUP:
    Confirm Exit
    Press OK to confirm exit.
SAVE-POPUP:
    Confirm Save
    Press OK to confirm you want to save the file.
```  

```python
def saveFile(btn):
    # SAVE-POPUP is a translation key, so the two parameters should be replaced
    if app.okBox("SAVE-POPUP", "Confirm you want to save."):
        saveFile()

def quit(btn):
    # SAVE-POPUP is a translation key, so the two parameters should be replaced
    if app.okBox("EXIT-POPUP", "Confirm you want to exit."):
        app.stop()
```  

* `[TOOLBAR]`  
    Each button should be on a new line, if the button has an image the line will be ignored.    
```sh
[TOOLBAR]
button1: New Button Name
button2: Another New Button Name
button3: One More New Button Name
OPEN: This will be ignored because it has an image...
```

* `[TOOLTIP-XXX]`  
    To translate [tooltips](/pythonDialogs/#tooltips) you will need a new section for each widget type, of the format: `[TOOLTIP-XXX]`:  
```sh
[TOOLTIP-LABEL]
l1: New tooltip text.
l2: Another new tooltip text

[TOOLTIP-ENTRY]
e1: Some more tooltip text
```

### External Translations
---

It's also possible to store additional translations to use on the fly. These are extra pieces of text you might want to translate during the running of the application, which aren't linked directly to a widget.  

```sh
[EXTERNAL]
VALUE-1: This is some translated text.
VALUE-2: This is some more translated text.
VALUE-3: This is the last piece of translated text.
```

These can then be accessed by using appJar's `.translate(key, default=None)` function.  

```python
# this function will print out some translated text
def showMessage():
    print(app.translate("VALUE-1"))
    print(app.translate("VALUE-2"))
    print(app.translate("VALUE-3"))
```  

The `default` value will be returned if no translation is found.  

### Widgets Not Supported  

* `[SCALE]`, `[TEXTAREA]`, `[METER]`, `[PIECHART]`, `[TREE]`  
    `[GOOGLEMAPS]`, `[MICROBIT]`, `[PLOT]`, `[SEPARATOR]`, `[GRIP]`  
    `[FRAME]`, `[SCROLLPANE]`, `[PANEDFRAME]`  
    These widgets are not included in translation, as they have no static text to change.  

* `[DATEPICKER]`, `[MENUBAR]`  
    These widgets have not yet been implemented.  

### Platform Support
**NB.** your platform might not support the characters you want to display.  
In which case, you'll need to install the relevant font.  

For example, to get Korean characters to show on a Raspberry Pi, try:  

```sh
    sudo apt-get install fonts-nanum
```

If you're after other languages, you can try:  

```sh
    apt-cache search chinese
``` 

And then install a likely looking font...  
