# Contributing
____

We are always happy to receive additions/updates/fixes to the library - simply submit a Pull Request.  

The key focusses of the project are that we have good, up-to-date documentation and reliable code.  

Therefore, in order to add new features, you should be looking to include them in both the documentation and the test suite.  

## Testing  
---
We use [Travis](https://travis-ci.org/jarvisteach/appJar) and [Coveralls](https://coveralls.io/github/jarvisteach/appJar) to ensure the code works.  
In order to ensure coverage, every new function that is added should be included in **/tests/widget_test.py**  
There are lots of functions in there that simply add widgets to the test GUI, at a minimum this ensures they are free of basic syntax errors.  
If the widget is interactive or has setters & getters, then it's useful to include a set followed by a get with an assert:

```python
app.addLabel("l1", "Message")
assert app.getLabel("l1") == "Message"
app.setLabel("l1", "New Message")
assert app.getLabel("l1") == "New Message"
app.clearLabel("l1")
assert app.getLabel("l1") == ""
```

If a function call (add/set/clear) were to fail, the test would fail. And if the ```assert``` doesn't match, the test will fail.

## Documentation
---
We've used [MkDocs](http://www.mkdocs.org) hosted on [GitHub Pages](https://pages.github.com) to build this site.  
The pages are written in Markdown - there are lots of sites out there giving advice...  

The process is fairly straightforward:  

* Identify the page you need to modify - look at the URL, the folder will be the file name  
* Find the **.md** file in **/docs/mkdocs/docs**  
* Add the relevant information  
