import sys
sys.path.append("../../")
from appJar import gui
import time

def uploadFile(filename):
    for i in range(50):
        print(i, filename)
        time.sleep(.2)
    return True

def uploader(btn):
    # call uploadFile(), with the contents of the "file" entry box
    # when uploadFile() completes, its return value will be passed to uploadComplete()
    filename = app.getEntry("file")
    if filename != "":
        app.setLabel("uploadStatus", "Starting upload")
        app.threadCallback(uploadFile, uploadComplete, filename)

def uploadComplete(success):
    if success:
        message = "Upload complete"
    else:
        message = "Upload failed"

    app.queueFunction(app.setLabel, "uploadStatus", message)

app=gui()
app.addLabel("uploadStatus", "No uploads")
app.addFileEntry("file")
app.addButton("UPLOAD", uploader)
app.go()
