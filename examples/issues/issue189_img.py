import sys
sys.path.append("../../")
from appJar import gui

with gui(useTtk=False) as app:
#    app.addImageButton("button2", None, "Capture 2.PNG", align=None) # Uncomment this
    app.addIconButton("button", None, "md-play", align="none") # Or this
