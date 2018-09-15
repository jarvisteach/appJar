import sys
sys.path.append("../../")

from appJar import gui

with gui('demo', '200x200') as app:
    app.label('hello world')
    with app.labelFrame('framer', ipad=20):
        app.ipadx = 10
        app.ipady = 20
        app.pady = 20
        app.addRadioButton('a', 'stuff a')
        app.addRadioButton('a', 'stuff b')
        app.addRadioButton('a', 'stuff c')
        app.addRadioButton('a', 'stuff d')

        app.setRadioTick('a', tick=False)

#    app.setLabelFrameInPadding('framer', [20, 20])
#    app.setLabelFramePadding('framer', [20, 20])
