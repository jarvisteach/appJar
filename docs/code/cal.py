from appJar import gui
import calendar

def setDays(btn):
    month = months.index(app.getOptionBox("Month")) + 1
    year = int(app.getOptionBox("Year"))
    days = range(1, calendar.monthrange(year, month)[1]+1)

    app.changeOptionBox("Day", days)



startDate = 1920
endDate = 2020

days = []
months = calendar.month_name[1:]
years=range(startDate, endDate)

app=gui()

app.addLabelOptionBox("Day", days)
app.addLabelOptionBox("Month", months)
app.addLabelOptionBox("Year", years)
app.setOptionBoxFunction("Month", setDays)
app.setOptionBoxFunction("Year", setDays)


app.go()
