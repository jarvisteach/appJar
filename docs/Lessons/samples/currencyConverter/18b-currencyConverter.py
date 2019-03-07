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

def updateImages(btn=None):
      win.setImage("source", "images/"+win.getOptionBox("source")+".png")
      win.setImage("target", "images/"+win.getOptionBox("target")+".png")

def convert(frm, to, amt):
      f_rate = currencies[frm]
      t_rate = currencies[to]
      return round ( amt / f_rate * t_rate, 2 ) 

def press (button):
      try:
            am = float(win.getEntry("Amount"))
            fr = win.getOptionBox("source")
            to = win.getOptionBox("target")
            conv = convert(fr, to, am) 
            win.setLabel("result", str(conv) + " " + to) 
      except:
            win.errorBox("Error", "Invalid amount, make sure you enter a number.")

def updateRate(name):
      global currencies
      currencies[name] = win.numBox("New Rate", "Enter the new exchange rate for: " + name)

def newCurrency(name):
      global currencies
      newC = win.textBox("New Currency", "Enter a new currency")
      if newC is not None: currencies[newC] = 0
      
# create the GUI
loadFile(fileName)
win = gui ( "Currency Converter" )
win.setStopFunction(stop)
win.addMenuList("Rates", currencies.keys(), updateRate)
win.addLabel ( "l1", "Currency Converter",0, 0, 5 )

win.addLabel ( "l2", "Amount", 1, 0)
win.addLabel ( "l3", "From:", 1, 1)
win.addLabel ( "l4", "To:", 1, 2)
win.addLabel ( "l5", "Result:", 1, 3)

win.addEntry ( "Amount", 2, 0)
win.setEntryWidth("Amount", 5)
win.addOptionBox ( "source", currencies.keys(), 2, 1)
win.addOptionBox ( "target", currencies.keys(), 2, 2)
win.addLabel ( "result", 0.0 , 2, 3)
win.addButton ( "Convert", press, 2, 4 )

win.addImage ( "source", None, 3, 1)
win.addImage ( "target", None, 3, 2)
win.addButton("New", newCurrency, 3, 4)

win.setBg("MidnightBlue")
win.setFont("White")
win.setLabelFont(16)

win.setEntrySubmitFunction("Amount", press)
win.setFocus("Amount")
win.setOptionBoxChangeFunction("source", updateImages)
win.setOptionBoxChangeFunction("target", updateImages)

updateImages()

win.go ( )
