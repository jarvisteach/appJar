# appJar  

## *The easiest way to create GUIs in Python.*

appJar is a framework representing a natural extension to Python's native tKinter GUI library.

Written by a teacher, in the classroom, for students.

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

## Download

<https://github.com/jarvisteach/appJar/raw/appJar/releases/appJar.zip>

## Documentation

<http://appJar.info>

## Installation

- Download the **.zip** file (see link above) & unzip it.
- Add appJar to your path:
  - Make a folder in your home directory, called PYLIB, and put appJar inside it.
  - On mac/linux add this to your .bashrc: `export PYTHONPATH=~/PYLIB:$PYTHONPATH`
  - On Windows, add a new environment variable (see tutorial [here](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html)).
- Give it a twirl:
  - Check the **docs** folder for a couple of PDFs with help, but visit the documentation website for a more complete version.
  - Check the **examples** folder for some example code.

## Example

```python
from appJar import gui  
app = gui("Example")  
app.addLabel("label1", "Hello World")  
app.go()  
```

or (using context managers):  

```python
from appJar import gui  
with gui("Example") as app:
    app.addLabel("label1", "Hello World")  
```

or (using simple naming):  

```python
from appJar import gui  
with gui("Example") as app:
    app.label("Hello World")  
```

## Reasoning

- Designed to be as easy as possible, yet still provide a lot of tkinter functionality.
- Provides 3 functions for most widgets:
  - add(name, value)
    - Adds a new widget (usually with a name and a value).
  - set(name, value)
    - Updates the value of the named widget.
  - get(name)
    - Gets the value of the named widget.
- Uses grid layout.
- When adding widgets, up to 4 numerical "positions" can be supplied:
  - column
    - The column to appear in, starting at 0.
  - row
    - The row to appear in, stating at 0.
  - columnspan
    - How many columns to span across.
  - rowspan
    - How many rows to span down.
- Provides loads of extra bits and pieces outside of core tkinter.
  - Some of this was from the excellent resources @ <http://effbot.org>.
  - Some of this was from slashdot examples of how to solve common problems.
  - Some of this has been incorporated from other people's modules:
    - ToolTip support form Michael Lange.
    - png support using James Wright's tkinter-png and Johann C. Rocholl's png.py libraries.
    - jpeg support using NanoJPEG from Martin J. Fiedler.
- I've tried to get as much functionality into this library as possible, without requiring any other modules.

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
