import sys
sys.path.append("appJar-0.93-py3.6.egg")
from appJar import gui

with gui() as app:
    app.label('hello world')
