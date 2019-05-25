import sys
sys.path.append("../../")

from appJar import gui

with gui('separators', '400x100') as app:
    with app.labelFrame("Test Results"):
#        app.sticky = 'news'
        app.separator(row=0, column=0, colspan=19, sticky='news')
#        app.separator(direction='vertical', row=1, column=1, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=3, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=5, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=6, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=9, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=11, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=13, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=15, colspan=1, rowspan=4)
#        app.addVerticalSeparator(row=1, column=17, colspan=1, rowspan=4)
