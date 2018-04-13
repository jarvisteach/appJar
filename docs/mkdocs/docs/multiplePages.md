# Multiple Pages  
---

A common question is how to have different *pages* of widgets in the same GUI.  
There are lots of ways to acheive this...

## SubWindows  
---

Create multiple [SubWindows](/pythonSubWindows) and hide/show them as required.  

## PagedFrames  
---

Create a [PagedWindow](/pythonWidgetGrouping/#paged-window) and navigate back and forth between each page.  

## TabbedFrames  
---

Create a [TabbedFrame](/pythonWidgetGrouping/#tabbed-frame) and have each set of widgets under a different tab.  

## Overlayed Frames  
---

Create a number of [Frames](/pythonWidgetGrouping/#frame) in the same grid position and `raise()` the required Frame.  

## FrameStacks  
---

Works the same as overlayed frames, but provides extra navigation methods, and automatic placement.  

## Hiding/Showing  
---

You can [manipulate widgets](/pythonWidgetOptions/#widget-manipulation) using `hide()` & `show()` to temporarily hide them.  

## Destroying/Recreating
---

You can also [manipulate widgets](/pythonWidgetOptions/#widget-manipulation) using `remove()` or `removeAllWidgets()` and then creating new widgets.  

## Updating Labels  
---

There's also the option of just changing the contents of existing widgets, using the `set` functions.  
