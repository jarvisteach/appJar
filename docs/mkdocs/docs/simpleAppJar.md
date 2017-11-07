# appJar 2.0  

We are trialling a new approach for adding, setting & getting widgets.  
Each widget now has a single function that supports all of these actions.  

## Operation  

```
app.label("title", "text")      # ADD a label if title is new
app.label("title", "text_2")    # SET a label if title exists
print(app.label("title"))       # GET a label
```  

There are two parameters being used here:  

| Parameter | Data type | Description |
| --------- | --------- | ------------|
| title | string | A unique identifier for the widget. |
| value | string | The relevant information for the widget. |

If no `value` is specified, then the `value` is returned from the widget.  
If no idget with that `title` exists, it is created.  
Otherwise, the existing widget is updated.  

When adding a widget, it's also possible to set its position.  

```
app.label("title", "text", row=2, column=4, rowspan=3)      # ADD a label
```

The following parameters are available when adding widgets:  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| row | integer | next row | The grid row to place the widget in. |
| column | integer | 0 | The grid column to place the widget in. |
| rowspan | integer | 1 | The number of grid rows to stretch the widget across. |
| colspan | integer | 1 | The number of grid columns to stretch the widget across. |

Each widget also supports its own optional parameters when adding (see below).  

## Label  
A widget for displaying text in the GUI.  
`value` will be the text to show in the label.  

* `.label(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| type | string | `standard` | Set to `selectable` or `flash` to create different labels. |


## Message 
A widget for displaying multi-line text in the GUI.  
`value` will be the text to show in the message.  

* `.message(title, value=None)`  

## Entry  
An interactive widget, for capturing user input in the GUI.  
`value` is not required when adding an entry.  

* `.entry(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| default | string | None | Sets default text to display in an empty entry. |
| secret | boolean | False | Configures the entry box to show stars instead of characters. |
| type | string | `standard` | Sets the type of the entry box. |
| focus | boolean | False | Should the entry box be given focus? |
| limit | integer | - | Sets a maximum limit on the number of characters taht can be entered. |
| case | string | None | Set to `upper` to force upercase or `lower` to force lowercase. |
| autorows | integer | 10 | If the type is `auto` this will set the number of rows to show. |

## Text  
An interactive widget, for capturing multi-line user input in the GUI.  
`value` is not required when adding an entry.  

* `.text(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| scroll | boolean | False | Will configure this as a scrollable text area. |

## Button  
A clickable button for triggering events.  
`value` will be the function to call.  

* `.button(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| image | string | None | A path to an image to show in the button. |
| icon | string | None | The name of an icon to show in the button. |

## Link  
A clickable **hyperlink** to trigger events or launch webpages.  
If the `value` is set to a function, the function will be called, otherwise a browser will be launched.  

* `.link(title, value=None)`  

## Check  
A checkbox style widget, that can be checked/unchecked.  
`value` should be True or False, indicating if the check starts selected or not.  

* `.check(title, value=None)`  

## Radio  
A combination widget, where only one of the adio buttons can be clicked.  

* `.radio(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| selected | boolean | False | Should this radio be selected? |

## Option  
When clicked, displays a drop-down of items, one of which can be selected.  

* `.option(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| type | string | `standard` | Set this to `ticks` if you want tickable options. |

## Spin  
Shows a single value, with arrows to scroll up or down, allowing the user to change the value.  

* `.spin(title, value=None, endValue=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| endValue | integer | - | If specified, value & endValue will be used to generate a range. |
| pos | integer | 0 | The position of an item to select. |
| item | string | None | The name of an item to select. |

## List
Displays a list of items, one (or more than one) of which can be selected.  

* `.list(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| rows | integer | - | If specified, value & endValue will be used to generate a range. |
| multi | boolean | False | Set the list to be multi-selectable. |
| group | boolean | False | Set the list to be part of a group. |

## Slider  
A draggable widget, where the user can select a number from a range.  

* `.slider(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| vert | boolean | False | Sets the slider to be vertically oriented. |
| show | boolean | False | Show the slider's value above the slider. |
| increment | integer | 10 | Configures how much the slider jumps, when the torugh is clicked. |
| interval | integer | - | Configyres the scale to show interval values, along its length. In steps of the value specified. |
| change | function | - | Set a function to call when the slider is changed. |

## Meter  
Various styles of progress meter.  
For `standard` and `split` meters `value` should be between 0 and 100.  
For `dual` meters, `value` should be alist of two values, each between 0 and 100.  

* `.meter(title, value=None, text=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| text | string | None | Set text to show on the meter. |
| type | string | `standard` | Choose the type of meter: `standard`, `split` or `dual`. |
| fill | boolean | False | Set the fill colour(s) for the slider (a list of two colours for `split` & `dual`). |

## Grip  
Displays a draggable icon, which allows the GUI to be moved.  

* `.grip(title, value=None)`  

## Separator  
Displays a line, giving visual separation in the GUI.  

* `.separator(title, value=None)`  

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| direction | string | horizontal | Set the orientation of the searator: `horizontal    or `vertical`. |

## Image  
Displays a picture.  

* `.image(title, value=None)`

| Parameter | Data type | Default | Description |
| --------- | --------- | ------- | ------------|
| type | string | `standard` | The type of image, one of: `icon`, `data` or `standard`. |
| fmt | string | - | If the `type` is `data` this will be used to determine the file type. |
| compound | boolean | False | If set to `True` will show the title of the image as well.  
| speed | integer | - | If this is an animated image, the FPS to animate the image at. |
| over | string | None | The path to an alternative image to show, when the mouse goes over the image. |
| submit | function | None | A function to call, when the image is clicked. |
| map | dictionary| - | A dictionary of name:coordinates to use as an image map. `submit` must also be set. |

## Properties  

* `.properties(title, value=None)`

## Date  

* `.date(title, value=None)`

