# Redirecting Output  
---

In **appJar** it's possible to have your print statements go directly to a [TextArea](/inputWidgets/#textarea) widget.  

Once you have added your `TextArea`, call the function `.redirectOutput(text)` passing in the name of the `TextArea` as a parameter.

Then any time you call `print()` it will display the text in the `TextArea`.  

**NB.** output redirection isn't as smart as print. You can only pass a single string, so you'll need to concatenate values together, and maybe cast them as strings as well (see the example below).  

* `.redirectOutput(title, end=True)`
This will cause all calls to `print` to go to the named `TextArea`.  
Set `end` to `False` if you want the new text to be shown at the top of the `TextArea`, otherwise it defaults to appending to the bottom.  

* `.cancelRedirectOutput()`
This will cause all calls to `print` to go to the terminal.  

This can also be done through the call to `text() - set ` `redirect` parameter to `True` or `False` to append to the end/beginning.   

``` python
from appJar import gui

# global variable to store the count
counter = 20

def countdown():
    global counter
    if counter > 0:
        # cast the counter as a string & concatenate with 'Counter: '
        print("Counter: " + str(counter))
        counter -= 1

def press():
    app.registerEvent(countdown)

with gui() as app:
    app.label('Logging Test')
    app.text('message')
    app.redirectOutput('message', end=False)
    app.button('GO!!!', press)
```
