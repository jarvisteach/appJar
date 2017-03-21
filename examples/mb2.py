import sys
sys.path.append("../")

from appJar import gui

app = gui("MicroBit Emulator")
app.addMicroBit("mb1")
app.setMicroBitImage("mb1", "09090:90909:90009:09090:00900")
app.go()
