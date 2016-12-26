import sys

node = []
left = []
right = []

# simple funciton to display stacks side-by-side
def displayStacks():
      maxLen = len(node)
      if len(left) > maxLen: maxLen = len(left)
      if len(right) > maxLen: maxLen = len(right)

      print("# | N | L | R")
      print("-------------")
      for loop in range(maxLen):
            print("%s | %s | %s | %s" % (loop, node[loop],left[loop],right[loop]))
      print("---------")


def addNode(val):
      global node, left, right
      pos = len(node)
      node.append(val)
      left.append(-1)
      right.append(-1)

      if pos > 0:
            curr = 0
            while True:
                  if val < node[curr]:
                        if left[curr] == -1:
                              left[curr] = pos
                              break
                        else:
                              curr = left[curr]
                  else:
                        if right[curr] == -1:
                              right[curr] = pos
                              break
                        else:
                              curr = right[curr]

def pre():
      print("PRE-ORDER")

def inO():
      print("IN-ORDER")

def post():
      print("POST-ORDER")


while True:
      choice = input("(A)dd, (S)how, p(R)e-order, (I)n-order, (P)ost-Order: ").upper()
      if choice == "A": addNode(int(input("Enter a num:")))
      elif choice == "S": displayStacks()
      elif choice == "R": pre()
      elif choice == "I": inO()
      elif choice == "P": post()
      elif choice == "Q": break
