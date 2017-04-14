#General Guidance
---

##Navigating the Docs  
The onine documentation aims to be as consistant as possible.  

There are two main sections:  

* **Fillings** - these are things you can add to the GUI  
* **Configuration** - these are ways of changing how the GUI looks or operates  

Plus some extras:  

* **Examples** - this will slowly become a source of sample applications  
* **Help** - more general Python guidance, with a couple of useful extras, and information about appjar  

###Fillings  
These are things you can add to the GUI:  

* **Widgets** - the various interface elements that can be included in a GUI  
* **Images** - a specific section on how to manage images in a GUI  
* **Sounds** - a section on how to get your GUI to make some noise  
* **Bars** - menubars, statusbars & toolbars that can be added to your GUI  
* **Pop-ups** - the different pop-ups that can be shown  
* **Splashscreen** - a splashscreen to show at loadtime  
* **Special Characters** - guidance on how to include special characters  
* **Beta widgets** - some other available widgets, just not quite finished  

###Configuration  
These are ways of changing how the GUI looks or operates:  

* **Arranging Widgets** - guidance on how to change the way widgets are laid out in the GUI  
* **Grouping Widgets**a - various containers for grouping widgets together in a GUI  
* **Changing Widgets** - how to change the way widgets look & act  
* **GUI Options** - how to change the general appearance/set-up of the entire GUI  
* **GUI Events** - how to get the GUI to respond to various user interactions or repeat things in the background   
* **Drag'n Drop** - how to implement drag and drop functionality  
* **Internationalisation** - how to support multiple languages in your GUI  

##Understanding the Docs  

When I first started appJar, I didn't really know any Python. I grew up on Pascal & Java, followed by JavaScript & PHP - appjar is therefore all in [CamelCase](https://en.wikipedia.org/wiki/Camel_case).

Also, because of this, the concept of [named parameters](https://en.wikipedia.org/wiki/Named_parameter) is also not really used (except in the more recent parts). Again, I learnt programming without this concept, and generally teach programming without this concept. You'll therefore find that sometimes you have to make two-or-three function calls, to acheive something that could be done with one - if I had more named parameters.

I've tried to keep function names standardised:

* `.add XXX()` - to add something to the GUI   
* `.set XXX()` - to change something in the GUI  
* `.set XXX YYY()` - to change some property of something in the GUI  
* `.get XXX()` - to get something from the GUI

When the docs list the parameters available on a function, any with an `=` means they are optional, with the dafault being shown.  

For example:  

* `setProperty(title, prop, value=False, callFunction=True)`  
    This has two required parameters `title` & `prop` - must be set (the title of the *Properties* group and a specific *property*)  
    And two optional parameters `value` & `callFunction` - if you don't pass `value` it will be set to False  

    So, you could simply call: `.setProperty("Toppings", "cheese")` to get rid of cheese.  
    Or, if you want cheese: `.setProperty("Toppings", "cheese", True)`.  

    You don't need to name the parameters, as they are always listed in the required order.  

    However, if you do want to name your parameters, feel free: `.setProperty("Toppings", "cheese", callFunction=False)`  

    In fact, it can make your life much easier: `.addLabel("l1", "Main Title", colspan=5)` - saves you having to type in the row or column values.  

##Deprecation

appjar has been going so long, that some of the early decisions have turned out to be bad ones...  
Some functions have now been [deprecated](https://en.wikipedia.org/wiki/Deprecation) - you can still use them, but appJar will warn you that you should be using something else.  
