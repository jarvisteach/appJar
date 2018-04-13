import sys
sys.path.append("../../")

from appJar import gui

app = gui("Login Form")

mess = app.addMessage("Message","Veuillez entrer les parametres de votre système d\'équation.", 0, 0, colspan=2)
#mess.config(aspect=600)
app.setMessageWidth("Message", 200)
app.setMessageBg("Message", "blue")

app.addLabel("nbrEquations", "Nombre d'équations:", 1, 0)
app.addNumericEntry("userEnt", 1, 1)

app.addLabel("nbrUnknowns", "Nombre d\'inconnues:", 2, 0)
app.addNumericEntry("passEnt", 2, 1)

app.addButtons(["Create", "Cancel"], None, colspan=3)
app.go()
