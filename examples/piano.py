import time
import sys
sys.path.append("../")
from appJar import gui

notes = ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "a6", "b6", "c6"]

recording = False

def status():
    app.setStatusbar("Recording: " + str(recording), 0)

def press(btn):
    dur = app.getOptionBox("Duration:")
    val = btn + "," + dur
    if recording:
        app.addListItem("notes", val)

    app.playNote(btn, dur)

def hover_in(btn):
    app.setLabelBg(btn, "gray")

def hover_out(btn):
    app.setLabelBg(btn, "white")

def buttons(btn):
    global recording
    if btn == "Record":
        recording = True
        app.enableButton("Stop")
        app.disableButton("Record")
        app.disableButton("Play")
        app.disableButton("Clear")
    elif btn == "Stop":
        recording = False
        app.disableButton("Stop")
        app.enableButton("Record")
        app.enableButton("Play")
        app.enableButton("Clear")
    elif btn == "Play":
        app.setStatusbar("Playing: True", 1)
        app.disableButton("Stop")
        app.disableButton("Record")
        app.disableButton("Play")
        app.disableButton("Clear")
        notes = app.getAllListItems("notes")
        for pos, note in enumerate(notes):
            note,dur = note.split(",")[0], note.split(",")[1]
            app.selectListItemPos("notes", pos)
            print(note, dur)
            time.sleep(1)

        app.setStatusbar("Playing: False", 1)
        app.enableButton("Record")
        app.enableButton("Play")
        app.enableButton("Clear")
    elif btn == "Clear":
        app.clearListBox("notes")

###############
# Create GUI
###############
app = gui("Piano")
app.setBg("purple")
app.startLabelFrame("PyPiano")
app.setPadding([5,5])

for pos, note in enumerate(notes):
    app.addEmptyLabel(note, 0, pos)
    app.setLabelFunction(note, press)
    app.setLabelBg(note, "white")
    app.setLabelRelief(note, "ridge")
    app.setLabelWidth(note, 5)
    app.setLabelHeight(note, 5)
    app.setLabelOverFunction(note, [hover_in, hover_out])
    app.setLabelTooltip(note, note)

app.addLabelOptionBox("Duration:", ["Breve", "Semi-breve", "Minim", "Crotchet"], 1, pos-3, 4)

app.stopLabelFrame()

app.startLabelFrame("Notes", 0, 10, 1, 3)
app.setPadding([5,1])
app.addListBox("notes", [])
app.stopLabelFrame()

app.addButtons(["Record", "Stop", "Play", "Clear"], buttons, 2, 0, 10)
app.disableButton("Stop")
app.addStatusbar(fields=3)
app.registerEvent(status)

app.go()
