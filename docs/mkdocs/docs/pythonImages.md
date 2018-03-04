#Images
---
![ImageDemo](img/imageDemo.png)  

Default image support in appJar assumes no extra libraries, so it only has native support for `.GIF` and `.PPM` images.  
However, extra code is included to allow the use of `.PNG` and `.JPG` files. appJar will convert these to `.GIF` files, before showing them.  
Converting image files is **SLOW**, so it's best to stick to `.GIF` files!  
Also, converting PNGs is temperamental in Python 2.7 - another reason to avoid.  

Getting the path for images right can be **TRICKY**  
It's therefore best to put images in the same folder as your Python code.  
Or, create an image folder and set it using the `.setImageLocation(location)` function.  

#### Built-in icons
appJar has a host of built-in icons you can use.  
They are all located in a folder called: `gui.icon_path`  
If you want to use one, you could just use `.addIcon()` or `.addIconButton()`  
Otherwise, concatenate `gui.icon_path` with the icon's name and `.png`  

###Add Images
---

* `.addImage(title, file, compound=None)`  
    Adding an image is exactly the same as adding any other widget.  
    Simply give the image a title, and pass the filename.  
    appJar will confirm the file is valid, and will also check the file contains the type specified.  
    If an animated `.GIF` is found, then it will be animated within the GUI.  
    `compound` can be set to one of *top*, *bottom*, *left*, *right*, *center* - this will show the image title in that position.  

```python
app.startLabelFrame("Simple", 0, 0)
app.addImage("simple", "balloons.gif")
app.stopLabelFrame()
```

* `.addImageData(title, imgData, fmt="gif", compound=None)`  
    As above, but receives raw image data.  
    Currently only supports base64 encoded GIF images.  
    Alternatively, you can pass in a ready made PhotoImage, simply set `fmt` to be 'PhotoImage'.  
    `compound` can be set to one of *top*, *bottom*, *left*, *right*, *center* - this will show the image title in that position.  

```python
from appJar import gui 
from PIL import Image, ImageTk

app = gui()
photo = ImageTk.PhotoImage(Image.open("images.jpg"))
app.addImageData("pic", photo, fmt="PhotoImage")
app.go()
```

* `.addIcon(title, iconName, compound=None)`  
    This will create an image as above, but use one of appJar's inbuilt icons.  
    Simply pass the name of one of the icons.  
    `compound` can be set to one of *top*, *bottom*, *left*, *right*, *center* - this will show the image title in that position.  

* `.setImageLocation(location)`  
    Set a folder for image files.  
    This will be put before the names of any image files used.  

### Change Images
---
* `.setImage(title, image)` & `.setImageData(title, imgData, fmt="gif")`  
    This will replace the existing image with the new one.  
    If the image has the same path, it will not be changed.  
    ImageData is always reloaded.  

* `.reloadImage(title, image)` & `.reloadImageData(title, imgData, fmt="gif")`  
    This will replace the existing image with the new one.  
    It will force an image reload, even if the file name hasn't changed.  
    Useful if an outside agency modifies the image file.  

```python
def changePic(btn):
    if btn == "Reload":
        app.reloadImage("reload", "balloons.gif")

app.startLabelFrame("Reload", 1, 1)
app.setSticky("ew")
app.addImage("reload", "balloons.gif")
app.addButton("Reload", changePic)
app.stopLabelFrame()
```

* `.setImageSubmitFunction(title, function)`  
    This will set a function to call when the image is clicked.  

```python
clicked = False
def changePic(btn):
    if btn == "clickme":
        global clicked
        if clicked: app.setImage("clickme", "balloons.gif")
        else: app.setImage("clickme", "balloons2.png")
        clicked = not clicked

app.startLabelFrame("Click Me", 0, 2)
app.addImage("clickme", "balloons.gif")
app.setImageSubmitFunction("clickme", changePic)
app.stopLabelFrame()
```

* `.setImageMouseOver(title, image)`  
    Set an image to show, instead of the stored image, while the mouse is over this widget.  

```python
app.startLabelFrame("Mouse Over", 0, 1)
app.addImage("mo_1", "balloons.gif")
app.setImageMouseOver("mo_1", "balloons2.png")
app.stopLabelFrame()
```

* `.setImageSize(title, width, height)`  
    This will set the size of the container for the image, cropping anything that doesn't fit.  

* `.zoomImage(title, mod)`  
    This will attempt to change the size of the image.  
    It's very rudimentary, and usually doesn't look good - but is fun to play around with (try adding a slider under an image...)  
    Negative values will shrink the image, positive will enlarge the image.  

```python
def changePic(btn):
    if btn == "Zoom":
        app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
```


* `.shrinkImage(title, mod)` & `.growImage(title, mod)`  
    These are wrappers for the above function, simply causing the image to shrink or grow accordingly.

### Image Maps
---
It is possible to set up a simple ImageMap - a clickable image, with names linked to different areas.  
When one of those areas is clicked, a function will be called, passing the name of the area as a parameter.  

* `.setImageMap(title, func, coords)`  
    This will associate an image map with the named image.  
    `coords` must contain a dictionary of areas on the map.  
    When a position on the image is clicked, in one of the areas, the named function will be called, passing in the area's name.  
    When an unknown position on the image is clicked, *UNKNOWN* will be passed to the function, along with the coordinates.  

```python
from appJar import gui

# each list of numbers contains the top left x/y and bottom right x/y
coords = {
    "America":[32, 17, 242, 167],
    "South America":[126, 170, 226, 292],
}

def click(area):
    app.setLabel("l1", area)

app=gui()
app.addImage("i1", "map.gif")
app.setImageMap("i1", click, coords)
app.addLabel("l1", "<click the map>")
app.go()
```

###Change Image Animation
---
If an image is animated, it's possible to control it.

* `.setAnimationSpeed(title, speed)`  
    This will change the speed an image is animated at.

* `.stopAnimation(title)` & `.startAnimation(title)`  
    These will start and stop the animation of an image.

```python
def changePic(btn):
    if btn == "Stop":
        global animated
        if animated:
            app.stopAnimation("animated")
            app.setButton("Stop", "Start")
        else:
            app.startAnimation("animated")
            app.setButton("Stop", "Stop")
        animated = not animated

app.startLabelFrame("Animated", 1, 2)
app.setSticky("ew")
app.addImage("animated", "animated_balloons.gif")
app.addButton("Stop", changePic)
app.stopLabelFrame()
```

###Set Background Images
---
It's also possible to add a background image to your GUI.  
If you have lots of grouped widgets, this can look quite **UGLY**, as all of the widgets are drawn on top.  

* `.setBgImage(image)`  
    Set the image for the background.

* `.removeBgImage(image)`  
    Remove the image form the background.

###Image Caching
---
appJar employs an image caching mechanism, to speed up image processing.  
Every time an image is loaded, it's added to the cache.  
The next time an image of the same filename is referenced, it will be loaded from the cache.  
This speeds up processes such as mouse-overs, or setting images back-and-forth.  

Animated images also have their own internal cache, storing each version of the image.  

appJar attempts to preload mouse over images and animated images, to improve smoothness.  

If there's ever a need to clear the image cache (maybe reduce memory footprint), call: `.clearImageCache()`  
