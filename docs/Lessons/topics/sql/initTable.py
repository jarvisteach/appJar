import sqlite3
connection = sqlite3.connect("faceBook.db")

with connection:
      cursor = connection.cursor()
      cursor.execute("DROP TABLE IF EXISTS friends")
      cursor.execute("CREATE TABLE friends (id INTEGER PRIMARY KEY, name VARCHAR(20), gender CHAR(1), dob DATE)")
      cursor.execute("INSERT INTO friends VALUES (1, 'Steve Jobs', 'M', '07101982')")
      cursor.execute("INSERT INTO friends VALUES (2, 'Bill Gates', 'M', '07101966')")
      cursor.execute("INSERT INTO friends VALUES (3, 'John Barnes', 'M', '07101944')")
      cursor.execute("INSERT INTO friends VALUES (4, 'Ada Lovelace', 'F', '07101911')")
      cursor.execute("INSERT INTO friends VALUES (5, 'Konnie Huq', 'F', '07101912')")
