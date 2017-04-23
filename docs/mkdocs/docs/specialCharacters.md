#Special Characters
---

If you've ever tried a [ValidationEntry](pythonWidgets/#entry), you'll notice we use some special characters:

![ValidationEntry](img/entValidation.png)

###Explanation
---
You can't find these on the keyboard, so can't type them in your code.  
Instead, you need to use a special code ([unicode](https://en.wikipedia.org/wiki/Unicode)), for the character you want.

For example, Unicode for the tick is ```2714```, and the cross is ```2716```

To represent these in Python, you need to use a special syntax:

```python
TICK=u"\u2714"
CROSS=u"\u2716"

app.addLabel("tick", TICK)
app.addLabel("cross", CROSS)
```

By putting a ```u``` in front of the string, you tell Python it is a Unicode character.  
(In fact, it calls the Unicode function, converting the string data into Unicode.)  

###Example
---
As demonstrated above, it's best to define any Unicode characters you want to use as constants, then you can use them in your code just like any other string.  

![MusicPlayer](img/1_unicode.png)

```python
PLAY  = u"\u25B6"  # 23F5 should work...
PAUSE = u"\u23F8"
RWD   = u"\u23EA"
FWD   = u"\u23E9"
STOP  = u"\u23F9"

def music(btn):
    if btn == PLAY:
        # play music
    elif btn == PAUSE:
        # pause music

app.setButtonFont(20)
app.addButtons([PLAY, PAUSE, STOP, RWD, FWD], music)
```

###Unicode Search
---

So, now you just need to find the right Unicode...  

Our favourite site is [FileFormat.info](http://www.fileformat.info/info/unicode/char/search.htm):  
![UnicodeSearch](img/2_unicode.png)

Simply type what you are looking for into the search box, and it will give you the best matches:  
![UnicodeResults](img/3_unicode.png)

Identify the one you want, and take a note of the Unicode: 263C  
(Note, these are hexadecimal codes, so the values will be between 0 and F)  

You can then use this code in your gui: ![UnicodeSun](img/4_unicode.png)  
```python
FLOWER = u"\u263C"
app.addButton(FLOWER, flowerPower)
```

###Important
---
Different platforms will (potentially) display these characters in different ways...  
As you can see in the music example, for some reason, the PLAY character doesn't display like the other characters...  

There is also an issue with Python GUIs in general, where they can't actually (yet) display all of the different Unicode characters.  
If the character has more than 4 digits in its code, it probably won't work.  
You may even get an error similar to: `character is above the range (U+0000-U+FFFF) allowed by Tcl`  
So, make sure you test them!  

###Easter Egg
---
Try holding the &lt;ALT&gt; key and typing different codes on a Windows computer...  
