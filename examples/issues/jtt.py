import sys
sys.path.append("../../")
from appJar import gui

def login(btn):
    u = app.getEntry('Username')
    p = app.getEntry('Password')
    if u == '' or p == '':
        app.errorBox('Login Error', 'Enter in both username and password!')
    else:
        user = "a"#db.query(User).filter_by(username = u).one_or_none()
        if user != None:
            if True:#user.check_password(p):
                print('yay')
                app.clearEntry('Username')
                app.clearEntry('Password')
                app.setTransparency(100)
                app.hideSubWindow('L')
            else:
                app.errorBox('Login Error', 'Incorrect password!')
                app.clearEntry('Password')
                app.setFocus('Password')
        else:
            app.errorBox('Login Error', 'No user by {}!'.format(u))
            app.clearEntry('Username')
            app.clearEntry('Password')
            app.setFocus('Username')

def openLogin():
    app.showSubWindow('L')
    app.setFocus('Username')


#employee_list = [str(i[0]) for i in db.query(Finisher.initials).\
#                                        filter(Finisher.active == True).all()]
employee_list=["a", "aa"]

app = gui('SLA Sendback Entry')

# Login #
app.startSubWindow("L")
app.setLocation(900,400)
app.addLabelEntry('Username')
app.setFocus('Username')
app.addLabelSecretEntry('Password')
app.addButton('Login', login)
app.stopSubWindow()

# Data Entry
app.addLabel('l1', 'Sendback Data Entry')
app.addAutoEntry('Employee', employee_list)
app.setFocus('Employee')
app.addLabelEntry


app.setTransparency(0)
openLogin()
app.go()
