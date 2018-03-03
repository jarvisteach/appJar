#General Guidance
---

##Navigating the Docs  
The online documentation aims to be as consistant as possible.  

There are two main sections:  

* **Fillings** - these are things you can add to the GUI  
* **Configuration** - these are ways of changing how the GUI looks or operates  

###Fillings  
These are things you can add to the GUI:  

* **Widgets** - the various interface elements that can be included in a GUI  
* **Images** - a specific section on how to manage images in a GUI  
* **Sounds** - a section on how to get your GUI to make some noise  
* **Bars** - menubars, statusbars & toolbars that can be added to your GUI  
* **Pop-ups** - the different pop-ups that can be shown  
* **Multiple Windows** - information on creating separate windows  
* **Splashscreen** - a splashscreen to show at loadtime  
* **Special Characters** - guidance on how to include special characters  
* **Beta widgets** - some other available widgets, just not quite finished  

---
<div style='text-align: center;'>
*Advertisement&nbsp;<sup><a href="/advertising">why?</a></sup>*
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
    style="display:block"
    data-ad-format="fluid"
    data-ad-layout-key="-gw-13-4l+6+pt"
    data-ad-client="ca-pub-6185596049817878"
    data-ad-slot="5627392164"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
---

###Configuration  
These are ways of changing how the GUI looks or operates:  

* **GUI Options** - options for configuring general GUI settings  
* **Widgets** - options for configuring the layout and look & feel of widgets  
* **Events** - options for delaying actions, making them repeat or run in the background  
* **Internationalisation** - how to support multiple languages in your GUI  
* **Logging** - how to turn on/off appJar's logging capabilities  
* **Command Line Arguments** - hw t use various command line arguments  
* **ttk** - how to enable ttk support  

##Understanding the Docs  

When I first started appJar, I didn't really know any Python. I grew up on Pascal & Java, followed by JavaScript & PHP - appjar is therefore all in [CamelCase](https://en.wikipedia.org/wiki/Camel_case).

Also, because of this, the concept of [named parameters](https://en.wikipedia.org/wiki/Named_parameter) is also not really used (except in the more recent parts). Again, I learnt programming without this concept, and generally teach programming without this concept. You'll therefore find that sometimes you have to make two-or-three function calls, to achieve something that could be done with one - if I had more named parameters.

I've tried to keep function names standardised:

* `.add XXX()` - to add something to the GUI   
* `.set XXX()` - to change something in the GUI  
* `.set XXX YYY()` - to change some property of something in the GUI  
* `.get XXX()` - to get something from the GUI

When the docs list the parameters available on a function, any with an `=` means they are optional, with the default being shown.  

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

##Beta Code

Some elements of appjar are in [beta](https://en.wikipedia.org/wiki/Software_release_life_cycle#BETA). This means you can use them, and they *generally* work - but you may come across issues or they may change in the future. Generally, the beta code works pretty well - it wouldn't be included if it didn't. But, equally, we know its not perfect - [drag'n drop](/pythonDnD) will keep growing & improving, and the [table](/pythonDevWidgets/#table) needs some work.  

So, please use them, and let us know any issues or improvements you'd like...  
