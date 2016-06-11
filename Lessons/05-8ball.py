# import the libraries
from appJar import gui
import random

# a list of possible answers
answers = ["Can't tell you now", "It is certain", "Ask again later", "Yes",
            "Don’t count on it", "My source says No", "Very doubtful", "Maybe" ]

# function to deal with button press
def press ( btn ) :
    if len ( win.getEntry ( "Question" ) ) == 0:
        win.errorBox ( "Error", "You must ask a question" )
    else:
        #try: win.playSound ( "buzz.wav" )
        #except Exception: pass
        win.setLabel ( "Answer", random.choice ( answers ) )
        win.clearEntry("Question")

win = gui("Magic 8 Ball")

win.setFont(18)

win.addEntry("Question")
win.setFocus("Question")
win.addButton( "Shake", press)
win.addImage("8ball", "resources/8ball.gif")
win.addEmptyLabel("Answer")
win.setLabelBg("Answer", "Yellow")

# start the gui
win.go()
