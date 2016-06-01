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

### File Boxes
* `.openBox()`
* `.saveBox()`
* `.directoryBox()`

### Other Boxes
* `.colourBox()`
