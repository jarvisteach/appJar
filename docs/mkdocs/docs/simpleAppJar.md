#appJar 2.0
---

We are moving away from adding, setting & getting widgets.  
You can now use the same function for all three tasks.

*** Need to change all widgets - to take a label flag, to show the label ***

## `.label(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| title | string | - | Yes | A unique identifier for the label. |
| value | string | - | Yes | The text to display in thelabel. |
| selectable | boolean | - | No | Create a flashing label. |
| flash | boolean | - | No | Create a selectable label. |
| row | integer | <next row> | No | The grid row to place the widget in. |
| column | integer | 0 | No | The grid column to place the widget in. |
| rowspan | integer | 1 | No | The number of grid rows to stretch the widget across. |
| colspan | integer | 1 | No | The number of grid columns to stretch the widget across. |

## `.message(title, value=None)`  

## `.entry(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | ------------|
| title | string | - | Yes | A unique identifier for the label. |
| value | string | - | Yes | The text to display in thelabel. |

| default | string | - | No | Sets default text to display in an empty entry. |
| secret | boolean | False | No | Configures the entry box to show stars instead of characters. |
| type | string | "standard" | No | Sets the type of the entry box. |
| focus | boolean | False | No | Should the entry box be given focus? |
| limit | integer | - | No | Sets a maximum limit on the number of characters taht can be entered. |
| case | string | - | No | Set to "upper" to force upercase or "lower" to force loercase. |
| autorows | integer | - | No | If the type is "auto" this will set the number of rows to show. |

| row | integer | <next row> | No | The grid row to place the widget in. |
| column | integer | 0 | No | The grid column to place the widget in. |
| rowspan | integer | 1 | No | The number of grid rows to stretch the widget across. |
| colspan | integer | 1 | No | The number of grid columns to stretch the widget across. |

## `.text(title, value=None)`  
    * scroll

## `.button(title, value=None)`  
    * image
    * icon
## `.link(title, value=None)`  
## `.check(title, value=None)`  
## `.radio(title, value=None)`  
    * selected

## `.option(title, value=None)`  
    * type
## `.spin(title, value=None, endValue=None)`  
    * pos
    * item

## `.list(title, value=None)`  
    * rows
    * multi
    * group 

## `.slider(title, value=None)`  
    * vert
    * increment
    * interval
    * show
    * change
## `.meter(title, value=None)`  
    * fill
    * type

## `.grip(title, value=None)`  
## `.separator(title, value=None)`  
    * direction

## `.image(title, value=None)`
    * compound
    * type
    * speed
    * over
    * submit
    * map
    * compound
    * fmt

## `.properties(title, value=None)`
## `.date(title, value=None)`
