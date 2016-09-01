http://www.ferg.org/thinking_in_tkinter/all_programs.html

The 4 basic precepts of GUI programming:
* Specify how you want the UI to *look*
* Decide what you want the UI to *do*
* Link the *looking* with the *doing*
* Write code that *waits* for user input

Looks - positioning *widgets* on the screen
Actions - code *event handlers* that deal with any user actions (clicking buttons, etc)
Linkning - *bind* event handlers with widgets, requires 3 things:
* type of event
* a widget
* event-handler routine
Waiting code - lives in the *event loop*, this sees every event that happens in a GUI and ignores most of them. However, if an event is bound to a handler, then the event is passed on

Containers vs. Widgets
Creaintg GUI objects & associating them with a parent
Packing

