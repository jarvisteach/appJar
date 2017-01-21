from appJar import gui
import calendar
import datetime

STARTDATE = 1920
ENDDATE = 2020
MONTH_NAMES = calendar.month_name[1:]

def updateDays(btn=None):
    day = app.getOptionBox("Day")
    month = MONTH_NAMES.index(app.getOptionBox("Month")) + 1
    year = int(app.getOptionBox("Year"))
    days = range(1, calendar.monthrange(year, month)[1]+1)
    app.changeOptionBox("Day", days)
    # keep previous date possible
    try: app.setOptionBox("Day", day)
    except: pass

def getDate():
    day = int(app.getOptionBox("Day"))
    month = MONTH_NAMES.index(app.getOptionBox("Month")) + 1
    year = int(app.getOptionBox("Year"))
    date = datetime.date(year, month, day)
    return date

def setDate(date):
    app.setOptionBox("Day", date.day-1)
    app.setOptionBox("Month", date.month-1)
    app.setOptionBox("Year", str(date.year))

def showDate(btn):
    print(getDate())

def buildWidgets():
    days = []
    years=range(STARTDATE, ENDDATE)

    app.startFrame("Cal")
    app.addLabel("dl", "Day:", 0, 0)
    app.setLabelAlign("dl", "w")
    app.addOptionBox("Day", days, 0, 1)
    app.addLabel("ml", "Month:", 1, 0)
    app.setLabelAlign("ml", "w")
    app.addOptionBox("Month", MONTH_NAMES,1,1)
    app.addLabel("yl", "Year:", 2, 0)
    app.setLabelAlign("yl", "w")
    app.addOptionBox("Year", years,2,1)
    app.setOptionBoxFunction("Month", updateDays)
    app.setOptionBoxFunction("Year", updateDays)
    app.addButton("GET", showDate, 3, 0, 2)
    app.stopFrame()

    updateDays()

app=gui()
buildWidgets()
setDate(datetime.date.today())
app.go()
