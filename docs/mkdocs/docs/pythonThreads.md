# Threads  
*For things that take a long time...*  

---  

[Looping](/pythonLoopsAndSleeps) is great for regularly updating the GUI, but if you want to call a function that might take a long time (such as downloading a file) you need to use a [thread](https://en.wikipedia.org/wiki/Thread_(computing)).  

Running your functions in threads allows the main GUI loop to keep running, so that the GUI won't hang.  

**NB.** Threads don't always work nicely with GUIs, so your thread **mustn't** try to change the GUI, instead you will need to put any GUI updates in a Queue ([see below](/pythonThreads/#queueing)).  

## Threading  
---

* `.thread(func, *args, **kwargs)`  
    This allows you to run your own functions in a separate thread, so they doesn't cause the GUI to hang.  
    Pass the name of your function (with no brackets) and any arguments that it requires.  
    For example: `app.thread(myFunction, param1, param2)`  

* `.threadCallback(func, callback, *args, **kwargs)`  
    Runs the specified function in a thread, with the passed in arguments.  
    Once the thread completes, call the callback function, passing in any return value from the original function.  

``` python
def uploadFile(filename):
    # this would upload the file to a server
    pass

def uploader(btn=None):
    filename = app.getEntry("file")
    if filename != "":
        app.setLabel("uploadStatus", "Uploading " + filename)

        # call uploadFile(), with the contents of the "file" entry box
        # when uploadFile() completes, its return value will be passed to uploadComplete()
        app.threadCallback(uploadFile, uploadComplete, filename)

def uploadComplete(success):
    if success:
        message = "Upload complete"
    else:
        message = "Upload failed"

    app.queueFunction(app.setLabel, "uploadStatus", message)

app.addLabel("uploadStatus", "No uploads")
app.addFileEntry("file")
app.addButton("UPLOAD", uploader)
```

## Queueing  
---

You **mustn't** try to update the GUI directly from a thread.  
Instead, you should add all your updates to appJar's *update queue*, and let appJar update the GUI.   

* `.queueFunction(func, *args, **kwargs)`  
    Pass the name of the GUI function (with no brackets) you want to call, along with any arguments it requires.  
    For example: `app.queueFunction(app.setLabel, "l1", "new label text")`   

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
