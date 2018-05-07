import sys
sys.path.append("../../")

from appJar import gui

def starter():
    print('starting')

with gui(start=starter) as app:
    app.label('hello world')
#    app.startFunction = starter
