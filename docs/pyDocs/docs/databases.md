#Databases in Python
##Database Recap

In order to be able to follow this guide, you will need to understand the basics of a database:

- **Table** - a list of information
- **Field** - each item in the list has named pieces of data in it
- **Record** - a single item in the list
- **Primary Key** - a unique identifier for an item in the list
- **Foreign Key** - a link to the primary key in another table
- **Relationships** - how tables link to each other

An example table could be called pupils, each item in the list represents a pupil, and each pupil has lots of information. A table is defined in a data-dictionary:

 | | 
-|-|-
Field Name | Data Type | Information
PupilID | Integer | Primary Key
First Name | String	 
Last Name | String	 
DOB | Date	 
Gender | String	 

To talk to a database you use **SQL** (*Structured Query Language*). There are two parts to SQL:

 - DDL (Data Definition Language) - used to build and modify tables
    - CREATE TABLE ...
    - ALTER TABLE ...
    - DROP TABLE ...
    - TRUNCATE TABLE ...
 - DML (Data Manipulation Language) - used to get or modify data in tables
    - SELECT ... FROM ... WHERE ...
    - INSERT INTO ... VALUES ...
    - UPDATE ... SET ... WHERE ...
    - DELETE FROM ... WHERE ...

Python comes with a built-in database: [SQLite](https://www.sqlite.org/). To gain access to it, you simply import the library:
```python
import sqlite3
```

Having done that, we simply connect to the database, perform some SQL, and dosconnect:

```python
db = sqlite3.connect('pupils.db')
# perform SQL statements
db.close()
```

As with file access, this can wrapped up using with, to ensure we always disconnect:

```python
with sqlite3.connect("pupils.db") as db:
    # perform SQL statements
```

Both of these will either open an existing database called pupils.db or create a new one with that name. This means that the information will always be saved to a file, so every time you run your program, all the old data will still be there. If you don't want to create a file, and would instead like to temporarily create a database in RAM, replace the database name with the String :memory:.
