import sys
sys.path.append("../../")
from appJar import gui

def login(btn): print(btn)

def openLogin():
    app.showSubWindow('L')


app = gui('SLA Sendback Entry')

# Login #
app.startSubWindow("L")#, modal=True)
app.addLabelEntry('Username')
app.setFocus('Username')
app.addLabelSecretEntry('Password')
app.addButton('Login', login)
app.stopSubWindow()

app.addLabelEntry('Entry')
app.setFocus('Entry')

openLogin()
app.go()
