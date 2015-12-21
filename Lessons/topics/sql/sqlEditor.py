import sqlite3
conn = sqlite3.connect('example.db')
done = False

def createTable(conn, name):
      print ( "Making: " + name )
      cols = "CREATE TABLE " + name + " ("
      while True:
            col = input("Col name:").strip()
            typ = input("Col type:").strip()
            if len(col) == 0: break
            else: cols += col + " " + typ + ","
      cols = cols[:-1] + ')'
      executeQuery(conn, cols)

#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''') 

def getTables(conn):
      return executeQuery("SELECT name FROM sqlite_master WHERE type='table'")

def dumpTable(conn, table):
      return executeQuery("SELECT * FROM " + table)

def executeUpdate(conn,sql):
      c = conn.cursor()
      print ( "Updating: " + sql)
      c.execute(sql)
      conn.commit()

def executeQuery(conn,sql):
      c = conn.cursor()
      print ( "Querying: " + sql)
      c.execute(sql)
      return c.fetchall()

while not done:
      print ("DB Browser")
      print ("==========")

      print ("Menu")
      print ("1 -- List tables")
      print ("2 -- Dump Table")
      print ("3 -- Create Table")
      print ("4 -- Execute Query")
      print ("5 -- Execute Update")

      choice = -1
      while not done:
            try: choice = int(input(":"))
            except: pass
            if choice == 0: done = True
            elif choice == 1: print ( getTables(conn)); break
            elif choice == 2: print ( dumpTable(conn, input("Table name?"))); break
            elif choice == 3:
                  tab = input("Table name?")
                  print ( createTable(conn, tab)); break
            elif choice == 4: print ( executeQuery(conn, input("Query?"))); break
            elif choice == 5: print ( executeUpdate(conn, input("Update?"))); break

#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")





conn.close()
