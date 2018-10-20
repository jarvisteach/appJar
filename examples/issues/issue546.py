import sys
sys.path.append("../../")

from appJar import gui

with gui('ttk demo', bg='red') as app:
    with app.labelFrame('lf1', bg='red'):
        app.label('hello world', bg='red')
