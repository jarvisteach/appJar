import sys
sys.path.append("../../")

from appJar import gui

def to_checkout():
    print("check")

with gui() as app:
    app.label('hello world')
    with app.frameStack("main", start=0):
       with app.frame():
           # Tabbed page for displaying info for each category
           with app.labelFrame("Item Inventory"):
               app.setSticky("nwe")
               app.addDbTable("stock", "main.db", "stock", 0, 0, 0, action=to_checkout,  actionButton="Checkout",
                              actionHeading="Checkout", border="solid", showMenu=True)
               app.setTableEditFunction("stock", table_edits)
               app.setSticky("s")
               app.addButton("Add Item", add_item, 10, 0)
