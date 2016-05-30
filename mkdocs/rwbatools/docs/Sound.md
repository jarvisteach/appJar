#Sound
---

The GUI can also make SOUND (on Windows).  
This uses the winsound API, so is very limited - must be a WAV file.

##Sound Files

* `.playSound(sound, wait=False)`

    Play the named sound file.  
    By default, the sound is played asynchronously, meaning the function will return immediately, even though the sound hasn't finished playing.  
    It is possible to override this, by setting wait to True. This is not recommended though, as the GUI will become unresponsive.

* `.stopSound()`

    This will stop whatever sound is currently being played.

* `.loopSound(sound)`

    This will play the named sound in a loop.

##Built-In Sounds

* `.soundError()`

    This will sound a simple error beep.

* `.soundWarning()`

    This will sound a simple warning beep.

##Musical Notes

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
