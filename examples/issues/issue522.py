import sys
sys.path.append("../../")

from appJar import gui

with gui('Pager Demo', '280x400', bg='darkkhaki') as app:


    with app.pagedWindow("Main Title", fg='red') as pw:
#    app.startPagedWindow("Main Title").config(fg='red')
#        pw.config(fg='red')
#        app.fg = 'black'
        with app.page(fg='black'):
            app.addLabel("l13", "Label 1")

        with app.page():
            app.addLabel("l21", "Label 2")

        with app.page():
            app.addLabel("l3", "Label 3")

        with app.page():
            app.addLabel("l4", "Label 4")

#        app.stopPagedWindow()
