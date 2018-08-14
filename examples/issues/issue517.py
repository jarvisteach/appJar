import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.table("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]],
        inactiveBg='red', inactiveFg='yellow',
        activeBg='blue', activeFg='white'
        )
    print('reset')
    app.setTableInactiveBg('g1', 'black')
    app.setTableActiveBg('g1', 'white')
    app.setTableInactiveFg('g1', 'white')
    app.setTableActiveFg('g1', 'black')
