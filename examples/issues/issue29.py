import sys
sys.path.append("../../")
from appJar import gui

def blockingSound():
    app.playSound("buzz.wav", wait=True)
    app.infoBox("Sound", "Finished sound")

def play():
    if app.getCheckBox("wait"):
        app.thread(blockingSound)
    else:
        app.playSound("buzz.wav")
        print("no wait")


def long():
    from time import sleep
    for i in range(100000000):
        sleep(0.5)
        print(i)

def loop():
    app.thread(long)
    
def stop():
    app.stopSound()
    
with gui("Issue 29") as app:
    app.label("Sound Test")
    app.addCheckBox("wait")
    app.button("PLAY", play)
    app.button("STOP", stop)
    app.button("LOOP", loop)
