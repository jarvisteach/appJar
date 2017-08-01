

"""
This code demonstrates "bare bones" drag and drop
"""

from Tkinter import *
import Tkdnd

class Dragged:
    """
    This is a thing to be dragged and dropped.
    """
    def __init__(self):
        print "An instance of Dragged has been created"
        
    def dnd_end(self,Target,Event):
        #this gets called when we are dropped
        print "I have been dropped; Target=%s"%`Target`

class CanvasDnd(Canvas):
    """
    This is a canvas to which we have added a "dnd_accept" method, so it
    can act as a Target Widget for drag and drop. To prove that the Target
    Object can be different from the Target Widget, CanvasDnd accepts as
    argument "GiveDropTo" the object to which the dropped object is to 
    be given.
    """    
    def __init__(self, Master, GiveDropTo, **kw):
        Canvas.__init__(self, Master, kw)
        #Simply remember the TargetObject for later use.
        self.GiveDropTo = GiveDropTo

    def dnd_accept(self,Source,Event):
        #Tkdnd is asking us if we want to tell it about a TargetObject.
        #We do, so we pass it a reference to the TargetObject which was
        #given to us when we started
        print "Canvas: dnd_accept"
        return self.GiveDropTo

class Receptor:
    """
    This is a thing to act as a TargetObject
    """
    def dnd_enter(self,Source,Event):
        #This is called when the mouse pointer goes from outside the
        #Target Widget to inside the Target Widget.
        print "Receptor: dnd_enter"
        
    def dnd_leave(self,Source,Event):
        #This is called when the mouse pointer goes from inside the
        #Target Widget to outside the Target Widget.
        print "Receptor: dnd_leave"
        
    def dnd_motion(self,Source,Event):
        #This is called when the mouse pointer moves withing the TargetWidget.
        print "Receptor: dnd_motion"
        
    def dnd_commit(self,Source,Event):
        #This is called if the DraggedObject is being dropped on us
        print "Receptor: dnd_commit; Object received= %s"%`Source`

def on_dnd_start(Event):
    """
    This is invoked by InitiationObject to start the drag and drop process
    """
    #Create an object to be dragged
    ThingToDrag = Dragged()
    #Pass the object to be dragged and the event to Tkdnd
    Tkdnd.dnd_start(ThingToDrag,Event)

Root = Tk()
Root.title("Drag-and-drop 'bare-bones' demo")
#Create an object whose job is to act as a TargetObject, that is, to
# received the dropped object.
TargetObject = Receptor()

#Create a button to act as the InitiationObject and bind it to <ButtonPress> so
# we start drag and drop when the user clicks on it.
InitiationObject = Button(Root,text='InitiationObject')
InitiationObject.pack(side=TOP)
InitiationObject.bind('<ButtonPress>',on_dnd_start)

#Create a canvas to act as the Target Widget for the drag and drop. Note that
# since we are going out of our way to have the Target Widget and the Target
# Object be different things, we pass a reference to the Target Object to
# the canvas we are creating.
TargetWidget = CanvasDnd(Root,GiveDropTo=TargetObject,relief=RAISED,bd=2)
TargetWidget.pack(expand=YES,fill=BOTH)

Root.mainloop()
