import sys
sys.path.append("../../")

from appJar import gui

def getEm():
    print(app.getAllEntries())
    print(app.getAllInputs())

def getEmi(btn):
    print(btn)
    print(app.getAllEntries())
    print(app.getAllInputs())

with gui("Labels") as app:
    app.startLabelFrame('lf1', colspan=2, label='')
    app.button("PRESS", getEm, col=0)
    app.button("PRESS2", getEmi, name="PRESS", col=1, row='p')
    app.link("click me", getEm, row='p', col=2)
    app.link("click me2", getEmi, col=3, row='p')
    app.stopLabelFrame()
    app.bindKey("z", getEm)
    app.bindKey("x", getEmi)
    with app.labelFrame("lf2", name='ORIGINALS'):
        app.addLabelEntry('a1', label="DUP")
        app.addLabelNumericEntry('a2', label="DUP")
        app.addLabelSecretEntry('a3', label="DUP")
        app.addSecretLabelEntry('a0', label="DUP")
        app.addLabelAutoEntry('a4', [1,2,3,4], label="DUP")
        app.addLabelFileEntry('a6', label="DUP")
        app.addLabelDirectoryEntry('a7', label="DUP")
        app.addLabelValidationEntry('a8', label="DUP")
        app.addLabelNumericEntry('a9', label="DUP")
        app.addNumericLabelEntry('a10', label="DUP")
        app.addLabelScale('a11', label="DUP")
        app.addLabelOptionBox('a12', [1,2,3,4], label="DUP")
        app.addLabelTickOptionBox('a13', [1,2,3,4], label="DUP")
        app.addLabelSpinBox('a14', [1,2,3,4], label="DUP")
        app.addLabelSpinBoxRange('a15', 5, 10, label="DUP")

    with app.labelFrame("lf3", row='p', column=1, label='NEWS'):
        app.entry('aa1', label="DUP")
        app.entry('aa2', label="DUP", kind='numeric')
        app.entry('aa3', label="DUP", secret=True)
        app.entry('aa0', label="DUP", secret=True)
        app.entry('aa4', [1,2,3,4], label="DUP", kind='auto')
        app.entry('aa6', label="DUP", kind='file')
        app.entry('aa7', label="DUP", kind='directory')
        app.entry('aa8', label="DUP", kind='validation')
        app.entry('aa9', label="DUP", kind='numeric')
        app.entry('aa10', label="DUP", kind='numeric')
        app.scale('aa11', label="DUP")
        app.option('aa12', [1,2,3,4], label="DUP")
        app.option('aa13', [1,2,3,4], kind='ticks', label="DUP")
        app.spin('aa14', [1,2,3,4], label="DUP")
        app.spin('aa15', 5, endValue=10, label="DUP")
