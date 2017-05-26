import sys
sys.path.append("../")

from appJar import gui
from mcpi.minecraft import Minecraft

# put this near the top of your code
BLOCKS={ "AIR":0, "STONE":1, "GRASS":2, "DIRT":3, "COBBLESTONE":4,
    "WOOD_PLANKS":5, "SAPLING":6, "BEDROCK":7, "WATER_FLOWING":8, "WATER":8,
    "WATER_STATIONARY":9, "LAVA_FLOWING":10, "LAVA":10, "LAVA_STATIONARY":11,
    "SAND":12, "GRAVEL":13, "GOLD_ORE":14, "IRON_ORE":15, "COAL_ORE":16,
    "WOOD":17, "LEAVES":18, "GLASS":20, "LAPIS_LAZULI_ORE":21,
    "LAPIS_LAZULI_BLOCK":22, "SANDSTONE":24, "BED":26, "COBWEB":30,
    "GRASS_TALL":31, "WOOL":35, "FLOWER_YELLOW":37, "FLOWER_CYAN":38,
    "MUSHROOM_BROWN":39, "MUSHROOM_RED":40, "GOLD_BLOCK":41, "IRON_BLOCK":42,
    "STONE_SLAB_DOUBLE":43, "STONE_SLAB":44, "BRICK_BLOCK":45, "TNT":46,
    "BOOKSHELF":47, "MOSS_STONE":48, "OBSIDIAN":49, "TORCH":50, "FIRE":51,
    "STAIRS_WOOD":53, "CHEST":54, "DIAMOND_ORE":56, "DIAMOND_BLOCK":57,
    "CRAFTING_TABLE":58, "FARMLAND":60, "FURNACE_INACTIVE":61,
    "FURNACE_ACTIVE":62, "DOOR_WOOD":64, "LADDER":65, "STAIRS_COBBLESTONE":67,
    "DOOR_IRON":71, "REDSTONE_ORE":73, "SNOW":78, "ICE":79, "SNOW_BLOCK":80,
    "CACTUS":81, "CLAY":82, "SUGAR_CANE":83, "FENCE":85, "GLOWSTONE_BLOCK":89,
    "BEDROCK_INVISIBLE":95, "STONE_BRICK":98, "GLASS_PANE":102, "MELON":103,
    "FENCE_GATE":107, "GLOWING_OBSIDIAN":246, "NETHER_REACTOR_CORE":247 
}
blockNames=list(BLOCKS.keys())
blockNames.sort()

def fileMenu(menu):
    if menu == "Checkpoint":
        mc.saveCheckpoint()
    elif menu == "Restore":
        mc.restoreCheckpoint()
    elif menu == "Normal":
        mc.camera.setNormal()
    elif menu == "Fixed":
        mc.camera.setFixed()
    elif menu == "Follow":
        mc.camera.setFollow()

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
    app.setStatusbar("X: "+ str(round(x,3)), 1)
    app.setStatusbar("Y: "+ str(round(y,3)), 2)
    app.setStatusbar("Z: "+ str(round(z,3)), 3)

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

# main GUI block
app = gui("Minecraft") # GUI
app.setLocation(300,650)

app.addLabelEntry("Chat", 0)
# put this in the main GUI block
app.setEntryFocus("Chat")
app.setEntrySubmitFunction("Chat", sendMsg)

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

# add this to the main GUI block
app.bindKey("<Left>", move)
app.bindKey("<Right>", move)
app.bindKey("<Up>", move)
app.bindKey("<Down>", move)
#app.bindKey("<Space>", move)

# put this in the main GUI block
app.addStatusbar(fields=4)
# call the update function every second
app.registerEvent(getLocation)

# put this in the main GUI block
app.addLabelOptionBox("Block", blockNames, 2, 0)
app.addButton("Drop", drop, 2, 1 )

# add a simple menu
app.addMenuList("File", ["Checkpoint", "Restore"], fileMenu)
app.addMenuList("Camera", ["Normal", "Fixed", "Follow"], fileMenu)

app.go()
