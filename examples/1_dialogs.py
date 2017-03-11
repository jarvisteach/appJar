from appJar import gui

def press(btn):
      if btn=="info": print(app.infoBox("INFO", "This is the info box"))
      elif btn=="error": print(app.errorBox("ERROR", "this is the error box"))
      elif btn=="warn": print(app.warningBox("WARNING", "This is the warning box"))
      elif btn=="yes": print(app.yesNoBox("YES NO", "This is the yes/no box"))
      elif btn=="quest": print(app.questionBox("QUESTION", "This is the question box"))
      elif btn=="ok": print(app.okBox("OK", "This is the OK box"))
      elif btn=="retry": print(app.retryBox("RETRY", "This is the retry box"))
      elif btn=="open": print(app.openBox("OPEN"))
      elif btn=="save": print(app.saveBox("SAVE"))
      elif btn=="dir": print(app.directoryBox("DIRECTORY"))
      elif btn=="col": print(app.colourBox())
      elif btn=="text": print(app.textBox("TEXT", "This is the text box"))
      elif btn=="num": print(app.numBox("NUMBER", "This is the number box"))


app=gui("Demo Dialog")
app.addButtons(["info", "error", "warn", "yes", "quest"], press)
app.addButtons(["ok", "retry", "open", "save", "dir"], press)
app.addButtons(["col", "text", "num"], press)
app.go()
