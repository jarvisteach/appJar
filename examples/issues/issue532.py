import sys
sys.path.append("../../")

from appJar import gui

def press():
    pos = app.slider('slider')
    app.label('lab', pos)

    app.meter('m1', pos, text='m1')
    app.meter('m2', pos, text='m1')
    app.meter('m3', pos, text='m1')
    app.meter('m4', pos, text='m1')
    app.meter('m5', [pos, pos], text='m1')
    app.meter('m6', [pos, pos], text='m1')

with gui() as app:
    app.sticky = 'nw'
    app.stretch='none'

    app.meter('m1', 80, orientation='vertical', row=0, column=0, rowspan=3, text='m1')
    app.meter('m4', 30, orientation='vertical', kind='split', row=0, column=1, rowspan=3, text='m2')
    app.meter('m6', [50, 80], orientation='vertical', kind='dual', row=0, column=2, rowspan=3, text='m3')

    app.meter('m2', 80, orientation='horizontal', row=0, column=3, text='m4')
    app.meter('m3', 30, orientation='horizontal', kind='split', row=1, column=3, text='m5')
    app.meter('m5', [50, 80], orientation='horizontal', kind='dual', row=2, column=3, text='m6')

    app.sticky = 'ew'
    app.separator(colspan=4)
    app.label('lab', 'xx', colspan=4)
    app.slider('slider', 50, increment=1, change=press, colspan=4)
