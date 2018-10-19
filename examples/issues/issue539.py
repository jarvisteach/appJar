import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.addFileEntry('f')
    app.addOpenEntry('o')
    app.addSaveEntry('s')
    app.addDirectoryEntry('d')

    app.addLabelFileEntry('lf')
    app.addLabelOpenEntry('lo')
    app.addLabelSaveEntry('ls')
    app.addLabelDirectoryEntry('ld')

    app.entry('ef', kind='file', text='aaa', default='bbb')
    app.entry('eo', kind='open', text='aaa', default='bbb')
    app.entry('es', kind='save', text='aaa', default='bbb')
    app.entry('ed', kind='directory', text='aaa', default='bbb')

    app.entry('lef', kind='file', label=True, tip='zzz')
    app.entry('leo', kind='open', label=True, tip='zzz')
    app.entry('les', kind='save', label=True, tip='zzz')
    app.entry('led', kind='directory', label=True, tip='zzz')
