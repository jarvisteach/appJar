import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.setLabelAnchor("hello world", "right" )
    app.label('ahello world')
    app.setLabelAnchor("ahello world", "w" )

    app.entry('hello world')
    app.setEntryAnchor("hello world", "right" )
    app.entry('ahello world')
    app.setEntryAnchor("ahello world", "w" )

    app.entry('fhello world')
    app.setEntryAlign("fhello world", "right" )
    app.entry('rgahello world')
    app.setEntryAlign("rgahello world", "w" )

    app.addSelectableLabel('c')
    app.setLabelAlign("c", "right" )
    app.addSelectableLabel('d')
    app.setLabelAlign("d", "w" )

    app.addSelectableLabel('y')
    app.setLabelAnchor("y", "right" )
    app.addSelectableLabel('z')
    app.setLabelAnchor("z", "w" )
