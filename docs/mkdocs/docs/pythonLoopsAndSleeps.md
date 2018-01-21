# Loops & Sleeps  
---

When you call `app.go()` you start a loop in the GUI that is constantly checking for [events](/pythonEvents/) - every time it finds an event, it processes it.  

**But**, if an event takes a long time to process, the GUI loop won't be checking for other events - this is when the GUI hangs (stops processing events).  

That's why your events need to be quick - they shouldn't have **loops** or **sleeps**.  

There are a few ways to get around this problem...  

## Sleeps    
---

If you want to do something at a later date, you can use the `.after()` function to specify when it should happen.  

* `.after(delay_ms, function, *args)`  
This will cause the specified `function` to be executed after the specified number of milliseconds.  
Additional parameters for the function can be specified, by setting `*args`.  
It will return an ID, which can be used to cancel the function, if it hasn't already started.  

* `.afterCancel(afterId)`  
This will cancel the specified function, if it hasn't already started.  

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

## Infinite Loops  
---

If you just want something to keep happening forever - maybe updating a statusbar or showing a clock, you can use appJar's built in loop.  

Any functions registered in this way, are called at set intervals.  

* `.registerEvent(function)`  
This will cause the GUI to keep repeating the named function in the background.  
By default, the function will repeat every second.  

* `.setPollTime(time)`  
If you want your functions to be called more or less frequently, change the frequency here.

``` python
#function to set the status bar
def getLocation():
    x,y,z = mc.player.getPos()
    app.setStatusbar("X: "+ str(round(x,3)), 0)
    app.setStatusbar("Y: "+ str(round(y,3)), 1)
    app.setStatusbar("Z: "+ str(round(z,3)), 2)

# call the getLocation function every second
app.registerEvent(getLocation)
```

## Conditional Loops
---

If you want your loop to only repeat a certain number of times or until a condition is met, you can put a decision at the beginning of the function and still use appJar's built in loop.  

You can use this method to simulate both `while` and `for` loops.  

``` python
# global variable to store the count
counter = 10

def countdown():
    global counter
    if counter > 0:
        app.setLabel("counter", str(counter))
        counter -= 1

app.registerEvent(countdown)
```

## Advanced Loops  
---

If you want more control over your loops, you can simulate your own...  

Using the `.after()` function mentioned above, you can simulate a loop, by having your function call `.after()` again.  

``` python
# global variable to store the count
counter = 10

def acceleratingCountdown():
    global counter
    if counter > 0:
        app.setLabel("counter", str(counter))
        counter -= 1
        app.after(100*counter, myLoop)

app.after(0, acceleratingCountdown)
```

This will simulate a countdown, but each time there is a smaller delay between counts.  

## Long Tasks
---

If you want to call a function that does something that takes a long time - such as working with files or networking, you will need a slightly different approach. Have a look at [thread support](/pythonThreads/) in appJar.  
