import sys
sys.path.append("../../")
from appJar import gui

def press(*args):
    if args[0]=="newRow":
        app.addGridRow('airflow_data_raw', app.getGridEntries('airflow_data_raw'))
    else:
        print(args)

app=gui("GridTest", "800x500")

app.addGrid(
    'airflow_data_raw',
    [
        ['Nozzle Diameter', 'Number of Nozzles', 'Differential Pressure', 'Static Pressure', 'Voltage', 'Current', 'Frequency'],
    ],
    row=1,
    column=0,
    colspan=3,
    action=press,
    addRow=True
)

app.go()
