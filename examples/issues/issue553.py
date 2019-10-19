import sys
sys.path.append("../../")

from appJar import gui

def to_checkout(param):
    print("check")

with gui() as app:
    app.label('hello world')
    with app.frameStack("main", start=0):
       with app.frame():
           # Tabbed page for displaying info for each category
           with app.labelFrame("Item Inventory"):
               app.setSticky("nwe")
               app.addDbTable("things", "issue553.db", "things", 0, 0, 0, action=to_checkout,  actionButton="Checkout",
                              actionHeading="Checkout", border="solid", showMenu=True)
               app.setTableEditFunction("things", to_checkout)

           with app.labelFrame("Item Inventory 2"):
               app.setSticky("nwe")
               app.addTable("things2", [['a', 'b', 'c'], ['aaa', 'bbb', 'vccc'], 'fff', 'fff', 'fff'], 0, 0, 0, action=to_checkout,
                               actionButton="Checkout", actionHeading="Checkout", border="solid", showMenu=True)
               app.setTableEditFunction("things2", to_checkout)

           app.setSticky("s")
           app.addButton("Add Item", to_checkout, 10, 0)
