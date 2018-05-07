import sys
sys.path.append("../../")

from appJar import gui

def showPositions():
    for widg in app.getContainer().grid_slaves():
        row, column = widg.grid_info()["row"], widg.grid_info()["column"]
        print(widg, row, column)

with gui("Grid Demo", "300x300", sticky="news", expand="both") as app:
    for x in range(5):
        for y in range(5):
            app.label(str(x)+str(y), row=x, column=y)
        
    app.button("PRESS", showPositions, colspan=5)
