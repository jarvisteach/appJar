#Defensive Programming  
Defensive programming is a way of designing your program, so that it will continue to work, even when unexpected things happen.  

Defensive programming should improve:  

- **Quality** by reducing the number of bugs
- **Readability** making your code more readable, and easier to understand
- **Reliability** preventing the program from crashing when it receives unexpected inputs

Defensive programming can sometimes go too far - you shouldn't try to prevent errors that can't happen, as this could slow your program down, and make it harder to maintain.  

It's also important not to be too vague, otherwise you might miss important errors, that need to be found.

##Styles of Defensive Programming
There are two styles of dealing with potential errors:  

- **EAFP** - **E**asier to **A**sk for **F**orgiveness than **P**ermission
- **LBYL** - **L**ook **B**efore **Y**ou **L**eap  

Generally, **EAFP** is preferred in Python.

##Examples of Defensive Programming
A common place programs can crash is when you expect NUMERIC input, but the user types a STRING:

```python
choice = int(input( "Enter your choice: " ))
```

###EAFP
In **EAFP**, you try to do what you wanted to do, then if it breaks, you deal with it.
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

###LBYL
In **LBYL**, you check if you can do something, and only do it if it's OK.

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
