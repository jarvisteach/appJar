import sys
sys.path.append("../../../../")
from appJar import gui
import random

animals = ['anteater.gif', 'ardvark.gif', 'armadillo.gif', 'llama.gif', 'tapir.gif']

def press (btn):
    animal = random.choice(animals)
    
    if btn == "animal1":        
        win.setImage("animal1",animal)
    elif btn == "animal2":
        win.setImage("animal2",animal)
    elif btn == "EXIT":
        win.stop()

win = gui ( "SNAP" )

win.setGeom("500x400")
win.setBg("black")

win.addLabel ("lb1", "Let's play snap!",0,0,2)
win.setLabelBg("lb1", "red")

win.addImage("animal1", "ardvark.gif",1,0)
win.addImage("animal2", "anteater.gif",1,1)

win.addButtons(["animal1","animal2","EXIT"],press,2,0,2)

win.go( )
