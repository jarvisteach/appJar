import sys
sys.path.append("../")
#Question Text, Answer A Text, Answer B Text, Correct Answer
questions = [["What language is this?","Python","Pascal","A"],["Did GB win any winter olympic medals?","YES","NO","A"]]

from appJar import gui

questionNum = 0
score = 0

def press(btn):
    global score, questionNum
    if btn == questions[questionNum][3]:
        app.setBg("green")
        app.infoBox("Well done", "That is correct")
        score += 1
    else:
        app.setBg("red")
        app.errorBox("Doh", "That is incorrect")

    questionNum += 1
    updateStatus()
    showQuestion()

def updateStatus():
    app.setStatusbar("Progress: " + str(questionNum) + " of " + str(len(questions)), 0)
    app.setStatusbar("Score: " + str(score), 1)

def showQuestion():
    if questionNum == len(questions):
        app.infoBox("Finished", "Your score was: " + str(score) + "/" + str(len(questions)))
        app.stop()
    else:
        app.setBg("grey")
        app.setLabel("question_number_lbl", "Question Number "+str(questionNum+1))
        app.setLabel("question_lbl", questions[questionNum][0])
        app.setLabel("answer1_lbl", "Option A "+questions[questionNum][1])
        app.setLabel("answer2_lbl", "Option B "+questions[questionNum][2])


app = gui("Quiz Master", "300x200")
app.setBg("grey")

app.addLabel("title","Quiz!")
app.addEmptyLabel("question_number_lbl")
app.addEmptyLabel("question_lbl")
app.addEmptyLabel("answer1_lbl")
app.addEmptyLabel("answer2_lbl")

app.addButtons(["A", "B"],press)
app.addStatusbar(fields=2)

showQuestion()

app.go()
