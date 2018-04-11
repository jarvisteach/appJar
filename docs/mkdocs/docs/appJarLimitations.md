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
* **Transparency** isn't supported on Linux  
* **app Icons** aren't available on Linux  
* **Audio** doesn't work on Linux  

### Mac:  
* **Pasting some special characters** will crash appJar on Mac  
* **Tickable Menus & OptionBoxes** don't work on Mac  
* **Buttons** don't support background colours and changing the height on Mac  
* **app Icons** aren't available on Mac  
* **Audio** doesn't work on Mac  

### Windows:  
* n/a  
