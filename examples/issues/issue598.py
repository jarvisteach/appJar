import sys
sys.path.append("../../")

from appJar import gui

def setter():
    app.entry('options', 'apple')

with gui('tabs', '500x500') as app:
    app.label('hello world')
    with app.tabbedFrame('tabs'):
        with app.tab('aaa'):
            app.label('aaa')
            app.label('aaa2')
            app.addEntry('abc')
            app.button('press', setter)
            app.label('aaa3')
        with app.tab('bbb'):
            app.label('bbb')
        with app.tab('ccc'):
            app.label('ccc')
        with app.tab('ddd'):
            app.label('ddd')
            app.button('press2', setter)
            app.entry('options', value=['aaa', 'apple', 'auto'], kind='auto')
