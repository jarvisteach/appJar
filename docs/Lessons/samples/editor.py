# example of a simple text editor
import sys
sys.path.append("../../../")
from appJar import gui

def open():
      file = win.openBox()
      if file != None:
            contents = file.read()
            win.setTextArea("win", contents)
            file.close()
            win.setTitle("Editor :: " + file.name)
            win.logTextArea("win")

def save():
      file = win.saveBox()
      if file != None:
            text = win.getTextArea("win")
            file.write(text)
            file.close()
            win.setTitle("Editor :: " + file.name)
            win.logTextArea("win")

def new():
      win.clearTextArea("win")
      win.setTitle("Editor :: untitled.txt")
      win.logTextArea("win")

def menus(name):
      if name == "New":
            if not win.textAreaChanged("win"):
                  new()
            else:
                  if win.okBox("Discard Changes", "Creating a new file will lose any current changes."):
                        new()
      elif name == "Open...":
            if not win.textAreaChanged("win"):
                  open()
            else:
                  if win.okBox("Discard Changes", "Opening a new file will lose any current changes."):
                        open()
      elif name == "Save":
            if win.textAreaChanged("win"): save()
            else: win.infoBox("Info", "No changes to save.")
      elif name == "Exit":
            if win.textAreaChanged("win"):
                  if win.okBox("Discard Changes", "Closing the editor will lose and changes."):
                        win.stop()
            else:
                  win.stop()
def tools(name):
      if name == "Background":
            col = win.colourBox()
            if col is not None:
                  win.setTextAreaBg("win",col)
                  win.setBg(col)
      elif name == "Foreground":
            col = win.colourBox()
            if col is not None:
                  win.setTextAreaFg("win",col)
      elif name == "Font +":
            win.increaseLabelFont()
      elif name == "Font -":
            win.decreaseLabelFont()

win = gui("Editor :: untitled.txt")

win.addMenuList("File", ["New", "Open...", "Save", "-", "Exit"], menus)
win.addToolbar(["Background", "Foreground", "Font +", "Font -"], tools)

win.addScrolledTextArea("win")
win.setTextAreaBg("win", "green")
win.setBg("green")
win.setTextAreaFocus("win")

win.go()
