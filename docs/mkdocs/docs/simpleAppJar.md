# appJar v1.0  

A feature we are working towards in the 1.0 release, is a simplified way of adding, setting & getting widgets.  
Each widget will have a single function that supports all three actions.  
This is in the current release, but only in BETA.  

## Operation  
---

```python
app.label("title", "text")      # ADD a label if title is new
app.label("title", "text_2")    # SET a label if title exists
print(app.label("title"))       # GET a label
```  

There are two parameters being used here:  

| Parameter | Data type | Description |
| --------- | --------- | ------------|
| title | string | A unique identifier for that widget type. |
| value | string | Any relevant information for the widget. |

The logic is as follows:

* If `title` doesn't exist - **ADD** the widget.  
* If `title` already exists and a `value` is specified - **SET** the widget.  
* If `title` already exists and a `value` is not specified - **GET** the widget.  

## Position  
---

When adding a widget, it's also possible to set its position.  

```python
app.label("title", "text", row=2, column=4, rowspan=3)      # ADD a label
```

The following positional parameters are available when adding widgets:  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| row | integer | &lt;next row&gt; | The grid row to place the widget in. |
| column | integer | 0 | The grid column to place the widget in. |
| rowspan | integer | 1 | The number of grid rows to stretch the widget across. |
| colspan | integer | 1 | The number of grid columns to stretch the widget across. |

Alternatively, they can be specified as a list/tuple:

```python
app.label("title0", "text", pos=(1, 0))      # ADD a label
app.label("title2", "text", pos=(1, 1))      # ADD a label
app.label("title3", "text", pos=(2, 0, 2))   # ADD a label
```

## Events  
----

Most of the widgets also have some support for events (see the [events page](/pythonEvents/#types-of-event) for more information).  
**NB.** the parameter is only the name of the function, don't include any brackets.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| submit | function | None | A function to call when the widget is *submitted*. |
| change | function | None | A function to call when the widget is *changed*. |
| drop | boolean/function | None | Update the widget with *dropped* data if True, otherwise call the function. |

`submit` & `change` will pass the name of the widget to the function, `drop` will pass the data to the function:  

```python
def update(name):
    if name == "size":
        updateSize()
    elif name == "toppings":
        updateToppings()

app.listbox("size", ["small", "medium", "large"], change=update)
app.listbox("toppings", ["corn", "cheese", "peppers"], change=update)
app.image("img1", "placeholder.gif", drop=True)
```

## Label  
----

A widget for displaying text in the GUI.  

* `.label(title, value=None)`  
    The `value` will be the text to show in the label.  
    Labels can receive a `submit` parameter, making them clickable.  
    Labels can receive `drop` data.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| kind | string | `standard` | Set to `selectable` or `flash` to create different labels. |


## Message 
A widget for displaying multi-line text in the GUI.  

* `.message(title, value=None)`  
    The `value` will be the text to show in the message.  
    Messages can receive `drop` data.  

## Entry  
---
An interactive widget, for capturing user input in the GUI.  

* `.entry(title, value=None)`  
    A `value` is not required, but if provided will populate the entry.  
    Entries can receive a `change` parameter, and can link a `submit` parameter to pressing <ENTER>.  
    Entries can receive `drop` data.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| label | boolean | False | Adds a Label before the widget. |
| kind | string | `standard` | One of: `standard`, `file`, `direcory`, `numeric`, `auto` or `validation`. |
| secret | boolean | False | Configures the entry box to show stars instead of characters. |
| default | string | None | Sets default text to display in an empty entry. |
| focus | boolean | False | Should the entry box be given focus? |
| rows | integer | 10 | If the kind is `auto` this will set the number of rows to show. |

There are also some validation settings that can be applied:  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| limit | integer | None | Sets a maximum limit on the number of characters taht can be entered. |
| case | string | None | Set to `upper` to force upercase or `lower` to force lowercase. |

## Text  
---
An interactive widget, for capturing multi-line user input in the GUI.  

* `.text(title, value=None)`  
    A `value` is not required, but if provided will populate the text.  
    Text boxes can receive a `change` parameter.  
    Text boxes can receive `drop` data.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| scroll | boolean | False | Will configure this as a scrollable text area. |

## Button  
---

A clickable button for triggering events.  

* `.button(title, value=None)`  
    The `value` should be a function to call when the button is pressed.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| image | string | None | A path to an image to show in the button. |
| icon | string | None | The name of an icon to show in the button. |

## Link  
---
A clickable **hyperlink** to trigger events or launch webpages.  

* `.link(title, value=None)`  
    The `value` can be set to a function to call when the link is clicked, or a valid URI to open in a browser.  

## Check  
---
A checkbox style widget, that can be checked/unchecked.  

* `.check(title, value=None)`  
    The `value` should be True or False, indicating if the check starts selected or not.  
    Check boxes can receive a `change` parameter.  

## Radio  
---
Radio buttons are used in groups, only one of them can be checked.  
By default, the first radio button added to a group will be selected.

* `.radio(title, value=None)`  
    The `title` is the radio button's group.  
    The `value` is the text to display next to this radio button.  
    Radio buttons can receive a `change` parameter, it will be linked to all radio buttons of the same `title`.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| selected | boolean | False | Should this radio be selected? |

## Option  
---
When clicked, displays a drop-down of items, one of which can be selected.  

* `.option(title, value=None)`  
    The `value` should contain a list of items to display in the drop-down.  
    Options can receive a `change` parameter.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| kind | string | `standard` | Set this to `ticks` if you want tickable options. |

## Spin  
---
Shows a single value, with arrows to scroll up or down, allowing the user to change the value.  

* `.spin(title, value=None, endValue=None)`  
    If only the `value` is set, it should be a list of values to display in the spin box.  
    If `endValue` is also set, then both parameters should be integers, and appJar will generate a range of whole numbers between the two values.  
    Spin boxes can receive a `change` parameter.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| endValue | integer | None | If specified, value & endValue should be integers, and will be used to generate a range. |
| pos | integer | 0 | The position of an item to select. |
| item | string | None | The name of an item to select. |

## Listbox
---

Displays a list of items, one (or more than one) of which can be selected.  

* `.listbox(title, value=None)`  
    The `value` should contain a list of items to display in the listbox.  
    Listboxes can receive a `change` parameter.  
    Listboxes can receive `drop` data.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| rows | integer | None | Specifies how many rows to display in the listbox. |
| multi | boolean | False | Set the listbox to be multi-selectable. |
| group | boolean | False | Set the listbox to be part of a group. |

## Slider  
---
A draggable widget, where the user can select a number from a range.  

* `.slider(title, value=None)`  
    The `value` is optional - it will set the starting position of the slider.  
    Sliders can receive a `change` parameter.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| direction | string | `horizontal` | Set the direction of the slider: `vertical` or `horizontal`. |
| show | boolean | False | Show the slider's value above the slider. |
| increment | integer | 10 | Configures how much the slider jumps, when the torugh is clicked. |
| interval | integer | None | Configures the slider to show interval values, along its length. In steps of the value specified. |

## Meter  
---
Various styles of progress meter.  

* `.meter(title, value=None)`  
    For `standard` and `split` meters `value` should be a number between 0 and 100.  
    For `dual` meters, `value` should be a list of two numbers, each between 0 and 100.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| text | string | None | Set text to show on the meter. |
| kind | string | `standard` | Choose the kind of meter: `standard`, `split` or `dual`. |
| fill | boolean | None | Set the fill colour(s) for the slider (a list of two colours for `split` & `dual`). |

## Grip  
---
Displays a draggable icon, which allows the GUI to be moved.  

* `.grip(title, value=None)`  
    A `value` is not required.  

## Separator  
---
Displays a line, giving visual separation in the GUI.  

* `.separator(title, value=None)`  
    A `value` is not required.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| direction | string | horizontal | Set the orientation of the separator: `horizontal` or `vertical`. |

## Image  
---

Displays a picture.  

* `.image(title, value=None)`
    The `value` should be the image file, icon or data to show.  
    Images can receive a `submit` parameter, making them clickable.  
    Images can receive `drop` data.  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| kind | string | `standard` | The kind of image, one of: `icon`, `data` or `standard`. |
| fmt | string | None | If the `kind` is `data` this will be used to determine the file type. |
| compound | string | None | Can be set to a position to show the title as well (`top`, `bottom`, `left`, `right` or `center`). |
| speed | integer | None | If this is an animated image, the FPS to animate the image at. |
| over | string | None | The path to an alternative image to show, when the mouse goes over the image. |
| map | dictionary| None | A dictionary of name:coordinates to use as an image map. `submit` must also be set. |

## Properties  
---
Displays a list of checkboxes, stored in a dictionary.  

* `.properties(title, value=None)`
    The `value` should contain a dictionary of names and booleans.  
    Properties can receive a `change` parameter.  

## Date  
---
Displays a simple date picker widget.  

* `.date(title, value=None)`
    The `value` should contain a date object.  
    Date pickes can receive a `change` parameter.  

## Canvas  
---
Displays a the canvas widget.  

* `.canvas(title)`
    Creates a canvas with the specified title. 

## popUp  
---

Displays a popUp.  

* `.popUp(title, message, kind="info", parent=None)`  
    This will show any of the availabel popUps.  
    `title`  will be displayed in the title bar.
    `message` will be displayed as the text of the popUp.  
    `kind` defaults to `info`, but can be any of: `error`, `warning`, `yesno`, `question`, `ok`, `retry`, `string`, `integer`, `float`, `text` or `number`.  
    `parent` allows you to link this popUp to a named SubWindow, instead of the main window.  

---

# GUI Properties  
---

* `.title` - pass a string for the title of the GUI  
* `.icon` - pass the path to an icon file  
* `.transparency` - pass a percentage (between 0 & 100) to set the transparency  
* `.visible` - pass either `True` or `False`  

* `.padding` - pass a tuple containing the x & y padding or a single integer for both x & y  
* `.inPadding` - pass a tuple containing the x & y padding or a single integer for both x & y  
* `.guiPadding` - pass a tuple containing the x & y padding or a single integer for both x & y  

* `.size` - pass a tuple containing the width & height (or the string `fullscreen`)  
* `.location` - pass a tuple containing the x & y coordinates (or the string `CENTER`)  
* `.fullscreen` - pass either `True` or `False`  
* `.resizable` - pass either `True` or `False`  

* `.sticky`
* `.stretch`
* `.expand`

* `.fg`
* `.bg`
* `.font`
* `.buttonFont`
* `.labelFont`

* `.row`
