# appJar 2.0  

We are moving away from adding, setting & getting widgets.  
You can now use the same function for all three tasks.  

## Operation  

```
app.label("title", "text")      # ADD a label
app.label("title", "text_2")    # SET a label
print(app.label("title"))       # GET a label
```  

## Parameters

Each widget will take the following parameters:

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| title | string | - | Yes | A unique identifier for the widget. |
| value | string | - | Yes | The text to display in the widget. |
| row | integer | next row | No | The grid row to place the widget in. |
| column | integer | 0 | No | The grid column to place the widget in. |
| rowspan | integer | 1 | No | The number of grid rows to stretch the widget across. |
| colspan | integer | 1 | No | The number of grid columns to stretch the widget across. |


## Label  
A widget for displaying text in a GUI.  

* `.label(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| type | string | standard | No | Set to "selectable" or "flash" to create different labels. |


## Message 
A widget for displaying mukti-line text in a GUI.  

* `.message(title, value=None)`  

## Entry  
An interactive widget, for capturing user input in a GUI.  

* `.entry(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| default | string | - | No | Sets default text to display in an empty entry. |
| secret | boolean | False | No | Configures the entry box to show stars instead of characters. |
| type | string | standard | No | Sets the type of the entry box. |
| focus | boolean | False | No | Should the entry box be given focus? |
| limit | integer | - | No | Sets a maximum limit on the number of characters taht can be entered. |
| case | string | - | No | Set to "upper" to force upercase or "lower" to force lowercase. |
| autorows | integer | - | No | If the type is "auto" this will set the number of rows to show. |

## Text  
An editable box for entering text.  

* `.text(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| scroll | boolean | - | No | Will configure this as a scrollable text area. |

## Button  
A clickable button for triggering events.  

* `.button(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| image | string | - | No | A path to an image to show in the button. |
| icon | string | - | No | The name of an icon to show in the button. |

## Link  
A clickable **hyperlink** to trigger events or launch webpages.  
If the `value` is set to a function, the function will be called, otherwise a browser will be launched.  

* `.link(title, value=None)`  

## Check  
A checkbox style widget, that can be checked/unchecked.  

* `.check(title, value=None)`  

## Radio  
A combination widget, where only one of the adio buttons can be clicked.  

* `.radio(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| selected | boolean | False | No | Should this radio be selected? |

## Option  
When clicked, displays a drop-down of items, one of which can be selected.  

* `.option(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| type | string | standard | No | Set this to `ticks` if you want tickable options. |

## Spin  
Shows a single value, with arrows to scroll up or down, allowing the user to change the value.  

* `.spin(title, value=None, endValue=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| endValue | integer | - | No | If specified, value & endValue will be used to generate a range. |
| pos | integer | - | No | The position of an item to select. |
| item | string | - | No | The name of an item to select. |

## List
Displays a list of items, one (or more than one) of which can be selected.  

* `.list(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| rows | integer | - | No | If specified, value & endValue will be used to generate a range. |
| multi | boolean | False | No | Set the list to be multi-selectable. |
| group | boolean | False | No | Set the list to be part of a group. |

## Slider  
A draggable widget, where the user can select a number from a range.  

* `.slider(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| vert | boolean | False | No | Sets the slider to be vertically oriented. |
| increment | integer | False | No |  |
| interval | integer | False | No |  |
| show | boolean | False | No | Show the slider's value above the slider. |
| change | function | - | No | Set a function to call when the slider is changed. |

## Meter  

* `.meter(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| tyoe | string | standard | No | Choose the type of meter: `standard`, `split` or `dual`. |
| fill | boolean | False | No | Set the fill colour(s) for the slider. |

## Grip  
Displays a draggable icon, which allows the GUI to be moved.  

* `.grip(title, value=None)`  

## Separator  
Displays a line, giving visual separation in the GUI.  

* `.separator(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| direction | string | horizontal | No | Set the orientation of the searator: `horizontal    or `vertical`. |

## Image  
Displays a picture.  

* `.image(title, value=None)`

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| type | string | standard | No | The type of image, one of: `icon`, `data` or `standard`. |
| fmt | string | - | No | If the `type` is `data` this will be used to determine the file type. |
| compound | boolean | False | No | If set to `True` will show the title of the image as well.  
| speed | integer | - | No | If this is an animated image, the FPS to animate the image at. |
| over | string | None | No | The path to an alternative image to show, when the mouse goes over the image. |
| submit | function | None | No | A function to call, when the image is clicked. |
| map | dictionary| - | No | A dictionary of name:coordinates to use as an image map. `submit` must also be set. |

## Properties  

* `.properties(title, value=None)`

## Date  

* `.date(title, value=None)`

