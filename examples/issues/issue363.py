import sys
sys.path.append("../../")
from appJar import gui

rescan = '\u2753 Scan again'
connect = '\u260D Connect'
frame = 'Manual Connection'
address = 'Address'
tcp = 'TCP'
timeout = 'Timeout'
info = '\u2139 Just an (IP) address is required, leave the rest blank to use the defaults.'

def manual():
    app.removeAllWidgets()
    with app.labelFrame('{}'.format(frame), 0, 0, 2):
        # Entry.
        app.entry('addr', pos=(0, 1), sticky='nesw')
        app.entry('tcp', kind='numeric', pos=(1, 1))
        app.entry('timeout', kind='numeric', pos=(3, 1))
        app.setFocus('addr')
        app.setEntryMaxLength('tcp', 5)
        app.setEntryMaxLength('timeout', 3)
        app.setEntryDefault('addr', '{}'.format(address))
        app.setEntryDefault('tcp', '{}'.format(tcp))
        app.setEntryDefault('timeout', '{}'.format(timeout))
    app.button("PRESS", manual)

with gui() as app:
    app.button("PRESS", manual)
