import sys
sys.path.append("../../")

from appJar import gui
from appJar import gui as GUI 

with GUI('','640x480') as gui:
    gui.addLabel('test', 'test', 0,0)

    with gui.toggleFrame('a', colspan=3, bg='green', stretch='column'):
        gui.addLabel('a', 'a')
    with gui.scrollPane("Test", colspan=3, bg='red', disabled='horizontal', sticky='nsew', stretch='both'):
        # with gui.frame('123', bg='yellow', colspan=3):
        for i in range(20):
                with gui.toggleFrame('{i}', colspan=5):
                    gui.addLabel(str(i), str(i))

    gui.setSticky('ws')
    gui.setStretch('none')
    row = gui.getRow()
    gui.addButton('b111', None, row,0)
    gui.addButton('b222', None, row,1)
    gui.setStretch('column')
    gui.addEmptyLabel('', row,2)
    gui.setLabelBg('', 'green')
