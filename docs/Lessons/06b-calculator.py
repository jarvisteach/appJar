from appJar import gui

# variables
total = 0.0
lastAction = None
didDecimal = False
started = False
text = ""

# do whatever maths needs doing
def doMath(num, action):
      global total, started, lastAction

      if not started:
            started = True
            total = num
            lastAction = action
            win.setStatus(str(total))
      else:
            win.setStatus(str(total)+action+str(num))
            if action == "+":
                  total += num
            elif action == "-":
                  total -= num
            elif action == "*":
                  total *= num
            elif action == "/":
                  total /= num
      win.clearLabel("lcd")

# stops decimal places showing if there are none
def setLcd(num):
      global text
      if num.is_integer():
           num = int(num)
      text = str(num)

      win.setLabel("lcd", text)

# function to handle button presses
def press(btn):
      global lastAction, total, started, didDecimal, text
      
      # if they press C - reset everything
      if btn == "c":
            lastAction = None
            started = False
            total = 0
            didDecimal = False
            win.clearLabel("lcd")
      # if they press a math key, and we have nums - do math
      elif btn in [ "+", "-", "*", "/" ]:
            if len(text) > 0: doMath(float(text), btn)
      # if they press =, work out answer
      elif btn == "=":
            doMath(float(text), lastAction)
            setLcd(total)
            started = False
            lastAction = "="
      # record decimal point
      elif btn == ".":
            didDecimal = True
      # otherwise
      else:
            if lastAction == "=":
                  text=""
                  lastAction = None
            elif didDecimal :
                  if text == "": text = "0"
                  text = text+"."
                  didDecimal = False
            text = text + btn
            setLcd(float(text))

# the button labels
butLabs = [["7","8", "9","/" ],
            ["4","5", "6", "*"],
            ["1","2", "3", "-"],
            ["0",".", "=", "+"]]

win = gui("Calculator")

win.setResizable(False)
win.setFont(18)
win.setBg("blue")

win.addLabel("lcd")
win.setLabelBg("lcd", "yellow")
win.setLabelAlign("lcd", win.E)
win.addButtons(butLabs, press)
win.setAllButtonWidths(3)
win.addStatus()

win.go()
