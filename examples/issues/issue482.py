import sys
sys.path.append("../../")

from appJar import gui

def fDeleteRow(dRow): app.deleteTableRow("entryTable", dRow)
def fAddRow(): app.addTableRow("entryTable", app.getTableEntries('entryTable'))

with gui() as app:
    app.addTable("entryTable", [["Item", "Description"]], action=fDeleteRow, addRow=fAddRow, actionHeading="Delete", addButton="Add Item", actionButton="X", showMenu=True)
