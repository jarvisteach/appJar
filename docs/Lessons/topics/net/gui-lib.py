from rwbatools import gui
from rwbatools import net

count = 0
loop = 0

# function to handle the button presses
def press(btn):
      mess =  win.getEntry ( "Msg" )
      if len(mess) > 0:
            if net.sendMessage(mess):
                  win.addListItem( "messages",  "Sent:     " + mess )
                  win.clearEntry("Msg")
            else:
                  win.errorBox("Network Error", "Unable to contact server.")

# called by GUI thread every 500 seconds
def checkForMsg():
      global loop
      print("Checking", loop)
      loop +=1
      global count
#      if net.ping():
#            win.setLabelBg("status", "green")
#            win.setLabel("status", "Server UP")
#            win.enableEntry("Msg")
#      else:
#            win.setLabelBg("status", "red")
#            win.setLabel("status", "Server DOWN")
#            win.disableEntry("Msg")
#
      msg = net.getMessage()
      if msg is not None and len(msg) > 0:
            win.addListItem( "messages",  "Received: " + msg )
            count = count + 1
            win.setTitle("Chat: " + str(count) )

# create and configure the GUI
net = net(9999)

win = gui ( "Chat" )
win.setFont ( 16 )
win.setBg ( "yellow" )

win.addRadioButton("Server", "Client", 0, 0)
win.addRadioButton("Server", "Server", 0, 1)

win.addEntry("ip", colspan=2)
win.setEntry("ip", str(net.getIPAddress()) )
win.addListBox ( "messages" , colspan=2)
win.addLabelEntry ( "Msg" , colspan=2)
win.setEntryWidth ( "Msg", 15 )
win.setEntryFunction ( "Msg", press )
win.setFocus ( "Msg" )
win.addEmptyLabel("status", colspan=2)
win.setPollTime(500)
win.registerEvent(checkForMsg)
win.go ( )

net.close()
