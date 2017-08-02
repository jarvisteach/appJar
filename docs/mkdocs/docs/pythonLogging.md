#Logging in appJar
---

**appJar** makes use of Python's built in [logging capabilities](https://docs.python.org/3.6/library/logging.html#levels).  

Logging works in a similar way to the `print()` function, except you also provide a parameter indicating the importance of the message - the logger will then only display messages of the right importance.

There are five levels of importance:  

* `CRITICAL` - a very serious problem, the GUI may well stop
* `ERROR` - a more serious problem, preventing something from happening
* `WARNING` - something unexpected happened
* `INFO` - confirmation that things are working as expected
* `DEBUG` - detailed diagnostic information

By default, **appJar** will only log messages of importance `WARNING` or above. And, by default, appJar will simply print them to the console (screen).  

**appJar** provides some useful functions for logging:

* `.logMessage(msg, level)` - log a message, of the specified importance
* `.setLogLevel(level)` - set the logging level, all messages of less importance than this will be ignored  
* `.setLogFile(fileName)` - write all log messages to the named file, instead of the console  

You can also use the following convenience functions for logging messages:

* `.critical(msg)`
* `.error(msg)`
* `.warn(msg)`
* `.debug(msg)`
* `.info(msg)`

##Logging to file
---

One of the benefits of using Python's logging capabilites, is the ability to have them logged to a file.  
By setting a `fileName`, messages will no longer appear on the screen. Instead, they will be written to the named file.  
The `logLevel` is also increased to **DEBUG**  

##External Logging
---

If you want to bypass the **appJar** functions, and use the logger directly in your code, simply request your own copy of the logger: `logger = logging.getLogger("appJar")`.  

You can then talk directly to the same logging mechanism that **appJar** uses.  

##How to use
---
The idea behind having different levels of logging, is that you don't have to remove all of your debug & testing messages. It is common to include lots of testing messages during development, and then remove them once we're satisfied the code is working. However, these might sometimes prove useful in the future, when trying to diagnose something that has gone wrong.  

With logging, you can register those messages as **DEBUG** or **INFO**. Then set the `logLevel` to be **INFO** during development, and **WARNING** once development is complete. Then, if you ever need them, you can simply change the `logLevel`.  
