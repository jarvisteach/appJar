# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import random
from appJar import gui

COLOURS = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white']
currentRound = 1
codePegs = [0, 0, 0, 0]

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

def guess(btn):
    global currentRound
    rnd = int(btn[2:])
    guess = [COLOURS[codePegs[0]], COLOURS[codePegs[1]], COLOURS[codePegs[2]], COLOURS[codePegs[3]]]

    if guess[0] in guess[1:] or guess[1] in guess[2:] or guess[2] in guess[3:]:
        app.errorBox("Error", "No duplicates")
    else:
        app.disableButton('GO'+str(currentRound))
        if guess == pattern:
            for res in range(4):
                app.setLabelBg("p"+str(res)+str(currentRound), 'red')
            app.infoBox("WINNER", "You guessed in " + str(currentRound) + " rounds.")
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

def newRow():
    with app.labelFrame('Round ' + str(currentRound), row=currentRound, sticky='news', padding=(2,2)):
        for i in range(4):
            app.label(str(i)+str(currentRound), '', bg=COLOURS[codePegs[i]], pos=(currentRound, i), submit=change, width=6)
        app.addNamedButton('GO', 'GO'+str(currentRound), guess, row=currentRound, column=4)
        with app.frame('feedback'+str(currentRound), row=currentRound, column=5, sticky='news', padding=(2,2)):
            for x in range(2):
                for y in range(2):
                    app.label('p' + str(x*2+y) + str(currentRound), '', bg='black', pos=(x, y), width=3)

with gui('Mastermind', bg='grey', fg='white') as app:
    newRow()
