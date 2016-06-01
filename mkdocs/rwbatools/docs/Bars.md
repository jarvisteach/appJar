#Toolbars, Menubars & Statusbars
----
Toolbars and Menubars are features common to most GUIs, you'll be used to seeing them along the top of apps, such as MS Word.  
Statusbars are also useful features, they allow you to show information about what's going on in a GUI, usually along the bottom of the app.  

##Toolbar
___
Toolbars (sometimes known as ribbons) appear across the top og a GUI.  
They offer a series of buttons to click, which change settings/functionality in a GUI.

####Create Toolbars

* `.addToolbar(names, funcs)`  
    Will add a list of buttons along the top, in a toolbar. Each button will call the corresponding function.  
    If only one function is supplied, they will all call the same function.  
    A bundle of free images is available, if the name used for the toolbar matches the nam of an image, an image will be used.  

####Set Toolbars

* `.setToolbarImage(name, image)`  
Will set an image for the corresponding button in the toolbar.

##Menubar
___
Adds a standard Menubar along the top of the GUI
The menubar will show, once the first menu has been added.
You can add a single menu option, or a list of menu options.

####Create Menus

* `.addMenu(title, function)`  
    Adds a single menu option, that will call the specified function.

* `.addMenuList(title, names, functions, tearable=False)`  
    Will create a top-level menu, with the specified title.  
    Within the menu will be the list of names, each calling the corresponding function in the function list.  
    If only one function is provided, all menus will call the same function.  
    If the menu name is a '-', then a separator will be added to the menu.  
    If tearable is set to True, then the menu can be undocked.  

* `.createMenu(title, tearable=False)`  
    Will create a top-level menu, to add memnu items to.

* `.addMenuItem(title, item, func=None)`  
    Add a sub-menu to the named top-level menu, with the specified function
    If the menu name is a '-', then a separator will be added to the menu.

* `.addMenuSeparator(title)`  
    Add a separator to the named menu.

* `.addMenuCheckBox(title, name)`  
    Add a check box, to the named menu, with the specified name.

* `.addMenuRadioButton(title, menu, name, value)`  
    Add a radio button, to the named menu, grouped by name, with the specified value.

####Set Menus

* `.setMenuCheckBox(title, menu)`  
    Inverts the specified check box, in the named menu.

* `.setMenuRadioButton(title, menu, value)`  
    Selects the specified value, of the specified radio button, in the named menu.

####Get Menus

* `.getMenuCheckBox(title, menu)`  
    Get the value of the specified check box, from the named menu.  
    Returns True or False.

* `.getMenuRadioButton(title, menu)`  
    Get the value of the specified radio button, from the named menu.  
    Returns the value of the checked radio button.

##Statusbar
___
Adds a statusbar along the bottom of the GUI.
This can be used for easy debugging, or as info for the user.

####Create Statuses

* `.addStatus(header="", fields=1, side=None)`  
    This turns the statusbar on, and if a header is supplied, will prepend the header before every message.  
    If fields is populated, it''s possible to have multiple status bixes, each addressable by a number.  
    Side can be set as LEFT/RIGHT to make the fields appear rom the left or rigt side, otherwise they will stretch equally.


####Set Statuses
* `.setStatus(text, field=0)`  
    This updates the contents of the statusbar. Again, if a header was set when adding the statusbar, that will be prepended to the message.  
    If multiple fields were created, a position can be supplied to populate.

* `.clearStatus(field=0)`  
    Clear anything displayed in the statusbar, along with any header that might be set.

* `.setStatusWidth(width, field=0)`  
    Set the width of the specified status field.
