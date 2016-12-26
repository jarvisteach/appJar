import sys

a = []
b = []
c = []
moves = 0

# funciton to initialise all of the global variables
# takes aparameter, how many discs to put on the start stack (a)
def init(size=3):
      global a,b,c, moves
      a = []
      for item in range(size, 0, -1): a.append(item)
      b = []
      c = []
      moves = 0

# simple funciton to display stacks side-by-side
def displayStacks():
      maxLen = len(a)
      if len(b) > maxLen: maxLen = len(b)
      if len(c) > maxLen: maxLen = len(c)

      print("A | B | C (", moves, ")")
      print("---------")
      for loop in range(maxLen-1, -1, -1):
            try: aVal = a[loop]
            except: aVal = " "
            try: bVal = b[loop]
            except: bVal = " "
            try: cVal = c[loop]
            except: cVal = " "

            print("%s | %s | %s" % (aVal,bVal,cVal))
      print("---------")

# function to pop from source & append to dest
def moveDisc(dest, source):
      global moves
      moves += 1
      dest.append(source.pop())
      displayStacks()

# recursive function to move the tower...
def moveStack(item, source, dest, spare):
      if item == 1: moveDisc(dest, source)
      else:
            moveStack(item-1, source, spare, dest)
            moveDisc(dest, source)
            moveStack(item-1, spare, dest, source)

# check for a command line param (number of discs)
if len(sys.argv) > 1: val = int(sys.argv[1])
else: val = 3

# init the stack
init(val)

# move the stacks
displayStacks()
moveStack(val, a, c, b)
displayStacks()
