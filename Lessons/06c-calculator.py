from appJar import gui

total = 0.0
lastAction = None
didDecimal = False
started = False

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
      win.clearEntry("lcd")

def press(name):
      global lastAction, total, started, didDecimal
      text = win.getEntry("lcd")
      
      if name == "c":
            lastAction = None
            started = False
            total = 0
            didDecimal = False
            win.clearEntry("lcd")
      elif name in [ "+", "-", "*", "/" ]:
            if len(text) > 0: doMath(float(text), name)
      elif name == "=":
            doMath(float(text), lastAction)
            setLcd(total)
            started = False
            lastAction = "="
      elif name == ".": didDecimal = True
      else:
            if lastAction == "=":
                  text=""
                  lastAction = None
            elif didDecimal :
                  if text == "": text = "0"
                  text = text+"."
                  didDecimal = False
            text = text + name
            setLcd(float(text))

def setLcd(num): # stops decimal places showing if there are none
      if num.is_integer():
           num = int(num)
      win.setEntry("lcd", str(num))

win = gui("Calculator")
win.setFont(18)
win.setBg("brown")
win.addEntry("lcd", 0, 0)
win.addButtons(["7","8", "9","/" ], press, 1)
win.addButtons(["4","5", "6", "*"], press, 2)
win.addButtons(["1","2", "3", "-"], press, 3)
win.addButtons(["0",".", "=", "+"], press, 4)
win.addStatus()
win.go()
