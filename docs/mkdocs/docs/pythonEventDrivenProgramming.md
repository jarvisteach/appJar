#Event-Driven Programming
---

When programming a GUI, you have to think slightly differently...  
Normally, your code is executed sequentially.  
You might branch off, using a decision.  
And you may even introduce some loops.  
But ultimately your code is executed from top-to-bottom.  

GUI programming is different.  
In a GUI, a loop is constantly running in the background, waiting for the user to click something.  
This is called the event loop.  
Every time something happens to the GUI, the event loop deals with it.  

