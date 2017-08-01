import sys
sys.path.append("../../")

from appJar import gui
from mcpi.minecraft import Minecraft

# function to send messages to minecraft server
def sendMsg(btn):
    msg = app.getEntry("Chat")
    mc.postToChat(msg)

mc = Minecraft.create() # minecraft connection

app = gui("Minecraft")

app.addLabelEntry("Chat", 0, 0)
app.addButton("Send", sendMsg, 0, 1)

app.go()
