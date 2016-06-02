#Images
____
Default image support in RWBAtools assumes no extra libraries. That means it should only support `.GIF` and `.PPM` images.  
However, code is included to allow the use of `.PNG` and `.JPG` files. RWBAtools will convert these to `.GIF` files, before loading.  
Converting image files is **SLOW**, so it's best to stick to `.GIF` files!

Getting the path for images right can be **TRICKY**  
It's therefore best to put images in the same folder as your Python code.

###Add Images

* `.addImage(title, file)`  
    Adding an image is exactly the same as adding any other widget.  
    Simply give the image a title, and pass the filename.

    RWBAtools will confirm the file is valid, and will also check the file contains the type specified.

    If an animated `.GIF` is found, then it will be animated within the GUI.

###Change Images

* `.setImage(title, image)`  
    This will replace the existing image with the new one.

* `.setImageMouseOver(title, image)`  
    Set an image to show, instead of the stored image, while the mouse is over this widget.  

* `.setImageSize(title, width, height)`  
    This will set the size of the container for the image, cropping anything that doesn't fit.

* `.zoomImage(title, mod)`  
    This will attempt to change the size of the image.  
    It's very rudimentary, and usually doesn't look good - but is fun to play around with (try adding a slider under an image...)  
    Negative values will shrink the image, positive will enlarge the image.  

* `.shrinkImage(title, mod)` & `.growImage(title, mod)`  
    These are wrappers for the above function, simply causing the image to shrink or grow accordingly.

###Change Image Animation
If an image is animated, it's possible to control it.

* `.setAnimationSpeed(title, speed)`  
    This will change the speed an image is animated at.

* `.stopAnimation(title)` & `.startAnimation(title)`  
    These will start and stop the animation of an image.

###Set Background Images
It's also possible to add a background image to your GUI.  
If you have lots of grouped widgets, this can look quite **UGLY**, as all of the widgets are drawn on top.  

* `.setBgImage(image)`  
    Set the image for the background.

* `.removeBgImage(image)`  
    Remove the image form the background.
