#Pop-ups
----
A number of pop-ups (aka dialogs) are available, to add a different user experience, notify the user of information, or get one off pieces of data.

### Message Boxes
* `.infoBox(title, message)`  
    Shows a simple information message, with an OK button.  
    ![InfoBox](img/dialogs/info.gif)

* `.errorBox(title, message)`  
    Shows a simple error message, with an OK button.  
    ![ErrorBox](img/dialogs/error.gif)

* `.warningBox(title, message)`  
    Shows a simple warning message, with an OK message.  
    ![WarningBox](img/dialogs/warning.gif)

###Question Boxes
* `.yesNoBox(title, message)`  
    Shows a question, with Yes/No buttons. Returns True/False.  
    ![yesNoBox](img/dialogs/yesno.gif)

* `.questionBox(title, message)`  
    Shows a question, with Yes/No buttons. Returns True/False.  
    ![QuestionBox](img/dialogs/question.gif)

* `.okBox(title, message)`  
    Shows a question, with OK/Cancel buttons. Returns True/False.  
    ![OkBox](img/dialogs/ok.gif)

* `.retryBox(title, message)`  
    Shows a question, with Cancel/Retry buttons. Returns True/False.  
    ![RetryBox](img/dialogs/retry.gif)

* `.textBox(title, message)`  
    Shows a question requesting a text response. Returns a String, or None if Cancel pressed.  
    ![TextBox](img/dialogs/text.gif)

* `.numberBox(title, message)`  
    Shows a question requesting a numeric response. Returns a number, or None if Cancel pressed.  
    ![NumberBox](img/dialogs/num.gif)

### Tooltips

* `.set XXX Tooltip(name, value)`  
    Sets a tooltip for the named widget, with the specified value.  
    The specified value will be displayed in a small pop-up, when the mouse is left over the widget.

    ![toltip](img/tooltip.png)

    If called a second time, it will update the value of the tooltip.  
    NB. `XXX` must be the widget type, eg. `Label`  

* `.enable XXX Tooltip(name)` & `.disable XXX Tooltip(name)`  
    These will enable or disable the named tooltip.  
    When disabled, it will not show-up.  

### File Boxes
* `.openBox(title=None, dirName=None, fileTypes=None, asFile=False)`  
    Shows an open file dialog.  

    ![OpenBox](img/dialogs/openBox_1.png)  
    ![OpenBox](img/dialogs/openBox_2.png)  
    Various parameters can be provided (although they don't work on all platforms):  

    * ```title``` this will set a title for the dialog  
    * `dirName` this will set a starting directory, defaults to the current working directory  
    * `fileTypes=[('images', '*.png'), ('images', '*.jpg')]`  
    This will set the allowed file extensions, it should be a list of tuples. They will be grouped by the name.  
    * `asFile` this will determine whether a path or actual Python file object is returned, defaults to filename   

* `.saveBox(title=None, fileName=none, dirName=None, fileExt=".txt", fileTypes=None, asFile=None)`  
    Shows a save file dialog.  

    ![SaveBox](img/dialogs/save.png)  

    Various parameters can be provided (although they don't work on all platforms):  
    * ```title``` this will set a title for the dialog  
    * `fileName` this will set a starting file name to save as  
    * `dirName` this will set a starting directory, defaults to the current working directory  
    `fileExt` this will set a file extension to start with
    * `fileTypes=[('images', '*.png'), ('images', '*.jpg')]`  
    This will set the allowed file extensions, it should be a list of tuples. They will be grouped by the name.  
    * `asFile` this will determine whether a path or actual Python file object is returned, defaults to filename   

* `.directoryBox(title=None, dirName=None)`
    Shows a choose directory dialog.  

    ![DirectoryBox](img/dialogs/directory.png)  

    * ```title``` this will set a title for the dialog  
    * `dirName` this will set a starting directory, defaults to the current working directory  

### Other Boxes
* `.colourBox(colour="#FF0000")`
    Shows a dialog for choosing colours.  

    ![ColourBox](img/dialogs/colour.png)  

    Can be passed a colour to start with, defaults to red.  
