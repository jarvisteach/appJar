# Logging in appJar
---

**appJar** makes use of Python's built in [logging capabilities](https://docs.python.org/3.6/library/logging.html#levels).  

Logging works in a similar way to the `print()` function, except you also provide a parameter indicating the importance of the message - the logger will then only display messages of the right importance.

There are five levels of importance:  

* `CRITICAL` - a very serious problem, the GUI may well stop
* `ERROR` - a more serious problem, preventing something from happening
* `WARNING` - something unexpected happened
* `INFO` - confirmation that things are working as expected
* `DEBUG` - detailed diagnostic information
* `TRACE` - used by appJar to log DEBUG information

By default, **appJar** will only log messages of importance `WARNING` or above. And, by default, appJar will simply print them to the console (screen).  

**appJar** provides some useful functions for logging:

* `.logMessage(msg, level, *args)` - log a message, of the specified importance, with any specified arguments (see below)  
* `.setLogLevel(level)` - set the logging level, all messages of less importance than this will be ignored  
* `.setLogFile(fileName)` - write all log messages to the named file, instead of the console  

You can also use the following convenience functions for logging messages:

* `.critical(msg, *args)`
* `.error(msg, *args)`
* `.warn(msg, *args)`
* `.info(msg, *args)`
* `.debug(msg, *args)`
* `.trace(msg, *args)`

#### Optional Arguments:  

* `*args` allows you to use a **string formatter** with your message.  
This can speed things up slightly, as it avoids unnecessary string concatenations, as well as automatically casting all variables to Strings:  

```
name = app.getEntry("name")
location = app.getEntry("location")
app.debug("User %s, has accessed the app from %s", name, location)
```

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

## Logging to file
---

One of the benefits of using Python's logging capabilities, is the ability to have them logged to a file.  
By setting a `fileName`, messages will no longer appear on the screen. Instead, they will be written to the named file.  
The `logLevel` is also increased to **DEBUG**  

## Command Line Arguments  
---

It's possible to set the starting log level using a [command line argument](/pythonCommandLine/).  
Simply use the first letter of the desired log level as an argument when you start your app:  
```sh
python3 logging.py -d  # log DEBUG messages and above
```

It's also possible to set the file name to log to:  
```sh
python3 logging.py -f debug.log  # log messages to a file called debug.log
```

## External Logging
---

If you want to bypass the **appJar** functions, and use the logger directly in your code, simply request your own copy of the logger: `logger = logging.getLogger("appJar")`.  

You can then talk directly to the same logging mechanism that **appJar** uses.  

## How to use
---
The idea behind having different levels of logging, is that you don't have to remove all of your debug & testing messages. It is common to include lots of testing messages during development, and then remove them once we're satisfied the code is working. However, these might sometimes prove useful in the future, when trying to diagnose something that has gone wrong.  

With logging, you can register those messages as **DEBUG** or **INFO**. Then set the `logLevel` to be **INFO** during development, and **WARNING** once development is complete. Then, if you ever need them, you can simply change the `logLevel`.  
