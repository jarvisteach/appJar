#import sys
#sys.path.append("../../")

from numpy import sin, pi, arange
import random
from appJar import gui 

with gui() as app:
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    axes = app.addPlot("p1", x, y)
    axes.set_title("Click somewhere on a line.\nRight-click to deselect.\nAnnotations can be dragged.")
    axes.legend(['The curve'])
    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
#    app.refreshPlot("p1")

    import mplcursors
    mplcursors.cursor(axes) # or just mplcursors.cursor()
