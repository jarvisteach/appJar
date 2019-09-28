import sys
sys.path.append("../../")

from appJar import gui

cwd = '/Users'

def open():
    path = app.directoryBox(title="choose")#, dirName="~/Documents/GitHub/")

def show():
    print(app.getAllEntries())


with gui() as app:
    app.label('hello world')
    app.button("OPEN", open)
    app.entry('--cwd', cwd, kind = 'directory', dirName=cwd)
    app.addFileEntry('fe1', dirName='/')
    app.addSaveEntry('se1', dirName='/Users')
    app.addDirectoryEntry('de1', dirName='/Users/jarvismail')
    app.addOpenEntry('oe1', dirName='/Users/jarvismail/Documents')
    app.button('SHOW', show)
