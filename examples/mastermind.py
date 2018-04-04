# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import random
from appJar import gui

COLOURS = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white']
HELP_MESSAGE = """Mastermind is a code-breaking game, in which the codebreaker (you) is trying to guess a randomly generated pattern.

Each guess is made by choosing four different colours on the decoding board.

The codemaker (the computer) will provide feedback by colouring the four pegs to the right of the decoding board.

A red peg indicates a guess that is correct in both colour and position, a white peg indicates a correct guess, in the wrong position."""
ERROR_MESSAGE = """Duplicates aren't allowed.

Please ensure you have selected four different colours."""

currentRound = 1
codePegs = [0, 0, 0, 0]
bestScore = 999

pattern = [] # stores the pegs to guess
while len(pattern) < 4:
    col = random.choice(COLOURS[1:])
    if col not in (pattern):
        pattern.append(col)

def change(peg): # called when pressing a peg label
    if int(peg[1:]) == currentRound:
        peg = int(peg[0])
        codePegs[peg] = (codePegs[peg] + 1) % 9
        app.setLabelBg(str(peg)+str(currentRound), COLOURS[codePegs[peg]])

def guess(btn): # called when pressing the guess button
    global currentRound, bestScore, codePegs
    guess = [COLOURS[codePegs[0]], COLOURS[codePegs[1]], COLOURS[codePegs[2]], COLOURS[codePegs[3]]]

    if guess[0] in guess[1:] or guess[1] in guess[2:] or guess[2] in guess[3:]:
        app.errorBox("Error", ERROR_MESSAGE)
    else:
        app.disableButton('GO'+str(currentRound))
        if guess == pattern:
            for res in range(4):
                app.setLabelBg("p"+str(res)+str(currentRound), 'red')
            app.infoBox("Winner", "You guessed in " + str(currentRound) + " rounds.")
            if currentRound < bestScore:
                bestScore = currentRound
            currentRound = 1
            codePegs = [0, 0, 0, 0]
            app.removeAllWidgets()
        else:
            done = []
            for i in range(4):
                if guess[i] == pattern[i]:
                    done.append("red")
                elif guess[i] in pattern:
                    done.append("white")
            done.sort()

            for i in range(len(done)):
                app.setLabelBg("p"+str(i)+str(currentRound), done[i])
            currentRound += 1
        newRow()

def getHelp():
    app.popUp("Help", HELP_MESSAGE)

def newRow():
    if currentRound == 1:
        score = str(bestScore) if bestScore < 999 else "???"
        app.label("score", "Best score: " + score, fg="yellow", font={'weight':'bold', 'size':16})
        app.link("help", getHelp, pos=(0,0), sticky="e", font={'size':9})

    with app.labelFrame('Round ' + str(currentRound), row=currentRound, sticky='news', padding=(2,2)):
        for i in range(4): # add the four labels for player choices
            app.label(str(i)+str(currentRound), '', bg=COLOURS[codePegs[i]], pos=(currentRound, i), submit=change, width=6)
        app.addNamedButton('GO', 'GO'+str(currentRound), guess, row=currentRound, column=4)
        with app.frame('feedback'+str(currentRound), row=currentRound, column=5, sticky='news', padding=(2,2)):
            for x in range(2): # add agrid of four labels for feedback
                for y in range(2):
                    app.label('p' + str(x*2+y) + str(currentRound), '', bg='black', pos=(x, y), width=3)
    app.location=("c", 50)

with gui('Mastermind', bg='grey', fg='white', sticky="new", stretch="none") as app:
    newRow()
