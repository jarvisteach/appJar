import sys
sys.path.append("../")

from mpl_toolkits.mplot3d import Axes3D
from appJar import gui 

with gui("MatPlotLib") as app:
    fig = app.addPlotFig("p1", width=3, height=3)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([1,5],[5,2],[3,3])
    fig.set_size_inches(10,20,forward=True)
    app.refreshPlot("p1")
