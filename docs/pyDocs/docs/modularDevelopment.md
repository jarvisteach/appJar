#Modular Development
A modular program is made up of lots of seperate parts (modules). Each of these should work independently of the others. In Python, we acheive this by writing *functions*.  

Python has lots of [built-in functions](https://docs.python.org/3.4/library/functions.html) that you might have met already: print, input, int, str, len, round, etc... These work by themselves, without needing to be changed. You simply give them some information to work with, and they (sometimes) give you some information back.  
##Writing a Function
So, how do we write a function? Well, it's pretty simple - you give it a name, and then everything that is indented after the name, is in that function:
```pyhton
def myFunction():
    print("This is in the function")
    print("This is also in the function")

print("This is not in the function.")

```
This funciton is called *myFunction*, but it could be called anything (except for the built-in function names or [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)). Whenever you tell your program to do *myFunction* it should print the two messages inside.
