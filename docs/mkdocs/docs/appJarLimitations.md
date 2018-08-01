# Limitations
---

There are some things that we don't do well, or that just don't work.  
These are usually caused by limitations in the underlying tkinter, and may be specific to a particular platform.  

## General Limitations:
 * **Animated GIFs** - appJar has its own way of animating GIFs, if animated GIFs don't have complete frames, the animation will break.    
 * **Image Backgrounds** - setting an image as a background doesn't work well - most widgets don't have their own transparency.  
 * **ttk** - appJar was never intended to work with ttk, but due to popular demand, we've tried to build it in, but there are still issues.  

## Platform Limitations:  

appJar has been designed to work the same on the three major platforms: Windows, Mac & Linux.  
However, not all features are available on all platforms.  

### Linux:  
* **Transparency** isn't supported  
* **app Icons** aren't supported  
* **Audio** doesn't work - relies on WinSound  

### Mac:  
* **app Icons** aren't supported  
* **Audio** doesn't work - relies on WinSound  
* **Buttons** don't support background colours and changing the height  
* **Tickable Menus & OptionBoxes** don't work   
* **Pasting some special characters** can [crash](https://bugs.python.org/issue22566) appJar  
* **Inertial scrolling** can [crash](https://stackoverflow.com/questions/16995969/inertial-scrolling-in-mac-os-x-with-tkinter-and-python) appJar  

### Windows:  
* n/a  
