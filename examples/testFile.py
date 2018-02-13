import sys
sys.path.append("../")
from appJar import gui

def getQuestions(fileName = "questions.txt"):
    questions = []
    data = None
    with open(fileName, "r") as questionsFile:
        while True:
            line = questionsFile.readline().strip()

            if line == "EOF": break             # end of file reached
            elif line.startswith("-"): continue # ignore these lines

            elif line.startswith("#"):          # start of question
                # we need to add our last question
                if data is not None:
                    questions.append(data)
                data = {"question":"", "options":[], "answer":""}

                question = line[5:].strip()
                nextLine = questionsFile.readline().strip()
                if not nextLine.startswith("------"):
                    question += " " + nextLine
                data["question"] = question

            elif line.startswith("*"):          # answer option
                option = line[1:]
                data["options"].append(option)

            elif line.startswith("Answer:"):    # answer
                answer = line[8:]
                data["answer"] = answer

    return questions

def checkAnswer(question):
    selection = app.getRadioButton(question)
    answer = questions[int(question[1:])-1]["answer"]

    if selection == answer:
        app.infoBox("CORRECT", "You got it!")
    else:
        app.infoBox("WRONG", "Try again!")

with gui("QUIZ") as app:
    questions = getQuestions()
    with app.pagedWindow("QUIZ DEMO"):
        count = 0
        for q in questions:
            count += 1
            title = "Q" + str(count)
            with app.page():
                app.setSticky("EW")
                app.addLabel(title, title + ": " + q["question"])
                app.setLabelBg(title, "green")
                with app.labelFrame(title, hideTitle=True):
                    for o in q["options"]:
                        app.addRadioButton(title, o)
                app.addNamedButton("CHECK", title, checkAnswer)
