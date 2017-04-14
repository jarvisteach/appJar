# Python Basics
* * *
Below is a bunch of stuff explaining the basics of Python...  

## Cheat Sheets
Help can be found at:

* [Python Cheat Sheet](/cheatSheets/PythonCheatSheet.pdf)
* [Turtle Cheat Sheet](/cheatSheets/Turtle%20T3%20CheatSheet.pdf)
* [GUI Cheat Sheet](/cheatSheets/GUI%20T3%20CheatSheet.pdf)
* * *
## Data
### Variables
Variables are the most important things in programming.  
They let your program remember information.  
Variables can store someone's name, their age, or even their favourite food.  
Variables simply point to a space in memory, where the data is stored.  

A variable always has three things:

* An **identifier** - a name to refer to the variable by  
* A **value** - the information the variable is storing  
* A **data type** - the type of information being stored (words, numbers, lists, etc.)  

```python
# this declares three variables: name, age, male
# and initialises each one with a starting value
name = "Alan Shearer"
age = 45
male = True
```

Variables generally go through a three stage process:

- **Create** - The variable identifier is declared, and the variable is initialised with a starting value
- **Change** - The variable's value is modified
- **Check** - The variable's value is checked, in decisions & loops

At various points along this route, the variable will be **used**.
### Constants
Sometimes, you need to store data that doesn't change - these are known as **constants**.  
They are *created* in the same way, but can't be *changed*.  
In Python, it is common to write the name of constants in **all uppercase**.
```python
# declare a constant, that we don't want to change
WINNING_SCORE = 100
```
### Data Types
Data types are very important, as they allow the program to have rules: if you add two numbers together, the program should do some maths, but if you add two words together (**concatenation**) the program will just make a new sentence.

There are five main data types:

* **String** - words, letter, sentences. Defined using speech marks.
* **Int** - whole numbers
* **Real** - (floats) numbers with fractions (decimal points)
* **Boolean** - True or False (On or Off)
* **List** - a collection of things (any of the above, or even a collection of lists)

Python tries to work out the data type automatically, but it occasionally needs some help, if you want to tell Python what the data type is, try one of the following:
```python
# create 3 new variables by changing the type of var1/var2/var3
name = str(var1)
age = int(var2)
price = float(var3)
```

### Arithmetic Operators
Python allows you to easily perform maths on your data

 | | 
-|-|-
+ | Addition | a = b + c
- | Subtraction | a = b - c
* | Multiplication | a = b * c
/ | Division | a = b / c
// | Modulus division | a = b // c
% | Remainder division | a = b % c
** | Exponent | a**b
round() | Round | Rounds the number to the nearest place
floor() | Round-down | Rounds the number down  
ceil() | Round-Up | Rounds the number up  
sum() | Sum | Adds together all the items in the list

### String Operations  
Python also lets us perform various actions on Strings.

 | | 
-|-|-
```varName.upper()``` | Uppercase | Makes the entire string uppercase
```varName.lower()``` | Lowercase | Makes the entire string lowercase
```varName.split(" ")``` | Split into a list | Converts the String into a list, using spaces
```varName.split(",")``` | Split into a list | Converts the String into a list, using commas
```varName.count("a")``` | Counts occurrences of the text | Counts how many times **a** appears in the String
```varName.index("a")``` | Finds the first position of the text | Finds the first position of **a**
```varName.startswith("Mr.")``` | Checks what the String starts with | Returns True if the String starts with **Mr.**
```varName.endswith("Jarvis")``` | Checks what the String ends with | Returns True if the String ends with**Jarvis**

### String Splicing    
Remember, Strings are just lists of characters.  
It's also possible to access parts of a String using array square brackets.  

 | | 
-|-|-
```varName[2]``` | Gets a character | Returns the third character
```varName[2:5]``` | Gets a substring | Returns characters from 2 to 4
```varName[2:]``` | Gets a substring | Returns characters from 2 to the end
```varName[:5]``` | Gets a substring | Returns characters from the beginning to 4
```varName[2:10:2]``` | Gets a substring | Returns characters from 2 to 9, skipping every other character
```varName[::-1]``` | Reverse a String | Returns the String in reverse order

* * *
## Selection & Operators
Selection is the ability to make a decision. It allows us to do different things, depending on what information is in a variable.  
This is done using **IF** statements:
```python
# if they are 18 or over, print "You can vote"
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")
```
Making decisions is all about comparing things; is one variable bigger than another, are two other variables the same...

```python
# if they are 18 or over, print "You can vote"
if favArtist == "Picasso":
    print("You like cubist paintings.")
elif favArtist == "Rembrandt":
    print("You like realistic paintings.")
elif favArtist == "Monet":
    print("You like impressionist paintings.")
elif favArtist == "Rembrandt":
    print("You like realistic paintings.")
elif favArtist == "Cezanne":
    print("You like post-impresionistic paintings.")
else:
    print("Unrecognised artist")
```

To compare things we use standard operators, just like in maths.

### Equality Operators
These let us test if things are equal or not:

 | |                                     
-|-|-
== | Equal to     | Check if two items are the same
!= | Not equal to | Check if two items are not the same

### Comparison Operators
These let us compare things:

 | | 
-|-|-
>  | Greater than             | Check if the first item is bigger than the second item
<  | Less than                | Check if the first item is smaller than the second item
>= | Greater than or equal to | Check if the first item is bigger than or the same as the second item
<= | Less than or equal to    | Check if the first item is smaller than or the same as the second item

### Logical Operators
These let us use logic to combine lots of operators:

 |
-|-
and | Both comparisons have to be True
or  | Either or both comparisons have to be True
not | This will change the result from True to False, or vice-versa



* * *
## Iteration
Being able to do selection (make decisions) on its own is nearly enough.  
However, if we want our programs to be really useful, we want them to be able to repeat stuff.

We call this *iteration*.

### While Loops
Let us repeat something until we can make a decision (this may never occur)

#### Infinite While Loops
```python
while True:
    print ( "Looping!" )
```

#### Conditional While Loops
```python
num = -1 # keep looping WHILE they don't guess 21
while num != 21:
    num = int ( input ( "Guess a number: " ) )
    print ( "You guessed:", num )
print ( "You finally got it!!!" )
```

### For Loops
Let us repeat something a set number of times 
#### For Loop Through an Array
```python
# make a list of fruits
fruits = ['banana', 'apple',  'mango']
for item in fruits:
    print ( 'Current fruit :', item)
```
#### For Loop x Times
```python
for index in range ( 10 ):
    print ( "Position:", index )
```
#### For Loop from x to y
```python
for index in range ( 0, 6 ):
    print ( "Position:", index )
```
#### For Loop in Steps
```python
for index in range ( 10, 21, 2 ):
    print ( "Position:", index )
```
### Loop Control
Pyhton provides two really useful commands to help in loop control:

- ```break``` - Ends the loop immediately
- ```continue``` - Goes back to the start of the loop, skipping anything not yet done

```python
while True:
    guess = int(input("Guess a number: "))
    if guess = answer:
        print("You got it!")
        break
    else:
        print("Wrong!")
```
* * *
## Lists
This does exactly what it says on the tin - we can store lots of information all with the same name.
If you have 100 books, you don't want to make 100 variables to remember all the names.  
Instead, you make one variable called *books* and then give each book a number...
```python
# make a list
pupils = ["Edd", "Clive", "Kim", "Kat", "Tim", "Tam"]

# print the first pupil in the list - item 0
print(pupils[0])

# add a pupil to the list
pupils.append("Jordan")

# get the number of pupils in the list
num_of_pupils = len(pupils)

# remove a pupil from the list
list.remove("Edd")
```
We can also iterate through a list, make decisions based on a list, and change items in a list:
```python
# make a list
pupils = ["Edd", "Clive", "Kim", "Kat", "Tim", "Tam"]

# print each pupil in the list
for item in pupils:
   print ( item )

# change an item in the list
pupils [ 2 ] = "Kimberly"

# check if an item is in a list
if "Kat" in pupils:
   print ( "Found her" )
```

We can also slice up or join lists:
```python
# make a list
pupils = ["Edd", "Clive", "Kim", "Kat", "Tim", "Tam"]

pupils[2:4]     # items from 2 until before 4 = Kim & Kat
pupils[2:]      # items from 2 until the end = Kim, Kat, Tim & Tam
pupils[:3]      # items from the beginning until before 3 = Edd, Clive & Kim
pupils[:]       # everything

# you can also count backwards
pupils[-1]      #last item in the array = Tam
pupils[-2:]     # last two items in the array = Tim & Tam
pupils[:-2]     # items from the beginning until 2 before the end = Edd, CLive, Kim & Kat
pupils[1:-1]    # remove first & last = Clive, Kim, Kat & Ti

# join an array into a String of items
sentence = ", ".join(pupils)    # makes the String "Edd, Clive, Kim, Kat, Tim, Tam"
```
* * *
## Modular Development
A modular program is made up of lots of separate parts (modules). Each of these should work independently of the others. In Python, we achieve this by writing *functions*.  

Python has lots of [built-in functions](https://docs.python.org/3.4/library/functions.html) that you might have met already: ``print()``, ``input()``, ``int()``, ``str()``, ``len()``, ``round()``, etc... These work by themselves, without needing to be changed. You simply give them some information to work with, and they (sometimes) give you some information back.  
## Writing a Function
So, how do we write a function? Well, it's pretty simple - you give it a name, and then everything that is indented after the name, is in that function:
```python
def myFunction():
    print("This is in the function")
    print("This is also in the function")

print("This is not in the function.")

```
This function is called *myFunction*, but it could be called anything (except for the built-in function names or [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)). Whenever you tell your program to do *myFunction* it should print the two messages inside.

A more detailed example might be for when you want to keep repeating the same things again and again. It is not a good idea (or any fun) to keep typing the same stuff again and again. Sometimes a loop can solve this, but other times it might not be enough.
```python
# define a function to draw a square
# the size parameter sets the length of the sides
def square ( size ):
   for loop in range ( 4 ) :
        t.forward ( size )
        t.right ( 90 )

# call the function - very important
# setting size to 77
square ( 77 )
```
* * *
## Libraries
Libraries are just other people's code that we want to use. To access them, we simply import them. We have learnt about three libraries so far:

* ```random``` - this lets us generate random numbers
* ```turtle``` - this lets us draw turtle shapes
* ```appJar``` - this lets us create simple GUIs

Here is an example of importing and using a library:
```python
import random

colours = [ "red", "yellow", "green", "blue" ]

# generate a random number between 1 & 100
num = random.randint ( 1, 100 )

# generate a random colour (using the list above)
colour = random.choice ( colours )
```
* * *
## File Access
Accessing files in Python is easy. You simply open the file, read from or write to it, then close it:
```python
outFile = open ( "myfile.txt", "a" )
outFile.write ( "hi there\n" )
outFile.close ( )
```
This can be simplified even further, using the **with** command. The with command will ensure the file is closed once you've finished with it:
```python
with open ( "myfile.txt", "a" ) as outFile :
    outFile.write ( "hi there\n" )
```
When you open a file, you pass the name of the file you want, and an access mode. The following access modes are most commonly used:

* **r** - opens a file for reading.
* **w** - creates a new file for writing (overwrites existing file).
* **a** - opens a file to append to (will create a file if needed).

When reading from a file, it is most common to read it line-by-line. Again, it is more convenient to use **with**:
```python
with open ( "myFile.txt", "r") as inFile :
    # read the file into data
    data = inFile.read ( ) 
    # make a list of lines
    myList = data.splitlines ( ) 
```
This will create a list called _myList_, with one entry for each line.
* * *
## Databases in Python
### Database Recap

In order to be able to follow this guide, you will need to understand the basics of a database:

- **Entity** - an item in the real world, we want to model (pupils in a school)
- **Table** - a container to hold information about an entity, often named after the entity (pupils)
- **Record** - a single item/row in the table (an actual pupil)
- **Field** - the columns in the table, each storing an attribute about the entity (name, age, etc)
- **Primary Key** - something unique to each record in a table (pupil ID)
- **Foreign Key** - when another table links to records in a table, you use their primary key
- **Relationships** - how tables link to each other

###Example
So, to model pupils in the real world - we would create a table, let's call it ```pupils```  
Each ```field``` in ```pupils``` will store a piece of information about a pupil  
Each ```record``` in ```pupils``` will hold all the information about a single pupil  
We can summarise this in a data-dictionary:

 | | | 
-|-|-|-
Field Name | Data Type | Information | Rules
PupilID | Integer | Primary Key
First Name | String	| | **between** 1 and 30 characters 
Last Name | String| | **between** 1 and 30 characters
DOB | Date | | **matches format** DD/MM/YYYY 
Gender | String	| | **one of** Male/Female/Unspecified 

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

Having done that, we simply connect to the database, perform some SQL, and disconnect:

```python
db = sqlite3.connect('pupils.db')
# perform SQL statements
db.close()
```

As with file access, this can be wrapped up using with, to ensure we always disconnect:

```python
with sqlite3.connect("pupils.db") as db:
    # perform SQL statements
```

Both of these will either open an existing database called pupils.db or create a new one with that name. This means that the information will always be saved to a file, so every time you run your program, all the old data will still be there. If you don't want to create a file, and would instead like to temporarily create a database in RAM, replace the database name with the String ```:memory:```
* * *
## Defensive Programming  
Defensive programming is a way of designing your program, so that it will continue to work, even when unexpected things happen.  

Defensive programming should improve:  

- **Quality** by reducing the number of bugs
- **Readability** making your code more readable, and easier to understand
- **Reliability** preventing the program from crashing when it receives unexpected inputs

Defensive programming can sometimes go too far - you shouldn't try to prevent errors that can't happen, as this could slow your program down, and make it harder to maintain.  

It's also important not to be too vague, otherwise you might miss important errors, that need to be found.

### Styles of Defensive Programming
There are two primary styles of dealing with potential errors:  

- **EAFP** - **E**asier to **A**sk for **F**orgiveness than **P**ermission
- **LBYL** - **L**ook **B**efore **Y**ou **L**eap  

Generally, **EAFP** is preferred in Python.

### Examples of Defensive Programming
A common place programs can crash is when you expect NUMERIC input, but the user types a STRING:

```python
choice = int(input( "Enter your choice: " ))
```

#### EAFP
Try to do what you wanted to do, then if it breaks, deal with it:
```python
try:
    choice = int(input( "Enter your choice: " ))
except ValueError:
    print( "Invalid number" )
```
In this example we simply (try to) convert the input into a number - if it fails, we deal with it.

We can then wrap this in a *loop*, to make it keep repeating until the data is valid:

```python
while True:
    try:
        choice = int(input( "Enter your choice: " ))
        break
    except ValueError:
        print( "Invalid number" )
        continue
```

#### LBYL
Check you can do something first, then only do it if it's OK.

```python
choice = input( "Enter your choice: " )
if choice.isdigit():
    choice = int(choice)
else:
    print( "Invalid number" )
```
In this example, we get the input, check it's a number, and then convert it.  

We can then wrap this in a *loop*, to make it keep repeating until the data is valid:

```python
while True:
    choice = input( "Enter your choice: " )
    if choice.isdigit():
        choice = int(choice)
        break
    else:
        print( "Invalid number" )
        continue
```

As can be seen, **EAFP** only catches *ValueErrors*, it will still crash if some other error occurs.  
But that complies with what we said earlier, we don't want to miss strange/important errors.  
And, in **LBYL**, it doesn't actually deal with any errors, but simply tries to prevent them - less reliable?
* * *
## Turtle Basics
To create a turtle, and get it to move, try the following:
```python
# get the library
import turtle
t = turtle.Pen()

# draw a square
for loop in range(4):
    t.forward(100)
    t.right(90)
```
* * *
## GUI Basics
To create a GUI, and show a label, try the following:
```python
# import the library
from appJar import gui

# create the GUI
app = gui("Hello")
app.addLabel("l1", "Hello World!")
app.go()
```
* * *
## Colour Map
Below is a useful colour map to use when doing Turtle or GUI programming.  
![Python Colour Map](https://pythonhosted.org/ete2/_images/svg_colors.png)

* * *
