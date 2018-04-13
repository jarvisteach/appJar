# attempt to use sub-windows
from random import *
import sqlite3 as lite
from appJar import gui

# CONSTANTS
BOOLEAN_LIST = [[1,"AND"], [2,"OR"], [3,"NAND"], [4,"NOR"]]

# connect to questions bank
con = lite.connect ('true_false_game.db') 
cur = con.cursor() 
s = '''SELECT statement, trueFalse from QuestionBank'''
cur.execute(s) 
OPTIONS = cur.fetchall() # collecting qs from db - works!

# called when the TRUE/FALSE buttons are pressed
def navigate(btn):
    # work out the solution
    if boolean == "AND": solution = answer1 and answer2
    elif boolean == "OR": solution = answer1 or answer2
    elif boolean == "NAND": solution = not(answer1 and answer2)
    elif boolean == "NOR": solution = not(answer1 or answer2)

    # check the answer
    if (btn == "True" and solution) or (btn == "False" and not solution):
        app.infoBox("Correct", "You got it!")
        # show next question
        populate_question()
    else:
        app.errorBox("Wrong", "Try again!")

# interrogates the dbase to get the questions and 
def pose_question (btn):
    app.showSubWindow("Main Game")
    populate_question()

def populate_question():
    level_choice = app.getOptionBox("Select Level")
    if level_choice == "Easy": start = 0
    elif level_choice == "Medium": start = 10
    elif level_choice =="Difficult": start = 20

    # generate random numbers
    index1 = randint(start, start+9)
    index2 = randint(start, start+9)
    index3 = randint(0,3)

    # get the random question details
    opt1 = OPTIONS[index1][0] 
    opt2 = OPTIONS[index2][0]

    global answer1, answer2, boolean
    answer1 = OPTIONS[index1][1]
    answer2 = OPTIONS[index2][1]
    boolean = BOOLEAN_LIST[index3][1]

    # update the GUI
    app.setLabel("opt1", opt1)
    app.setLabel("boolean", boolean)
    app.setLabel("opt2", opt2)

def make_gui():
    global app
    app = gui("Level")

    # populate the level selector
    app.setBg("Red")
    app.addOptionBox("Select Level", ["Easy", "Medium","Difficult"])
    app.addButton("Go", pose_question)

    # populate the game screen
    app.startSubWindow("Main Game", modal=True)
    # configure it
    app.setSize("500x200")
    app.setBg("MediumPurple1")
    app.setFg("purple4")
    app.setFont(20)
    # add widgets
    app.addImage("logo", "true_false.gif", 0, 0)
    app.addLabel("l1", "True False Game", 0,1,2)
    app.addLabel("l2", "Answer True or False to the following expression:", 1,0,3)
    # these will be populated later
    app.addLabel("opt1", "<<BLANK>>", 2, 0)
    app.addLabel("boolean", "<<BLANK>>", 2, 1)
    app.addLabel("opt2", "<<BLANK>>", 2, 2)

    app.addButtons(["True", "False"], navigate, 3, 0, 3)
    app.stopSubWindow()

    # start the GUI
    app.go()
    
make_gui()
