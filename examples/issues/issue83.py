import sys
sys.path.append("../../")
from appJar import gui

def addFileSettings(bn):
    app.openLabelFrame('Test')
    for s in range(int(app.getEntry('sets'))):
        for o in range(int(app.getSpinBox('set_options'))):
            row = app.getRow()
            app.addLabelOptionBox('Set {} Option {}'.format(s + 1, o + 1),
                                  ['--','OC','HS'], row, 0)
            app.addNumericEntry('set_{}_{}'.format(s, o), row, 1)
            app.setEntryDefault('set_{}_{}'.format(s, o), '.006')
            app.setEntryWidth('set_{}_{}'.format(s, o), 9)
        if s < int(app.getEntry('sets')) - 1:
            app.addHorizontalSeparator(colour = None)
    app.stopLabelFrame()

def addFileSettings2(bn):
    app.startLabelFrame('Test2')
    for s in range(int(app.getEntry('sets'))):
        for o in range(int(app.getSpinBox('set_options'))):
            row = app.getRow()
            app.addLabelOptionBox('2Set {} Option {}'.format(s + 1, o + 1),
                                  ['--','OC','HS'], row, 0)
            app.addNumericEntry('2set_{}_{}'.format(s, o), row, 1)
            app.setEntryDefault('2set_{}_{}'.format(s, o), '.006')
            app.setEntryWidth('2set_{}_{}'.format(s, o), 9)
        if s < int(app.getEntry('sets')) - 1:
            app.addHorizontalSeparator(colour = None)
    app.stopLabelFrame()

app=gui()

app.addLabelEntry('sets')
app.startLabelFrame('Test')
row = app.getRow()
app.addLabel('Options', 'Options per Set', row, 0)
app.addSpinBoxRange('set_options', 1, 3, row, 1)
app.setSpinBoxWidth('set_options', 10)
app.stopLabelFrame()

app.addButton('Next', addFileSettings)
app.addButton('Next2', addFileSettings2)
app.go()

