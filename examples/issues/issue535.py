import sys
sys.path.append("../../")

from appJar import gui
from numpy import sin, pi, arange
import random, time

def getXY():
    x = arange(0.0, app.slider('yVal')+1, 0.01)
    y = sin(random.randint(1,app.slider('yVal') +1) * pi * x)
    return x,y 

def generate():
    while True:
        app.queueFunction(app.updatePlot, 'p1', *getXY())
        time.sleep(1)

with gui() as app:
    app.label('MatPlotLib Demo', colspan=2)
    app.slider('yVal', show=True, pos=[1,1], sticky='ns', direction='vertical')
    app.slider('xVal', show=True, pos=[2,0], colspan=2, sticky='ew')
    app.plot("p1", *getXY(), row=1)

    app.thread(generate)

