import sys
sys.path.append("../../")
from appJar import gui

def press(*args):
    if args[0]=="newRow":
        app.addGridRow('airflow_data_raw', app.getGridEntries('airflow_data_raw'))
    else:
        print(args)

app=gui("GridTest")


app.addGrid(
    'c',
    [
#        ["a"],
        ['Nozzle Diameter', 'Number of Nozzles', 'Differential Pressure', 'Static Pressure', 'Voltage', 'Current', 'Frequency'],
    ],
    addRow=True
)

app.go()
