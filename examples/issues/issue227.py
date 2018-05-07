import sys
sys.path.append("../../")

from appJar import gui
#-----------------------------------------------------------------------------------
def AddBills(btn):
    Water = float(app.getEntry("Water"))
    Electric = float(app.getEntry("Electric"))
    Internet = float(app.getEntry("Internet"))
    VehicleLoan = float(app.getEntry("Vehicle Loan"))
    CreditCard = float(app.getEntry("Credit Card"))
    Mortgage = float(app.getEntry("Mortgage"))
    VehicleInsurance = float(app.getEntry("Vehicle Insurance"))

    app.setTextArea("Bill Sum", Water + Electric + Internet +
    VehicleLoan + CreditCard + Mortgage + VehicleInsurance)

# I can only use the Add Bills button when there are values in all of the entries
# As opposed to it allowing me to be able to add say just two entries
#-----------------------------------------------------------------------------------
app = gui("Bill Manager", "500x500")

app.setFont(20)
app.setBg("grey")

app.addEntry("Water", 0, 2)
app.addEntry("Electric", 1, 2)
app.addEntry("Internet", 2, 2)
app.addEntry("Vehicle Loan", 3, 2)
app.addEntry("Credit Card", 4, 2)
app.addEntry("Mortgage", 5, 2)
app.addEntry("Vehicle Insurance", 6, 2)
app.addButton("Add Bills", AddBills, 7, 2)
app.addTextArea("Bill Sum", 8, 2)

app.setEntryDefault("Water", "Water")
app.setEntryDefault("Electric", "Electric")
app.setEntryDefault("Internet", "Internet")
app.setEntryDefault("Vehicle Loan", "Vehicle Loan")
app.setEntryDefault("Credit Card", "Credit Card")
app.setEntryDefault("Mortgage", "Mortgage")
app.setEntryDefault("Vehicle Insurance", "Vehicle Insurance")

app.addCheckBox("Water", 0, 0)
app.addCheckBox("Electric", 1, 0)
app.addCheckBox("Internet", 2, 0)
app.addCheckBox("Vehicle Loan", 3, 0)
app.addCheckBox("Credit Card", 4, 0)
app.addCheckBox("Mortgage", 5, 0)
app.addCheckBox("Vehicle Insurance", 6, 0)
#-------------------------------------------------------------------------------------------------------
def update_meter():

    billList = [app.getCheckBox("Water"), app.getCheckBox("Electric"), app.getCheckBox("Internet"),
                app.getCheckBox("Vehicle Loan"), app.getCheckBox("Credit Card"),
                app.getCheckBox("Mortgage"), app.getCheckBox("Vehicle Insurance")]

    bill_value = [0]

    for bill in billList:
        if bill is True:
            bill_value.append(14.2857142857)
    addValues = sum(bill_value)
    app.setMeter("Progress", addValues)

# I can get the meter to go up to add the percentage completed -
# but the meter starts to glitch from a higher value to a lesser value
# I'm also trying to figure out how to subtract values from the percentage complete -
# When the user unselects the box
#-------------------------------------------------------------------------------------------------------

app.registerEvent(update_meter)

app.addMeter("Progress")
app.setMeterFill("Progress", "green")

app.go()
