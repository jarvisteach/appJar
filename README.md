# appJar  

Simple tKinter GUIs in Python  

---

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]
[![Test Coverage][coveralls-image]][coveralls-link]
[![Code Health][landscape-image]][landscape-link]
[![Code Climate][climate-image]][climate-link]
[![irc][irc-image]][irc-link]

[pypi-v-image]: https://img.shields.io/pypi/v/appJar.png
[pypi-v-link]: https://pypi.python.org/pypi/appJar
[travis-image]: https://travis-ci.org/jarvisteach/appJar.svg?branch=appJar
[travis-link]: https://travis-ci.org/jarvisteach/appJar
[climate-image]: https://codeclimate.com/github/jarvisteach/appJar/badges/gpa.svg
[climate-link]: https://codeclimate.com/github/jarvisteach/appJar
[landscape-image]: https://landscape.io/github/jarvisteach/appJar/appJar/landscape.svg?style=flat
[landscape-link]: https://landscape.io/github/jarvisteach/appJar/appJar
[coveralls-image]: https://coveralls.io/repos/github/jarvisteach/appJar/badge.svg
[coveralls-link]: https://coveralls.io/github/jarvisteach/appJar
[irc-image]:https://img.shields.io/badge/irc-%23appJar-lightgrey.svg
[irc-link]:http://webchat.freenode.net/?channels=appJar&nick=appJarGuest

Download Here: https://github.com/jarvisteach/appJar/raw/appJar/releases/appJar.zip

Docs here: http://appJar.info

This provides a library for implementing easy GUIs...

### Installation:
 - Download the ZIP file (click the big green button) & unzip it
 - Add it to your path:
   - make a folder in your home directory, called PYLIB, and put appJar inside it
   - On mac/linux add this to your .bashrc: export PYTHONPATH=~/PYLIB:$PYTHONPATH
   - On Windows, add a new environment variable
 - Give it a twirl:
   - Check the docs folder, for a couple of PDFs with help.
   - Check the Lessons folder, for some example code.

### Example:
```
from appJar import gui  
app = gui("Example")  
app.addLabel("label1", "Hello World")  
app.go()  
```

or (using context managers):  

```
from appJar import gui  
with gui("Example") as app:
    app.addLabel("label1", "Hello World")  
```

or (using simple naming):  

```
from appJar import gui  
with gui("Example") as app:
    app.label("Hello World")  
```

### Reasoning:
 - Designed to be as easy as possible, yet still provide a lot of tkinter functionality
 - Provides 3 functions for most widgets:
   - add(name, value) this adds a new widget (usually with a name and a value)
   - set(name, value) this updates the value of the named widget
   - get(name) this gets the value of the named widget
 - Uses grid layout
 - When adding widgets, up to 4 numerical "positions" can be supplied:
   - column - the coloumn to appear in, starting at 0
   - row - row to appear in, stating at 0
   - columnspan - how many columns to span across
   - rowspan - how many rows to span down
 - Provides loads of extra bits and pieces outside of core tkinter
   - Some of this was from the excellent resources @ http://effbot.org
   - Some of this was from slashdot examples of how to solve common problems
   - Some of this has been incorporated from other people's modules:
     - ToolTip support form Michael Lange  
     - png support using James Wright's tkinter-png and Johann C. Rocholl's png.py libraries  
     - jpeg support using NanoJPEG from Martin J. Fiedler  

 - I've tried to get as much functionality into this library as possible, without requiring any other modules
