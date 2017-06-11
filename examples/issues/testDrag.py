import sys
sys.path.append("../../")
import Tkdnd
import types

from appJar import gui

class Dragged:
    """
    This is a prototype thing to be dragged and dropped.
    
    Derive from (or mixin) this class to creat real draggable objects.
    """
    #We use this to assign a unique number to each instance of Dragged.
    #    This isn't a necessity; we do it so that during the demo you can
    #    tell one instance from another.
    NextNumber = 0
    
    def __init__(self):
        Blab(1, "An instance of Dragged has been created")
        #When created we are not on any canvas
        self.Canvas = None
        self.OriginalCanvas = None
        #This sets where the mouse cursor will be with respect to our label
        self.OffsetX = 20
        self.OffsetY = 10
        #Assign ourselves a unique number
        self.Number = Dragged.NextNumber
        Dragged.NextNumber += 1
        #Use the number to build our name
        self.Name = 'DragObj-%s'%self.Number
        
    def dnd_end(self,Target,Event):
        #this gets called when we are dropped
        Blab(1, "%s has been dropped; Target=%s"%(self.Name,`Target`))
        if self.Canvas==None and self.OriginalCanvas==None:
            #We were created and then dropped in the middle of nowhere, or
            #    we have been told to self destruct. In either case
            #    nothing needs to be done and we will evaporate shortly.
            return
        if self.Canvas==None and self.OriginalCanvas<>None:
            #We previously lived on OriginalCanvas and the user has
            #   dragged and dropped us in the middle of nowhere. What you do
            #   here rather depends on your own personal taste. There are 2 choices:
            #   1) Do nothing. The dragged object will simply evaporate. In effect
            #      you are saying "dropping an existing object in the middle
            #      of nowhere deletes it".  Personally I don't like this option because
            #      it means that if the user, while dragging an important object, 
            #      twitches their mouse finger as the object is in the middle of
            #      nowhere then the object gets immediately deleted. Oops.
            #   2) Resurrect the original label (which has been there but invisible)
            #      thus saying "dropping an existing dragged object in the middle of
            #      nowhere is as if no drag had taken place". Thats what the code that
            #      follows does.
            self.Canvas = self.OriginalCanvas
            self.ID = self.OriginalID
            self.Label = self.OriginalLabel
            self.Label['text'] = self.OriginalText
            self.Label['relief'] = RAISED
            #We call the canvases "dnd_enter" method here to keep its ObjectDict up
            #    to date. We know that we had been dragged off the canvas, so before
            #    we call "dnd_enter" the cansases ObjectDict says we are not on the
            #    canvas. The call to "dnd_enter" will till the canvas that we are,
            #    in effect, entering the canvas. Note that "dnd_enter" will in turn
            #    call our "Appear" method, but "Appear" is smart enough to realize
            #    that we already have a label on self.Canvas, so it quietly does
            #    does nothing,
            self.Canvas.dnd_enter(self,Event)
            return
        #At this point we know that self.Canvas is not None, which means we have an
        #    label of ourself on that canvas. Bind <ButtonPress> to that label so the
        #    the user can pick us up again if and when desired.            
        self.Label.bind('<ButtonPress>',self.Press)
        #If self.OriginalCanvas exists then we were an existing object and our
        #    original label is still around although hidden. We no longer need
        #    it so we delete it.
        if self.OriginalCanvas:
            self.OriginalCanvas.delete(self.OriginalID)
            self.OriginalCanvas = None
            self.OriginalID = None
            self.OriginalLabel = None

    def Appear(self, Canvas, XY):
        """
        Put an label representing this Dragged instance on Canvas.
        
        XY says where the mouse pointer is. We don't, however, necessarily want
            to draw our upper left corner at XY. Why not? Because if the user
            pressed over an existing label AND the mouse wasn't exactly over the
            upper left of the label (which is pretty likely) then we would like
            to keep the mouse pointer at the same relative position inside the
            label. We therefore adjust X and Y by self.OffsetX and self.OffseY
            thus moving our upper left corner up and/or left by the specified
            amounts. These offsets are set to a nominal value when an instance
            of Dragged is created (where it matters rather less), and to a useful
            value by our "Press" routine when the user clicks on an existing
            instance of us.
        """
        if self.Canvas:
            #we are already on a canvas; do nothing
            return
        self.X, self.Y = XY    
        #Create a label which identifies us, including our unique number
        self.Label = Label(Canvas,text=self.Name,borderwidth=2, relief=RAISED)
        #Display the label on a window on the canvas. We need the ID returned by
        #    the canvas so we can move the label around as the mouse moves.
        self.ID = Canvas.create_window(self.X-self.OffsetX, self.Y-self.OffsetY, window=self.Label, anchor="nw")
        #Note the canvas on which we drew the label.
        self.Canvas = Canvas

    def Vanish(self,All=0):
        """
        If there is a label representing us on a canvas, make it go away.
        
        if self.Canvas is not None, that implies that "Appear" had prevously
            put a label representing us on the canvas and we delete it.
            
        if "All" is true then we check self.OriginalCanvas and if it not None
            we delete from it the label which represents us.
        """
        if self.Canvas:
            #we have a label on a canvas; delete it
            self.Canvas.delete(self.ID)
            #flag that we are not represented on the canvas
            self.Canvas = None
            #Since ID and Label are no longer meaningful, get rid of them lest they
            #confuse the situation later on. Not necessary, but tidy.
            del self.ID
            del self.Label
        
        if All and self.OriginalCanvas:
            #Delete label representing us from self.OriginalCanvas
            self.OriginalCanvas.delete(self.OriginalID)
            self.OriginalCanvas = None
            del self.OriginalID
            del self.OriginalLabel

    def Move(self,XY):
        """
        If we have a label a canvas, then move it to the specified location. 
        
        XY is with respect to the upper left corner of the canvas
        """    
        assert self.Canvas, "Can't move because we are not on a canvas"
        self.X, self.Y = XY
        self.Canvas.coords(self.ID,self.X-self.OffsetX,self.Y-self.OffsetY)

    def Press(self,Event):
        """
        User has clicked on a label representing us. Initiate drag and drop.
        There is a problem, er, opportunity here. In this case we would like to
            act as both the InitiationObject (because the user clicked on us
            and it't up to us to start the drag and drop) but we also want to
            act as the dragged object (because it's us the user wants to drag
            around). If we simply pass ourself to "Tkdnd" as the dragged object
            it won't work because the entire drag and drop process is moved
            along by <motion> events as a result of a binding by the widget
            on which the user clicked. That widget is the label which represents
            us and it get moved around by our "move" method. It also gets
            DELETED by our "vanish" method if the user moves it off the current
            canvas, which is a perfectly legal thing from them to do. If the
            widget which is driving the process gets deleted, the whole drag and
            drop grinds to a real quick halt. We use a little sleight of hand to
            get around this:
            1) From the label which is currently representing us (self.Label) 
               we take the text and save it in self.OriginalText. This will allow 
               us to resurrect the label at a later time if so desired. (It turns 
               out we so desire if the user tries to drop us in the middle of 
               nowhere, but that's a different story; see "dnd_end", above).
            2) We take the label which is currently representing us (self.Label)
               and we make it into an invisible phantom by setting its text to ''
               and settings its relief to FLAT. It is now, so to speak, a polar
               bear in a snowstorm. It's still there, but it blends in with the
               rest of then canvas on which it sits. 
            3) We move all the information about the phantom label (Canvas, ID
               and Label) into variables which store information about the 
               previous label (PreviousCanvas, PreviousID and PreviousLabel)
            4) We set self.Canvas and friends to None, which indicates that we 
               don't have a label representing us on the canvas. This is a bit
               of a lie (the phantom is technically on the canvas) but it does no
               harm.
            5) We call "self.Appear" which, noting that don't have a label
               representing us on the canvas, promptly draws one for us, which
               gets saved as self.Canvas etc.
            We went to all this trouble so that:
            a) The original widget on which the user clicked (now the phantom)
               could hang around driving the drag and drop until it is done, and
            b) The user has a label (the one just created by Appear) which they 
               can drag around, from canvas to canvas as desired, until they 
               drop it. THIS one can get deleted from the current canvas and
               redrawn on another canvas without Anything Bad happening.           
            From the users viewpoint the whole thing is seamless: they think
                the ARE dragging around the original label, but they are not. To 
                make it really clear what is happening, go to the top of the
                code and set "LeavePhantomVisible" to 1. Then when you drag an 
                existing object, you will see the phantom.
            The phantom is resolved by routine "dnd_end" above. If the user 
                drops us on a canvas, then we take up residence on the canvas and
                the phantom label, no longer needed, is deleted. If the user tries
                to drop us in the middle of nowhere, then there will be no
                'current' label for us (because we are in the middle of nowhere)
                and thus we resurrect the phantom label which in this case
                continues to represent us.    
            Note that this whole deal happens ONLY when the user clicks on an
                EXISTING instance of us. In the case where the user clicks over
                the button marked "InitiationObject" then it it that button that
                IS the initiation object, it creates a copy of us and the whole
                opportunity never happens, since the "InitiationObject" button 
                is never in any danger of being deleted.
        """
        Blab(1, "Dragged.press")
        #Save our current label as the Original label
        self.OriginalID = self.ID
        self.OriginalLabel = self.Label
        self.OriginalText = self.OriginalLabel['text']
        self.OriginalCanvas = self.Canvas
        #Made the phantom invisible (unless the user asked to see it)
        if LeavePhantomVisible:
            self.OriginalLabel['text'] = '<phantom>'
            self.OriginalLabel['relief']=RAISED
        else:
            self.OriginalLabel['text'] = ''
            self.OriginalLabel['relief']=FLAT
        #Say we have no current label    
        self.ID = None
        self.Canvas = None
        self.Label = None
        #Ask Tkdnd to start the drag operation
        if Tkdnd.dnd_start(self,Event):
            #Save where the mouse pointer was in the label so it stays in the
            #    same relative position as we drag it around
            self.OffsetX, self.OffsetY = MouseInWidget(self.OriginalLabel,Event)
            #Draw a label of ourself for the user to drag around
            XY = MouseInWidget(self.OriginalCanvas,Event)
            self.Appear(self.OriginalCanvas,XY)
    

def on_dnd_start(event=None):
    print(event)

def x():
    print("x")

app=gui()
for i in range(10):
    lab = app.addLabel("l"+str(i), "text here")
    lab.bind('<ButtonPress>',on_dnd_start)
    lab.x = types.MethodType(x, lab)
app.go()
