import sys
sys.path.append("../../")
from appJar import gui

# make the question array
questions = []
with open("questions.txt") as f:
    for line in f:
        parts = line.split(",")
        q = {}
        q["question"] = parts[0]
        q["options"] = parts[1:-1]
        q["answer"] = parts[-1].strip()
        questions.append(q)

score = 0

def showScore():
    app.label("score", "Score: " + str(score) + "/" + str(len(questions)))

def launcher(btn):
    app.showSubWindow(btn)

def check():
    global score
    qNum = app.getCurrentFrame("Questions")
    choice = app.radio(str(qNum))
    answer = questions[qNum]["answer"]

    if choice.strip() == answer.strip():
        app.infoBox("Correct", "You got it right")
        score += 1
        showScore()
    else:
        app.errorBox("Wrong", "You got it wrong")

    app.nextFrame("Questions")

with gui("Quiz Demo") as app:
    app.buttons(["Quiz", "Scores"], launcher)

    with app.subWindow("Quiz", modal=True):
        with app.frameStack("Questions", start=0):
            for pos, q in enumerate(questions):
                with app.frame():
                    with app.labelFrame("Question " + str(pos + 1)):
                        app.label(q["question"])
                        for o in q["options"]:
                            app.radio(str(pos), o)
        showScore()
        app.button("SUBMIT", check)

    with app.subWindow("Scores", modal=True):
        app.label("Scores")
