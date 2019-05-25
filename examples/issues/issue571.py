import sys
sys.path.append("../../")

from appJar import gui

with gui('Test') as app:
    app.setSize(250, 200)
    with app.labelFrame('Status'):
        app.addLabel('status', 'Unknown')
        app.setLabelBg('status', 'grey')
        app.setLabelSticky('status', 'nsew')
