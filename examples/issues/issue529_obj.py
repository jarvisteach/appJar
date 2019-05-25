import sys
sys.path.append("../../")

from numpy import sin, pi, arange
from appJar import gui 
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as addToolbar
import random

from mpl_toolkits.mplot3d import Axes3D

with gui() as app:
    fig = app.addPlotFig("p1", showNav=True)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([1,2],[1,2],[1,2])
