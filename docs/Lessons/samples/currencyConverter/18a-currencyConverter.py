# import the library
import sys
sys.path.append("../../../../")
from appJar import gui

# hash of currencies
currencies={}
fileName = "conversionRates.txt"

def loadFile(fileName):
      global currencies
      with open ( fileName, "r") as inFile :
            for line in inFile:
                  items = line.split(",")
                  currencies[items[0].strip()] = float(items[1].strip())

def stop():
      # save file
      with open ( fileName, "w" ) as outFile :
            for c in list(currencies.keys()):            
                  outFile.write(c + "," + str(currencies[c]) + "\n")
      return True

def convert(frm, to, amt):
      f_rate = currencies[frm]
      t_rate = currencies[to]
      return round ( amt / f_rate * t_rate, 2 )

# function to handle button presses
def press(name):
      try:
            am = float(win.getEntry("amount"))
            fr = win.getOptionBox("from")
            to = win.getOptionBox("to")
            conv = convert(fr, to, am)
            win.setLabel("amount", str(conv) + " " + to)
      except:
            win.errorBox("Error", "Invalid amount, make sure you enter a number.")
      
def updateRate(name):
      global currencies
      currencies[name] = win.numBox("New Rate", "Enter the new exchange rate for: " + name)

# first load the currencies
loadFile(fileName)

# create the GUI and start it
win = gui("Currency")
win.setFont(16)

win.addLabel("title", "Currency Converter", 0, 0, 4)

win.addEntry("amount", 1, 0)
win.setEntryWidth("amount", 5)
win.setFocus("amount")
win.setEntryFunc("amount", press)

win.addOptionBox("from", currencies.keys(),1,1)
win.addLabel("to", "To:",1,2)
win.addOptionBox("to", currencies.keys(),1,3)

win.addButton("Convert", press, 1, 4)
win.addLabel("amount", "0", 2, 2, 2)
win.setStopFunction(stop)

win.addMenuList("Rates", currencies.keys(), updateRate)

win.go()


