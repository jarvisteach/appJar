import sys
sys.path.append("../../")

from appJar import gui
from mcpi.minecraft import Minecraft

def sendMsg(btn):
    msg = app.getEntry("Chat")
    mc.postToChat(msg)

#function to move the minecraft character
def move(btn):
    x,y,z = mc.player.getPos()

    if btn == "LEFT" or btn == "<Left>":
        x -= 1
    elif btn == "RIGHT" or btn == "<Right>":
        x += 1
    elif btn == "FORWARD" or btn == "<Up>":
        z -= 1
    elif btn == "BACKWARD" or btn == "<Down>":
        z += 1
    elif btn == "JUMP" or btn == "<Space>":
        y += 1
        z -= 1 

    mc.player.setPos(x, y, z)

mc = Minecraft.create() # minecraft connection

app = gui("Minecraft") # GUI

app.addLabelEntry("Chat", 0)
app.addButton("Send", sendMsg, 0, 1)

# put this in the main GUI block
app.startLabelFrame("Move Me", colspan=2)
app.setSticky("EW")
app.setStretch("both")
app.addButton("FORWARD", move, 0, 1)
app.addButton("LEFT", move, 1, 0)
app.addButton("JUMP", move, 1, 1)
app.addButton("RIGHT", move, 1, 2)
app.addButton("BACKWARD", move, 2, 1)
app.stopLabelFrame()

app.go()
