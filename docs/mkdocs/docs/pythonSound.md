#Sound
---

Sound is only supported in Windows, using the Winsound API.  
Therefore, only ```.WAV``` files will work.

###Playing Sound Files
---

* `.playSound(sound, wait=False)`  
    Play the named sound file.  
    By default, the sound is played asynchronously, meaning the function will return immediately, even though the sound hasn't finished playing.  
    It is possible to override this, by setting wait to True. This is not recommended though, as the GUI will become unresponsive.

    If you want to call a function after a sound has finished playing, you will need to use a [thread](/pythonThreads):

```
# this function only returns once the sound finishes 
def blockingSound():
    app.playSound("sound.wav", wait=True)
    app.infoBox("Sound", "Finished sound")

# play the sound in a thread
def playSound():
    app.thread(blockingSound)

with gui("SOUND") as app:
    app.button("PLAY", playSound)
```

    **NB.** This causes a few issues:
    * Threaded sounds queue up and only start when the previous threaded sound finishes.  
    * Trying to play a non-threaded sound, will do nothing.  
    * Trying to stop a threaded sound won't work, but **WILL** cause the GUI to hang, until the sound (and any queued sounds) finishes.  

* `.stopSound()`  
    This will stop whatever sound is currently being played.

* `.loopSound(sound)`  
    This will play the named sound in a loop, in the background.

* `.setSoundLocation(location)`  
    Set a folder for the sound files.  
    This will be put before the names of any sound files used.  

###Playing Built-In Sounds
---

* `.bell()`  
    This will work on all platforms, playing a bell sound.  

* `.soundError()`  
    This will sound a simple error beep.

* `.soundWarning()`  
    This will sound a simple warning beep.

###Playing Musical Notes
---

* `.playNote(note, duration=200)`

    Support is built in for playing musical notes, using winsound.
    The note can be a numeric frequency, or a String note.
    The duration can be a number in milliseconds, or a String duration.

    Over 50 String notes are available, such as:

    * f#1 = 46
    * b7 = 3951
    * g9 = 12543  
    
    The following String durations are supported:

    * BREVE = 2000
    * SEMIBREVE = 1000
    * MINIM = 500
    * CROTCHET = 250
    * QUAVER = 125
    * SEMIQUAVER = 63
    * DEMISEMIQUAVER = 32
    * HEMIDEMISEMIQUAVER = 16

    These can be accessed through the variables `gui.NOTES` and `gui.DURATIONS`
