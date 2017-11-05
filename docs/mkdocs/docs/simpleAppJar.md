#appJar 2.0
---

We are moving away from adding, setting & getting widgets.  
You can now use the same function for all three tasks.

*** Need to change all widgets - to take a label flag, to show the label ***

## `.label(title, value=None)`  

| Parameter | Data type | Default | Compulsory | Description |
| --------- | --------- | ------- | ---------- | -------------------------|
| selectable    | boolean    | - | No       | Create a flashing label. |
| flash    | boolean    | - | No       | Create a selectable label. |

## `.message(title, value=None)`  

## `.entry(title, value=None)`  
    * default
    * secret
    * type
    * focus
    * limit
    * case
(    * autoRows )
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
