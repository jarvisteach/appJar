import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.entry('data1', label='AAA:')
    app.entry('data2', label='AAA:')
    app.entry('data3', label='AAA:')
    app.addLabelEntry('AAA:')
