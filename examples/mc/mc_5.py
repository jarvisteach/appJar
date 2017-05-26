import sys
sys.path.append("../../")

from appJar import gui
from mcpi.minecraft import Minecraft

# put this near the top of your code
BLOCKS = {"Stone":1, "Grass":2, "Dirt":3, "Cobblestone":4,
        "Water":8, "Lava":10, "Gold":14, "Iron":15,
        "Coal":16, "Wood":17, "Leaves":18, "Gold":41,
        "Iron":42, "TNT":46, "Torch":50, "Fire":51,
        "Diamond":57, "Snow":78,}
BLOCK_NAMES = list(BLOCKS.keys())
print(BLOCK_NAMES)

# function to drop a block just in front
def drop(btn):
    playerBlock = app.getOptionBox("Block")
    blockId = BLOCKS[playerBlock]
    x,y,z = mc.player.getPos()
    mc.setBlock(x, y+1, z-1, blockId)

#function to set the status bar
def getLocation():
    x,y,z = mc.player.getPos()
    block = mc.getBlock(x, y, z)
    app.setStatusbar(block)
    app.setStatusbar("X: "+ str(round(x,3)), 0)
    app.setStatusbar("Y: "+ str(round(y,3)), 1)
    app.setStatusbar("Z: "+ str(round(z,3)), 2)

# function to send messages to minecraft server
def sendMsg(btn):
    msg = app.getEntry("Chat")
    if len(msg) > 0:
        mc.postToChat(msg)
    else:
        app.errorBox("Invalid Message", "You must type a chat message before sending it.")

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

def menuPress(menu):
    if menu == "Create":
        mc.saveCheckpoint()
    elif menu == "Restore":
        mc.restoreCheckpoint()
    elif menu == "Normal":
        mc.camera.setNormal()
    elif menu == "Fixed":
        mc.camera.setFixed()
    elif menu == "Follow":
        mc.camera.setFollow()

# main GUI block
app = gui("Minecraft") # GUI

app.addLabelEntry("Chat", 0)
app.addButton("Send", sendMsg, 0, 1)

app.startLabelFrame("Move Me", colspan=2)
app.setSticky("EW")
app.setStretch("both")
app.addButton("FORWARD", move, 0, 1)
app.addButton("LEFT", move, 1, 0)
app.addButton("JUMP", move, 1, 1)
app.addButton("RIGHT", move, 1, 2)
app.addButton("BACKWARD", move, 2, 1)
app.stopLabelFrame()

app.addStatusbar(fields=3)
app.registerEvent(getLocation)

app.addLabelOptionBox("Block", BLOCK_NAMES, 2, 0)
app.addButton("Drop", drop, 2, 1 )

app.addMenuList("Checkpoint", ["Create", "Restore"], menuPress)
app.addMenuList("Camera", ["Normal", "Fixed", "Follow"], menuPress)

app.go()
