import sys
sys.path.append("../../")

from appJar import gui

def changetab(val):
    print(val, app.getPagedWindowPageNumber('tw'))
    print('previous', app.getPagedWindowPreviousPageNumber('tw'))
#    return False

with gui() as app:
    with app.pagedWindow('tw', change=changetab):
#        app.setPagedWindowChangeFunction('tw', changetab)
        for i in range(10):
            name = 't'+str(i)
            with app.page():
                app.label(name)
                app.button(name, changetab)

            
