import sys
sys.path.append('../')
import random

COLOURS = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white']
currentRound = 1
a = b = c = d = 0
target = []

while len(target) < 4:
    col = random.choice(COLOURS)
    if col not in (target) and col != 'black':
        target.append(col)
    
from appJar import gui

def findDups(pegs):
    if pegs[0] in pegs[1:] or pegs[1] in pegs[2:] or pegs[2] in pegs[3:]:
        return True
    else:
        return False

def press(btn):
    global a, b, c, d, currentRound
    if btn == 'a'+str(currentRound):
        a += 1
        if a > 8: a = 0
        app.setLabelBg('a'+str(currentRound), COLOURS[a])
    elif btn == 'b'+str(currentRound):
        b += 1
        if b > 8: b = 0
        app.setLabelBg('b'+str(currentRound), COLOURS[b])
    elif btn == 'c'+str(currentRound):
        c += 1
        if c > 8: c = 0
        app.setLabelBg('c'+str(currentRound), COLOURS[c])
    elif btn == 'd'+str(currentRound):
        d += 1
        if d > 8: d = 0
        app.setLabelBg('d'+str(currentRound), COLOURS[d])
    elif btn == 'GO'+str(currentRound):
        guess = [COLOURS[a], COLOURS[b], COLOURS[c], COLOURS[d]]
        if findDups(guess):
            app.errorBox("Error", "No duplicates")
            return
        app.disableButton('GO'+str(currentRound))
        if guess == target:
            for res in range(1,5):
                app.setLabelBg(str(res)+str(currentRound), 'red')
            app.infoBox("WINNER", "You guessed in " + str(currentRound) + " rounds.")
        else:
            done = []
            whites = 0
            reds = 0

            for pos in range(len(guess)):
                if guess[pos] == target[pos] and guess[pos] not in done:
                    reds+= 1
                    done.append(guess[pos])
                elif guess[pos] in target and guess[pos] not in done:
                    whites += 1
                    done.append(guess[pos])

            for res in range(1,5):
                if reds > 0:
                    reds -= 1
                    app.setLabelBg(str(res)+str(currentRound), 'red')
                elif whites > 0:
                    whites -= 1
                    app.setLabelBg(str(res)+str(currentRound), 'white')
            currentRound += 1
            newRow()

def newRow():
    with app.labelFrame('Round ' + str(currentRound), row=currentRound):
        app.config(sticky='news', bg='grey', fg='white', padding=(2,2))
        app.label('a'+str(currentRound), '', bg=COLOURS[a], submit=press, width=6)
        app.label('b'+str(currentRound), '', bg=COLOURS[b], pos=('p', 1), submit=press, width=6)
        app.label('c'+str(currentRound), '', bg=COLOURS[c], pos=('p', 2), submit=press, width=6)
        app.label('d'+str(currentRound), '', bg=COLOURS[d], pos=('p', 3), submit=press, width=6)
        app.addNamedButton('GO', 'GO'+str(currentRound), press, row='p', column=4)
        with app.frame('feedback'+str(currentRound), row='p', column=5):
            app.config(sticky='news', bg='grey', fg='white', padding=(2,2))
            app.label('1'+str(currentRound), '', bg='black', width=3)
            app.label('2'+str(currentRound), '', bg='black', pos=('p', 1), width=3)
            app.label('3'+str(currentRound), '', bg='black', width=3)
            app.label('4'+str(currentRound), '', bg='black', pos=('p', 1), width=3)

with gui('Mastermind', bg='green') as app:
    newRow()
