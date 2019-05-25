import sys
sys.path.append("../../")

from appJar import gui

def rads():
    app.setRadioTick('rb')

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
    app.radio(title='rb', name='a', kind='button')
    app.radio(title='rb', name='b', kind='button')
    app.radio(title='rb', name='c', kind='button')
    app.setRadioTick('rb')
    app.setRadioTick('rb', False)
    app.setRadioSquare('rb', True)
    app.button('press', rads)
