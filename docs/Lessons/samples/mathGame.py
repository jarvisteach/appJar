# import the library
import random
import sys
sys.path.append("../../../")
from appJar import gui

actions = ["+", "-", "*", "/" ]
answers = []

difficulty = 1

# function to deal with button press
def press(name):
    win.setStatusbar ( name )
    if name == "EXIT": win.stop()
    #elif name == "SUBMIT": win.setStatus(win.textBox("Name", "Please enter your name:"))
    elif name == "SUBMIT":
            checkAnswers()

def checkAnswers():
      global answers
      score = 0
      for loop in range(10):
            a = win.getEntry ("l"+str(loop) )

            try:
                  a = float(a)
            except ValueError:
                  win.errorBox("Error", "Question " + str(loop + 1) + " is invalid" )
                  win.setFocus("l"+str(loop) )
                  return

            if a == answers[loop]:
                  score += 1
                  win.disableEntry("l"+str(loop) )
                  win.setEntryBg ("l"+str(loop), "green" )
            else:
                  win.setEntryBg ("l"+str(loop), "red" )

      if score < 5:
            win.infoBox("Score", "Low score: " + str(score) + "/10" )
      elif score < 10:
            win.infoBox("Score", "Medium score: " + str(score) + "/10" )
      else:
            win.infoBox("Score", "Perfect score: " + str(score) + "/10" )
            doLabels()


def changeScale ( name ) :
      global difficulty
      difficulty = win.getScale("Difficulty")
      win.setStatusbar(difficulty)
      doLabels()

def stopApp():
      return win.yesNoBox("Quit", "Exit program?")

def doLabels():
      global difficulty, answers
      answers = []
      for loop in range (10):
            numa = random.randint(1*difficulty*2, 10*difficulty*2) 
            numb = random.randint(1*difficulty*2, 10*difficulty*2) 
            action = random.choice(actions)

            if action == "+": answers.append(numa+numb)
            elif action == "-": answers.append(numa-numb)
            elif action == "*": answers.append(numa*numb)
            elif action == "/": answers.append(numa/numb)

            lab = str(numa) + " " + action + " " + str(numb) + " = "
            try:
                        win.addLabel ("l"+str(loop), lab, 2+loop, 0 )
                        win.addEntry ("l"+str(loop), 2+loop, 1 )
            except Exception:
                        win.setLabel ("l"+str(loop), lab )
                        win.enableEntry("l"+str(loop) )
                        win.setEntryBg ("l"+str(loop), "white" )
                        win.setEntry ("l"+str(loop), "" )

# create the GUI
win = gui("Hello")

# configure the GUI
win.setBg("Red")
win.setStopFunction(stopApp)
win.setLabelFont(20)
win.setButtonFont(16)
win.addMenuList("Help", ["a", "b", "c", "d", "-", "g", "e"], press)
win.addStatusbar()

win.addScale("Difficulty", 1, 0,2)
win.setScaleRange("Difficulty", 1,5,difficulty)
win.setScaleChangeFunction("Difficulty", changeScale)
doLabels()
win.addButtons(["SUBMIT", "RESET", "EXIT"], press, 12,0,2)

# go go go
win.go()
