import sys
sys.path.append("../../")

from appJar import gui

cwd = '/Users/jarvismail'

def open():
    path = app.directoryBox(title="choose")#, dirName="~/Documents/GitHub/")

def show():
    print(app.getAllEntries())


with gui() as app:
    app.label('hello world')
    app.button("OPEN", open)
    app.entry(cwd, cwd, kind = 'directory', dirName=cwd, label=True)
    app.entry(cwd+'-', cwd, kind = 'directory', label=True)
    app.addLabelFileEntry('/', dirName='/')
    app.addLabelSaveEntry('/users', dirName='/Users')
    app.addLabelDirectoryEntry('/users/jarvismail', dirName='/Users/jarvismail')
    app.addLabelOpenEntry('/users/jarvismail/documents', dirName='/Users/jarvismail/Documents')
    app.button('SHOW', show)
