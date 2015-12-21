from rwbatools import gui
from rwbatools import sql

dbConn = sql()
addRow = False # toggles edit row

def refreshGrid():
      table = str(win.getOptionBox("tables"))
      win.changeOptionBox("tables", dbConn.getTables(), table)
      if len(table) > 0:
            win.updateGrid('g1', dbConn.getData(table), addRow)
            win.setTitle("Table: " + table)
            win.setLabel("rows", "Row Count: " + str(dbConn.rows))

def but(data):
      global addRow
      if data in ("tables", "Refresh"):
            refreshGrid()
      elif data == "newRow":
            vals = win.getGridEntries("g1")
            sql = "insert into " + dbConn.table + " values ("
            for i in vals:
                  sql += "'" + i + "', "
            sql = sql[0:-2]
            sql += ")"
            rem = dbConn.executeUpdate(sql)
            if rem > 0: refreshGrid()
            win.infoBox(str(rem) + " Rows Inserted", str(rem) + " rows have been inserted.")
      elif data == "Edit":
            addRow = not addRow
            refreshGrid()
      elif data == "Drop":
            if win.questionBox("Confirm Drop Table", "Press YES to confirm you want to drop the table " + dbConn.table +
                              ". All data will be lost from this table."):
                  dbConn.dropTable()
                  win.changeOptionBox("tables", dbConn.getTables())
                  refreshGrid()
      else:
            sql = "delete from " + dbConn.table + " where "
            for i in range(len(dbConn.cols)):
                  sql += str(dbConn.cols[i]) + "='" + str(data[i]) + "' AND "
            # remove final AND
            sql = sql[0:-4]
            print(sql)
            rem = dbConn.executeUpdate(sql)
            if rem > 0: refreshGrid()
            win.infoBox(str(rem) + " Rows Deleted", str(rem) + " rows have been deleted.")

# create the window
win = gui("Grid!")
win.setFont(12)
win.setBg("gray")
win.setGeom("800x350")

win.addLabel("l1", "SQL Browser")
win.addOptionBox("tables", dbConn.getTables(), row=0, column=1)
win.setOptionBoxCommand("tables", but)
win.addButtons(["Refresh", "Drop"], but, row=0, column=2)

win.addGrid("g1", (),1, 0, 3, action=but, addRow=addRow)
win.setGridGeom("g1", 300, 300)

win.addLabel("rows", "Row Count: 0", colspan=2)
win.addButton("Edit", but, row=2, column=2)

refreshGrid()
win.go()
