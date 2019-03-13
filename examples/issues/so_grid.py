import sys
sys.path.append("../../")

def openSub(): print('open sub')
def addCourse(): print('open sub')
def addTask(): print('open sub')

from appJar import gui

app = gui("Organizer", "900x600")

app.setSticky("ne")
app.setExpand("none")

app.setLabelFont("title", "Calibri")

#Adding Widgets#
app.addLabel("title", "Organizing studies")

app.addButton("Login", openSub, row=0, column=1)

app.setExpand('both')
app.setSticky('news')

#Courses Panel
app.startLabelFrame("Courses",row=1,column=0,rowspan=14,sticky="news")
app.addTable("Courses",[["Course","Start","End","Open"]])
app.stopLabelFrame()

#Tasks Panel
app.startLabelFrame("Tasks",row=1,column=1,rowspan=14,sticky="news")
app.addTable("Tasks",[["Task","End","Open"]])
app.stopLabelFrame()

app.setExpand('none')
app.setSticky('ne')

app.addButton("Add Course",addCourse,row=16,column=0)
app.addButton("Add Task",addTask,row=16,column=1)
#for i in range(2,18):
#    app.addEmptyLabel("{0}".format(i),row=i,colspan=0)
app.go()
