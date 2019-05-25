# Stylesheets
---

One great idea we've seen recently is trying to replicate web page stylesheets in appJar.  

The basic concept behind stylesheets is that different parts of a webpage are given IDs, which are used to style that tag.

The same can be acheived in appJar.

## Making the Stylesheet
---

The stylesheet will consist of a number of dictionaries, each with the relevant style elements:

```python
body = { 
    'geom':'400x200', 
    'font':{'size':14, 'family':'helvetica', 'weight':'normal'},
    'bg':'blue',
    'fg':'red'
}

heading = { 
    'font':{'size':20, 'family':'times', 'weight':'bold', 'underline':True, 'slant':'italic'},
    'bg':'red',
    'fg':'yellow'
}

text = { 
    'font':{'size':16, 'family':'times', 'weight':'normal', 'slant':'roman'},
    'bg':'orange',
    'fg':'red',
    'width':300 # set the aspect for the message box
}   
```

Save this with an appropriate name, eg. `style.py`


## Applying the Stylesheet
---

To apply the stylesheet, you need to import it, and then set-up the IDs:

```python
from appJar import gui 
import style

with gui('Demo Stylesheet', **style.body) as app:
    app.label("Stylesheet Demonstration", **style.heading)
    app.message("This demonstration gives an example of how "
                + "stylesheets can be replicated in appJar.", **style.text)
    app.label("Some other text, without style.")
```

The IDs are slightly more complicated than regular CSS, but they just mean get the named variable from the `style` file.  
`**` is special python syntax which *unpacks* the variable (replaces it with the contents of the dictionary).


## Getting Fancy
---

If you want to take things a bit further, and use a *clever* name for your stylesheet, you can either:

* import it **as** a simpler name:
```python
# stylesheet saved as: exampleStylesheet2.py
import exampleStylesheet2 as style
```

* Or use the `imp` library to do a special import:

```python
import imp
# stylesheet saved as: myAppJarStylesheet.css
style = imp.load_source('style', 'myAppJarStylesheet.css')
```
