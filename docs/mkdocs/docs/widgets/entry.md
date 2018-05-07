##Entry
____
Entries are used to capture input from the user. They take a single parameter - a title.

There are five special-case Entries:

* NumericEntry - this only allows numbers to be typed in - always returns a float (None if empty).
* SecretEntry - this will show stars, instead of the letters typed - useful for capturing passwords.
* AutoEntry - this takes a list of words to provide auto-completion.  
* ValidationEntry - can be set to valid/invalid/waiting - will colour the border green/red/black and show a ✔/✖/★  
* FileEntry/DirectoryEntry - provides a button to select a file/directory and auto-populates the Entry  

![Entries](../img/1_entries.png)

```python
from appJar import gui

app=gui()

app.addEntry("e1")
app.addEntry("e2")
app.addEntry("e3")
app.addLabelEntry("Name")
app.addValidationEntry("v1")
app.addFileEntry("f1")

app.setEntryDefault("e2", "Age here")
app.setEntryValid("v1")

app.go()
```

####Add Entries

* `.addEntry(title)`
* `.addNumericEntry(title)`
* `.addSecretEntry(title)`
* `.addAutoEntry(title, words)`  
* `.addValidationEntry(title)`  
* `.addFileEntry(title)`  
* `.addDirectoryEntry(title)`  

    Each of these will add the specified type of Entry, using the title provided.

#### Set Entries
* `.setEntry(title, text, callFunction=True)`  
    This sets the contents of the specified Entry.  
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.setEntryDefault(title, text)`  
    This sets a default value to display in an Entry.  
    Once the user starts typing, it will disappear.  
    The text is centered, shown in a light gray font, and will not be returned by `.getEntry(title)`  

* `.setEntryUpperCase(title)` & `.setEntryLowerCase(title)`   
    This will force all text typed into the Entry to be uppercase/lowercase.  

* `.setEntryMaxLength(title, maxLength)`  
    This will set a maximum length for the specified Entry.  
    Any additional characters typed will be discarded.  

* `.setEntryValid(title)` & `.setEntryInvalid(title)` & `.setEntryWaitingValidation(title)`  
    These will set the relevant status of a validation Entry.  
    (Have a look [here](/specialCharacters) for help displaying special characters)  
    ![EntryValidation](../img/entValidation.png)

* `.setValidationEntry(title, state="valid")`  
    Same as above, set flag to one of `valid`, `invalid` or `wait`.  

* `.setAutoEntryNumRows(title, rows)`  
    This will set the number of rows to display in an AutoEntry.  
    NB. this is limited to the depth of the GUI - if there is no space, then no rows will be displayed. 
    ![AutoEntry](../img/1_autoEntry.png)  

* `.appendAutoEntry(title, value)`  
    This will add the value/list of values to the specified AutoEntry.  

* `.removeAutoEntry(title, value)`  
    This will remove the value from the specified AutoEntry.  

* `.changeAutoEntry(title, value)`  
    This will replace all items in the specified AutoEntry with a new list of values.  

* `.clearEntry(title, callFunction=True)`  
    This will clear the contents of the specified Entry.
    Set ```callFunction``` to be False, if you don't want to call any associated functions.  

* `.clearAllEntries(callFunction=False)`  
    This will clear all Entries in the GUI.  
    Set ```callFunction``` to be True, if you want to call any associated functions.  

* `.setFocus(title)`  
    This will put the cursor in the specified Entry, so that the user can start typing without needing to click.

#### Get Entries
* `.getEntry(title)`  
    This will return the contents of the specified Entry.  
    NB. *numericEntries* always return a float.  

* `.getAllEntries()`  
    This will return the contents of all Entries in the app, as a dictionary.  
    NB. *numericEntries* always return a float.  
