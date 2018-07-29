import sys
sys.path.append("../../")
import string

FREQUENCIES = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41,
                6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]

freq = {}
letCount = 0

from appJar import gui

def resetFreq():
    global letCount
    for f in freq: freq[f] = 0
    letCount = 0

def updateFreq():
    for f in freq: app.label(f+'_c', str(freq[f]))
    for f in freq:
        try: app.label(f+'_f', str(round(freq[f]/float(letCount)*100, 2)))
        except: app.label(f+'_f', '0.0')

def lock(key):
    if app.check(key): app.disableEntry(key)
    else: app.enableEntry(key)

    val = app.entry(key)
    if not app.check(key):
        for i, c in enumerate(app.text('text')):
            if c == val:
                app.textAreaUntagRange('text', 'red', '1.'+str(i), '1.'+str(i+1))
    else:
        app.textAreaTagPattern('text', 'red', val)

def retag():
    vals = app.getAllCheckBoxes()
    for v in vals:
        if vals[v]:
            app.textAreaTagPattern('text', 'red', app.entry(v))

# called when letters are changed
def update(key):
    global letCount
    resetFreq()
    cipher = app.text('ciphertext').upper()
    codes = app.getAllEntries()
    text = ''
    letCount = 0
    for c in cipher:
        try:
            text += codes[c]
            freq[c] = freq[c] + 1
            letCount += 1
        except:
            text += c
    app.text('text', text, replace=True)
    retag()
    updateFreq()

# make the GUI
with gui('Cipher Analysis', bg='grey') as app:
    for i, l in enumerate(string.ascii_uppercase):
        freq[l] = 0
        app.label(l+"_c", "0", pos=(0, i), fg='red')
        app.label(l+"_f", "0", pos=(1, i), fg='red')
        app.label(l, pos=(2, i))
        app.entry(l, l, pos=(3, i), width=2, fg='blue', change=update, case='upper')
        app.check(l, False, pos=(4, i), change=lock, label='')

    with app.tabbedFrame("tabs", colspan=26, stretch='both'):
        with app.tab("Text"):
            app.text("ciphertext", colspan=26, height=12, change=update)
            app.text("text", colspan=26, height=12)
        with app.tab("Frequencies"):
            for i, l in enumerate(string.ascii_uppercase):
                app.label('f_'+l, l+": " + str(FREQUENCIES[i]), row=i%13, col=i//13)

    app.textAreaCreateTag("text", "red", background="red", foreground="white")
    app.status()
