* * *
# Cheat Sheets
Help can be found at:

* [Python Cheat Sheet](/cheatSheets/PythonCheatSheet.pdf)
* [Turtle Cheat Sheet](/cheatSheets/Turtle%20T3%20CheatSheet.pdf)
* [GUI Cheat Sheet](/cheatSheets/GUI%20T3%20CheatSheet.pdf)
* * *
# Variables & Data Types
Variables are the most important thing in programming.  
They let your program remember information.  
Variables can store someone's name, their age, or even their favourite food.

A variable needs three things:

* A **name** - the label given to the information
* A **value** - the information the program needs to remember
* A **data type** - this tells the program what type of data it is (words, numbers, lists, etc.)

```python
# this makes three variables called: name, age, male
name = "Alan Shearer"
age = 45
male = True
```
Data types are very important, as they allow the program to have rules: if you add two numbers together, the program should do some maths, but if you add two words together (**concatenation**) the program will just make a new sentence.

There are five main data types:

* **String** - words, letter, sentences. Defined using speech marks.
* **Int** - whole numbers
* **Float** - numbers with fractions (decimal points)
* **Boolean** - True or False (On or Off)
* **List** - a collection of things (any of the above, or even a collection of lists)

Python tries to work out the data type automatically, but it occasionally needs some help, if you want to tell Python what the data type is, try one of the following:
```python
# create 3 new variables by changing the type of var1/var2/var3
name = str(var1)
age = int(var2)
price = float(var3)
```
* * *
# Selection & Operators
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
# Iteration
Being able to do selection (make decisions) on its own is nearly enough.  
However, if we want our programs to be really useful, we want them to be able to repeat stuff.

We call this *iteration*.

## While Loops
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

## For Loops
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
* * *
# Lists
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
# Functions
When you are writing a program, you might want to keep doing the same things again and again. It is not a good idea (or any fun) to keep typing the same stuff again and again. Sometimes a loop can solve thi , but other times it might not be enough.
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
# Libraries
Libraries are just other people's code that we want to use. To access them, we simply import them. We have learnt about three libraries so far:

* Random - this lets us generate random numbers
* Turtle - this lets us draw turtle shapes
* rwbatools - this let us access the GUI stuff

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
# Turtle Basics
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
# GUI Basics
To create a GUI, and show a label, try the following:
```pyhton
# import the library
import sys
sys.path.append ( "W:\COMPUTING\PYLIB" )
from rwbatools import gui

# create the GUI
win = gui ( "Hello" )
win.addLabel ( "l1", "Hello World!" )
win.go ( )
```
* * *
# File Access
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
* **w** - creates a new file for writing (overwrites existng file).
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
# Colour Map
Below is a useful colour map to use when doing Turtle or GUI programming.  
![Python Colour Map](https://pythonhosted.org/ete2/_images/svg_colors.png)

* * *
