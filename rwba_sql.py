import sqlite3

#####################################
## SQL Wrapper
#####################################
class sql():
      # self.rows - contains the number of rows affected by last query
      # self.table - stores the name of the last table queried/updates
      def __init__(self, db='example.db'):
            ''' connects to the specified database, or example.dg '''
            self.conn = sqlite3.connect(db)

      def getTables(self):
            ''' returns a list of table names '''
            vals = self.executeQuery("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [] 
            for i in vals:
                  tables.append(i[0])
            return tables

      def dropTable(self, table=None):
            if table == None: table = self.table
            else: self.table = table
            return self.executeUpdate("drop table " + table)

      def getNumRows(self,table):
            ''' returns a count of how many rows are in the given table '''
            self.table = table
            return self.executeQuery("SELECT count(*) FROM " + table)[0][0]

      def getPK(self,table):
            self.table = table
            c = self.conn.cursor()
            c.execute("PRAGMA table_info('" + table + "') ")
            print ( "# orderNum, name, type, NOTNULL, default, pk" )
            for row in c.execute("PRAGMA table_info('"+table+"')").fetchall():
                  print(row)

      def executeUpdate(self,sql):
            ''' performs the specified update SQL, returns number of rows affected '''
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()
            return c.rowcount

      def executeQuery(self,sql):
            ''' performs the specified query SQL, returns a row set '''
            c = self.conn.cursor()
            c.execute(sql)
            return c.fetchall()

      def getData(self,table):
            ''' returns a 2D list of rows in the specified table, row[0] contains the name of each column '''
            self.table = table
            rows = []
            c = self.conn.cursor()
            c.execute("select * from " + table)
            self.cols = [i[0] for i in c.description]
            rows.append ( self.cols )
            for row in c.fetchall(): rows.append(row)
            self.rows = len(rows) - 1
            return rows
