setBg:
    All widgets created with:
        .config(background=self.__getContainerBg()
    But
        .__positionWidget()
            Calls __setWidgetBg() using .__getContainerBg()

    .setBg(colour)
        Calls .config(background=colour)
        Then loops through .winfo_children()
        And if not __widgetIsContainer() calls __setWidgetBg()

    .set XXX Bg(colour)
        If METER calls setBg
        If TABBEDFRAME calls setBg
        Else calls __setWidgetBg()
    --------------
    .__widgetIsContainer() - checks the isContainer field
    .__setWidgetBg() - the big one!
        Checks widget type, then calls appropriate setters





tabbedFrame rethink:
BGs:
* Container - only visible at end of tab bar
* Tabs - active/inactive
* Panes - each one

Therefore:
* Make tabs/Panes match colour!
* have active/inactive writing colour
* container BG


activeforeground
activebackground

bg
fg

disabledforeground
disabledbackground
