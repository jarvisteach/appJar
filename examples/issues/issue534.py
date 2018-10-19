import sys
sys.path.append("../../")

from appJar import gui

def rads():
    app.setRadioTick('rb')

with gui() as app:
    app.label('hello world')
    app.radio(title='rb', name='a', kind='button')
    app.radio(title='rb', name='b', kind='button')
    app.radio(title='rb', name='c', kind='button')
    app.setRadioTick('rb')
    app.setRadioTick('rb', False)
    app.setRadioSquare('rb', True)
    app.button('press', rads)
