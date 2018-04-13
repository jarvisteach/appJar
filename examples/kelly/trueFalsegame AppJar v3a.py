import sys
sys.path.append("../../")
# attempt to use sub-windows
from random import *
import sqlite3 as lite
from appJar import gui
import time

def main():
    main_game()
# deals with the event to open the sub window
def level(btn):
    main_game.showSubWindow("Level")
# interrogates the dbase to get the questions and 
def pose_question (btn):
    level_choice=(main_game.getOptionBox("Select Level"))
    print(level_choice)
    main_game.hideSubWindow("Level")
    
     # connect to questions bank
    con = lite.connect ('true_false_game.db') 
    cur = con.cursor() 
    s = '''SELECT statement, trueFalse from QuestionBank'''
    cur.execute(s) 
    options = cur.fetchall() # collecting qs from db - works!
    boolean_list = [[1,"AND"], [2,"OR"], [3,"NAND"], [4,"NOR"]]
    global opt1
    global opt2
    global boolean
    global index3
    global answer1
    global answer2
    if level_choice == "Easy":
        index1_L1 = randint(0,9)
        index2_L1 = randint (0,9)
        opt1 = options[index1_L1][0] #chosing 2 options from the dictionary of true/false statements
        opt2 = options[index2_L1][0]
        answer1 = eval(options [index1_L1][1])
        answer2 = eval(options [index2_L1][1])       
    elif level_choice == "Medium":
        index1_L2 = randint(10,19)
        index2_L2 = randint (10,19)
        opt1 = options[index1_L2][0] 
        opt2 = options[index2_L2][0]
        answer1 = eval(options [index1_L2][1]) # eval?
        answer2 = eval(options [index2_L2][1])
    elif level_choice =="Difficult":
        index1_L3 = randint(20,29)
        index2_L3 = randint (20,29)
        opt1 = options[index1_L3][0] 
        opt2 = options[index2_L3][0]
        answer1 = eval(options [index1_L3][1])
        answer2 = eval(options [index2_L3][1])
    
    index3 = randint(0,3)
    boolean = boolean_list[index3][1] #returning the key from the random value that was generated
    print ("Look at the statement: will the output be True or False?")
    print("~~~~~~~~~~ {}   {}   {} ~~~~~~~~~~".format( opt1, boolean, opt2))

    #### ADDED THESE THREE LINES ####
    main_game.setLabel("l4", opt1)
    main_game.setLabel("l5", boolean)
    main_game.setLabel("l6", opt2)

    main_game.show()
    
# main game GUI with sub window to select level using pose_question function
def main_game():
    global main_game
    global question
    opt1="test"
    opt2="test"
    boolean = "OR"
    question = 1
    main_game= gui("main_game", "800x600")
    main_game.addButton("Start", level)
    main_game.startSubWindow("Level")
    main_game.setStopFunction(stopSub)
    main_game.setBg("Red")
    main_game.addOptionBox("Select Level", ["Easy", "Medium","Difficult"])
    main_game.addButton("Go", pose_question)
    main_game.stopSubWindow()
    main_game.setBg("purple")
    # title, levels and options
    main_game.setSticky("ew")
    main_game.setExpand("both")
    main_game.setBg("MediumPurple1")
    main_game.setFg("purple4")
    main_game.addImage("logo", "true_false.gif",0,0,1)
    main_game.setFont(20)
    main_game.addLabel("l1", "True False Game",0,2)
    main_game.addLabel("Question",("Question ",question), 1,0,2)
    main_game.addLabel("l2", "Answer True or False to the following expressions", 2,0,4)
    main_game.setSticky("ew")
    main_game.addLabel("l4", opt1, 3,0)
    main_game.addLabel("l5", boolean, 3,2)
    main_game.addLabel("l6", opt2,3,4)
    # link the buttons to the function called press
    main_game.addButtons(["TRUE", "FALSE"], main_game_answer, 6,0,3)
    main_game.addButtons(["Next Question", "Quit"], main_game_next,6,3)
    main_game.go(startWindow="Level")
    
def stopSub(btn=None):
    return False

def main_game_answer():
    return False
def main_game_next():
    return False
main()
