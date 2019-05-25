import sys
sys.path.append("../../")

from appJar import gui 
from mpl_toolkits.mplot3d import Axes3D

with gui() as app:
    fig = app.plot("p1", nav=True)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([1,2],[1,2],[1,2])
