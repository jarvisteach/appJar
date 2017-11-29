# Threads - for things that take a long time...  
---

Looping is great for regularly updating the GUI, but if you want to call a function that might take a long time (such as downloading a file) you need to use a [thread](https://en.wikipedia.org/wiki/Thread_(computing)).  

Running your functions in threads allows the main GUI loop to keep running, so that the GUI won't hang.  

Threads don't always work nicely with GUIs, so your thread shouldn't try to change the GUI, instead you will need to put any GUI updates in a Queue.  

* `.thread(function, *args, *kwargs)`  
    This allows you to run your own functions in a separate thread, so they doesn't cause the GUI to hang.  
    Simply pass the name of your function (with no brackets) and any arguments that it requires.  
    For example: `app.thread(myFunction, param1, param2)`  

* `.queueFunction(function, *args, **kwargs)`  
    You mustn't try to update the GUI directly from your threads.  
    Instead, use this function to queue any updates.  
    Pass the name of the GUI function (with no brackets) and any arguments that it requires.  
    For example: `app.queueFunction(app.updateLabel, "l1", "new label text")`   

``` python
downloadCount = 0

def downloader():
    global downloadCount
    # it's fine to put loops in threads
    for i in range(5):
        # update the GUI through the GUI queue
        app.queueFunction(app.setLabel, "l1", "Starting download " + str(downloadCount))
        # this takes a long time
        downloadFile("file" + str(downloadCount) + ".dat")
        # update the GUI through the GUI queue
        app.queueFunction(app.setLabel, "l1", "Finished download " + str(downloadCount))
        # it's fine to put sleeps in threads
        time.sleep(1)

# put the downloader function in its own thread
app.thread(downloader)
```
* `.threadCallback(func, callback, *atgs, **kwargs)`  
