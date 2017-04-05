import sys
sys.path.append("../")
from appJar import gui

PLAY  = u"\u25B6" # 23F5
PAUSE = u"\u23F8"
RWD   = u"\u23EA"
FWD   = u"\u23E9"
STOP  = u"\u23F9"

def music(btn):
    print(btn)
    if btn == PLAY:
        # play music
        pass
    elif btn == PAUSE:
        # pause music
        pass

app=gui()
app.setButtonFont(30)
app.addButtons([PLAY, PAUSE, STOP, RWD, FWD], music)
FLOWER = u"\u263C"
app.addButton(FLOWER, music)
app.go()
