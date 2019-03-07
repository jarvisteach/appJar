import socket
import sys
sys.path.append("../../../../")
from appJar import gui

connected = False
sock = None
count = 0

def connServ():
      global sock, connected
      try:
            sock = socket.socket()
            sock.connect(("localhost", 9999))
            sock.settimeout(0.01)
            connected=True
            print ( "Connected...")
      except Exception as e:
            print ("Failed to connect: ", e )
            connected=False

# function to handle the button presses
def press(btn):
      global sock, connected
      try:
            connServ()
            mess =  win.getEntry ( "Msg" )
            sock.send(mess.encode('ascii') )
            win.addListItem( "messages",  "Sent:     " + mess )
            print("Received:", mess)
            win.clearEntry("Msg")
      except Exception as e:
            win.errorBox("Network Error", "Unable to contact server:"+str(e))
            sock.close()
            connected = False
            print ("Failed to send:", e)

def checkForMsg():
      print("Checking for messages....")
      global sock, connected, count
      if not connected:
            connServ()
            print("Connected to server")
      try:
            recv = sock.recv(1024).decode()
            if len(recv) > 0:
                  win.addListItem( "messages",  "Received: " + recv )
                  count = count + 1
                  win.setTitle("Chat: " + str(count) )
            sock.send(str(chr(24)).encode('ascii') )
      except Exception as e:
            print ( "Failed to receive message:", e )

# create and configure the GUI
win = gui ( "Chat" )
win.setFont ( 16 )
win.setBg ( "yellow" )
win.addListBox ( "messages" )
win.addLabelEntry ( "Msg" )
win.setEntryWidth ( "Msg", 15 )
win.setEntrySubmitFunction ( "Msg", press )
win.setFocus ( "Msg" )
win.registerEvent(checkForMsg)
win.go ( )

sock.close()
