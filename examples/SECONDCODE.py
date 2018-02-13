#psychology revision app
import sys
sys.path.append("../")
from appJar import gui
app = gui()


# handle button events
def LoginScreenPress(button):
    #if user clicks 'cancel', app stops
        usr = app.getEntry("Username") 
        pwd = app.getEntry("Password")
        
        print("User:", usr, "Pass:", pwd)

        if button == "Cancel":
            app.stop()
        elif usr == "user1" and pwd == "pass1":
            app.infoBox("Success" , "Valid login")
            app.hideSubWindow("Login")
            app.show()

            #Revision = app.getEntry("Revision")
def press2(button):
        
        if button == "Revision":
                app.hide()
                app.showSubWindow("Revision")
                #Menu()
        elif button == "1. Attachment":
                app.hideSubWindow("Revision")
                app.showSubWindow("Attachment")
                Attachment()
        elif button == "2. Social influence":
                app.hideSubWindow("Revision")
                app.showSubWindow("Social influence")
                Attachment()
        elif button == "schaffer":
                app.hideSubWindow("Attachment")
                app.showSubWindow("schaffer")
                schaffer()
        elif button == "stages of Attachment":
                app.hideSubWindow("Attachment")
                app.showSubWindow("stages_of_Attachment")
                stages_of_Attachment()
        elif button == "number1":
                app.hideSubWindow("Social influence")
                app.showSubWindow("number1")
                number1()
        elif button == "number2":
                app.hideSubWindow("Social influence")
                app.showSubWindow("number2")
                number2()
        elif button == "Exit": # if user selects the exit button it calls the stop function, only for main menu window
                stopApp()

def press3(button):
        if button == "Questions":
                app.hide()
                app.showSubWindow("Questions")    
                 
def exitChoice(button):
        if button == "Exit": # if user selects the exit button it calls the stop function
                app.stop()
        elif button == "3. Exit": # Revision window
                app.stop()
        elif button == "3.  Exit": # attachment window
                app.stop()
        elif button == "3.   Exit": # social influence window
                app.stop()
        elif button == "3.    Exit": # social influence window
                app.stop()
#def back(button):
#        if button == "back":
                
def QuizQuestions():

        app.addRadioButton("song", "Killer Queen")
        app.addRadioButton("song", "Paradise City")
        app.addRadioButton("song", "Parklife")




        questionsFile = open("questions.txt", "r") # opens file
        questions = [] # array containing questions and answers that will be returned

        while True:
                line = questionsFile.readline().strip()
                if line == "EOF": # final line in file is "EOF"
                        break
        
        if len(line) > 0 and line[0] == "#": # questions always start line with "#"
            question = line[5:].strip()      # removes extraneous characters
            line2 = questionsFile.readline().strip() # some questions are over 2 lines in txt
            if not line2[0] == "-":
                question = question + " " + line2
                questionsFile.readline() # skips empty line in file             
            answers = []                    # stores answers for current question
            answers.append(questionsFile.readline()[2:].strip()) #answer 1
            answers.append(questionsFile.readline()[2:].strip()) #answer 2
            answers.append(questionsFile.readline()[2:].strip()) #answer 3
            answers.append(questionsFile.readline()[2:].strip()) #answer 4
            questionsFile.readline() # skips empty line in file
            correctAnswer = questionsFile.readline()[7:].strip() #current correct answer
            questionAndAnswers = [] # array storing questions and answers to be appended to questions[]
            questionAndAnswers.append(question)
            questionAndAnswers.append(correctAnswer) # ensure correct answer is always first in array
            for answer in answers: # ensure we do not append correct answer twice
                if not answer == correctAnswer:
                    questionAndAnswers.append(answer)
            questions.append(questionAndAnswers) # append question & answer combo to array for output
        
            return questions
                
        
                
#menu choices
#def Menu(button):
        #app.addLabel("lb1", "Please select an option: ")
        #app.addButton("1. Attachment", press2)
        #app.addButton("2. Social influence",press2)
        #app.addButton("3. Exit",press2)
        #print()
        #MenuChoice()

    
#select which to study 
#def MenuChoice():
    #Choice = input("> ")
    #if Choice == "1":
        #Attachment()
   # elif Choice == "2":
        #SocialInfluence()
   # elif Choice == "3":
       # exit(0)
    #else:
        #print("This is not an option. Please try again")
       # MenuChoice()


#Attachment options
def Attachment():
        print()
        app.addLabel("Please select the lesson: ")
        app.addButton("1. schaffer and emerson ")
        app.addButton("2. stages of Attachment")
        app.addButton("3. Exit")
        print()
        #AttachmentChoice()
#select which to study
def AttachmentChoice():
    Choice = input("> ")
    if Choice == "1":
        schafferEmerson()
    elif Choice == "2":
        StagesOfAttachment()
    elif Choice == "3":
        exit(0)
    else:
        print("This is not an option. Please try again")
        Attachment()


def stopApp(): # function to shut down program
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

app.setStopFunction(stopApp)


#main text - geometry 
app.setGeometry("1200x950")
app.setLocation("CENTER")

app.setBg("MintCream")
app.setFont(18)


app.addLabel("title1", "Psychology revision app")
app.setLabelFg("title1", "black")

app.addButtons(["Exit"], exitChoice)
app.addButtons(["Revision"], press2)
app.addButtons(["Questions"], press3)




#revision window
app.startSubWindow("Revision")
app.addLabel("lb3", "Please select an option: ")
app.addButton("1. Attachment", press2)
app.addButton("2. Social influence", press2)
app.addButton("3. Exit", exitChoice)
#app.hideSubWindow("Login")##################
app.setGeometry("1200x850")
app.setLocation("CENTER")
app.setBg("MintCream")
app.stopSubWindow()

###########
app.startSubWindow("Questions")
QuizQuestions()
app.addLabel(QuizQuestions)
#app.hideSubWindow("Login")##################
app.setGeometry("1200x850")
app.setLocation("CENTER")
app.setBg("MintCream")
app.stopSubWindow()


#Attachment window
app.startSubWindow("Attachment")
app.addLabel("lb2", "Please select the lesson: ")
app.addButton("schaffer", press2)
app.addButton("stages of Attachment", press2)
app.addButton("3.  Exit", exitChoice)

app.setGeometry("1200x950")
app.setLocation("CENTER")
app.setBg("MintCream")
app.stopSubWindow()








#schaffer and emerson window
app.startSubWindow("schaffer")

app.setGeometry("1200x850")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)
app.addMessage("l1", "Here is information about schaffer and emerson's stages of attatchment: ")
app.addMessage("l2", "Schaffer and Emerson (1964) studied 60 babies from Glasgow at monthly intervals for the first 18 months of life using a longitudinal method. ", 0, 1)




app.addMessage("l4", "Children were studied in their own homes and visited monthly for approx. a year.Interactions with carers were analysed to establish when infants started to display seperation anxiety ", 1, 0)
app.addMessage("l6", " Results revealed that attachments were most likely to form with carers who were sensitive to the baby's signals, rather than the person they spent the most time with.", 1, 1, 2)
app.addMessage("l7", "By 10 months old, most of the babies had multiple attachments. It was observed that the mother was the main attachment figure for roughly half of the babies when they were 18 months old and the father for most of the others. ", 2)
app.addMessage("l8", "Based on this finding, this would suggest that being sensitive and responsive (including playing and communicating an infant) is more instrumental in attachment development than physical care.", 2,1)
app.addButton("3.    Exit", exitChoice)
#app.addButton("back", back)

#app.startLabelFrame("l1", hideTitle=True)
#app.setLabelFrameAnchor("l1", "e")
#app.addLabel("l1", "row=0\ncolumn=0")
#app.stopLabelFrame()
                    
app.setMessageBg("l1", "LightYellow")
app.setMessageBg("l2", "blue")
app.setMessageBg("l4", "green")
app.setMessageBg("l6", "orange")
app.setMessageBg("l7", "yellow")
app.setMessageBg("l8", "purple")
app.stopSubWindow()




#stages of attachment window
app.startSubWindow("stages_of_Attachment")

#app.addButton("3.  Exit", exitChoice)


app.setGeometry("1200x850")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)
app.addMessage("l9", "Schaffer's observational research led to the formulation of four distinct stages of developmental progress that characterise infants' attachments:")
app.addMessage("l10", "Asocial stage (0-6 weeks) - Similar responses to objects & people. Preference for faces/ eyes.", 0,1)
app.addMessage("l11", "Indiscriminate attachments (6 weeks - 6 months) Preference for human company. Ability to distinguish between people but comforted indiscriminately. ", 1,0)




app.addMessage("l12", "Specific (7 months +) Infants show a preference for one caregiver, displaying separation and stranger anxiety. The baby looks to particular people for security, comfort and protection. ", 1,1,2)
app.addMessage("l13", "Multiple (10/11 months +) Attachment behaviours are displayed towards several different people eg. siblings, grandparents etc.", 2)
app.addMessage("l14", "5", 2 ,1)



                    
app.setMessageBg("l9", "LightYellow")
app.setMessageBg("l10", "blue")
app.setMessageBg("l11", "green")
app.setMessageBg("l12", "orange")
app.setMessageBg("l13", "yellow")
app.setMessageBg("l14", "purple")
app.stopSubWindow()



#Social Influence window
app.startSubWindow("Social influence")
app.addLabel("lb4", "Please select the lesson: ")
app.addButton("number1", press2) #types of conformity
app.addButton("number2", press2) #asch's study
#app.addButton("Exit", exitChoice)
#
app.setGeometry("1200x950")
app.setLocation("CENTER")
app.setBg("MintCream")
app.stopSubWindow()


app.setGeometry("1200x850")
app.setLocation("CENTER")
app.setBg("MintCream")
app.setFont(18)
#app.addLabel("title2", "Psychology revision app")
#app.setLabelFg("title2", "black")
#app.addButtons(["schaffer and emerson", "stages of Attachment", "exit"], press2)
#AttachmentChoice()





#types of conformity window
app.startSubWindow("number1") #types of conformity sub window

#app.addButton("3.  Exit", exitChoice)


app.setGeometry("1200x850")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)
app.addMessage("l15", "1")
app.addMessage("l16", "2 ", 0, 1)




app.addMessage("l17", "3 ", 1, 0)
app.addMessage("l18", "4 ", 1, 1, 2)
app.addMessage("l19", "5", 2)
app.addMessage("l20", "6", 2, 1)


                    
app.setMessageBg("l15", "LightYellow")
app.setMessageBg("l16", "blue")
app.setMessageBg("l17", "green")
app.setMessageBg("l18", "orange")
app.setMessageBg("l19", "yellow")
app.setMessageBg("l20", "purple")
app.stopSubWindow()



#asch's study window
app.startSubWindow("number2")

#app.addButton("3.  Exit", exitChoice)


app.setGeometry("1200x850")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)
app.addMessage("l21", "1")
app.addMessage("l22", "2 ", 0, 1)




app.addMessage("l23", "3 ", 1, 0)
app.addMessage("l24", "4 ", 1, 1, 2)
app.addMessage("l25", "5", 2)
app.addMessage("l26", "6", 2, 1)


                    
app.setMessageBg("l21", "LightYellow")
app.setMessageBg("l22", "blue")
app.setMessageBg("l23", "green")
app.setMessageBg("l24", "orange")
app.setMessageBg("l25", "yellow")
app.setMessageBg("l26", "purple")
app.stopSubWindow()







#login window
app.startSubWindow("Login")
#app = gui("Login Window", "400x200")
app.setBg("MintCream")
app.setFont(18)

app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "MintCream")
app.setLabelFg("title", "black")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")


app.addButtons(["Submit", "Cancel"], LoginScreenPress)
app.setFocus("Username")

app.stopSubWindow()
app.go(startWindow="Login")

