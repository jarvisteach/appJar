from appJar import gui
import random

grid = [""] * 9

def resetButtons():
      print ( grid )
      for loop in range (9):
            win.setButton(str(loop), "" )
            win.enableButton(str(loop))
            grid[loop] = ""

def didWin():
      print ( grid )

      if grid[0] != "" and grid[0] == grid[1] == grid[2]: return True
      elif grid[3] != "" and grid[3] == grid[4] == grid[5]: return True
      elif grid[6] != "" and grid[6] == grid[7] == grid[8]: return True
      elif grid[0] != "" and grid[0] == grid[3] == grid[6]: return True
      elif grid[1] != "" and grid[1] == grid[4] == grid[7]: return True
      elif grid[2] != "" and grid[2] == grid[5] == grid[8]: return True
      elif grid[0] != "" and grid[0] == grid[4] == grid[8]: return True
      elif grid[2] != "" and grid[2] == grid[4] == grid[6]: return True
      else: return False

def getBestMove():
      while True:
            pos = random.randint(0,8)
            if grid[pos] == "": return pos

def makeMove(pos, player):
      win.setButton(str(pos), player)
      win.disableButton(str(pos))
      grid[pos] = player

def playerMove(button):
      val = int(button)
      makeMove(val, "X")

def computerMove():
      val = getBestMove()
      makeMove(val, "O")

# function to deal with button press
def press ( btn ) :
      playerMove(btn)
      if didWin():
            win.infoBox("Winner", "You win!")
            resetButtons()
      else:
            computerMove() 
            if didWin():
                  win.infoBox("Winner", "Computer wins!")
                  resetButtons()


# create the GUI
win = gui("X and O")
win.setBg("red")

win.addButtons(["0", "1", "2"], press)
win.addButtons(["3", "4", "5"], press)
win.addButtons(["6", "7", "8"], press)
win.setAllButtonWidths(3)
resetButtons()

win.go()
