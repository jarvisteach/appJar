import sys
sys.path.append("../../")

from appJar import gui

def s3(): pass
def t4(): pass

with gui() as app:
    with app.tabbedFrame('tp'):
        with app.tab('tab1'):
            app.label('hello world', row=0, column=0)
            app.label('hello world2', row=0, column=1)
            app.label('hello world3', row=0, column=2)
            app.label('hello world4', row=0, column=3)
            app.text('text', scroll=True, colspan=4)

        with app.tab("HW", sticky="news"):
            app.sticky = 'news'
            with app.labelFrame("HW Feedback", sticky='news'):
                app.label("foo4", "Feedback:", row=0, column=0, colspan=1, rowspan=1, bg='red')
                app.addScrolledTextArea("lb4", row=1, column=0, colspan=1, rowspan=1)
                app.addHorizontalSeparator(row=31, column=0, colspan=1, rowspan=1)
                app.separator(row=31, column=0, colspan=1, sticky='news')
                app.buttons(["Run","Retest","Quit HW"], s3, row=32, column=0)
                app.buttons(["To Results"], t4, row=33, column=0) # End with-statement # End with-statement
