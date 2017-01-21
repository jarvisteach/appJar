from appJar import gui

def music(btn):
      if btn == "Stop":
            app.stopSound()
      elif btn == "Play":
            song = app.getRadioButton("song")+".wav"
            app.playSound(song)

app=gui()

app.startLabelFrame("Songs")
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "We Will Rock You")
app.addRadioButton("song", "Don't Stop Me Now")
app.addRadioButton("song", "We Are The Champions")
app.stopLabelFrame()

app.addButtons(["Play","Stop"], music)

app.go()
