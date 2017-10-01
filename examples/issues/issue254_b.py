import sys
sys.path.append("../../")
import uuid
import gettext
import appJar
#import hs602

class app(appJar.gui):
    """HS602 utility app using appJar."""
    def __init__(self):
        # Init defaults and call main window.
        super().__init__(useTtk=True)
        self.useTtk()
        self.setTtkTheme('clam')
        self.setTitle('foo')
        self.main()
        
    def lang(self, foo):
        return 'foo'
        
    def main(self):
        self.startLabelFrame('Fooframe')
        self.addLabelNumericEntry(self.lang('foo'), None)
        self.addLink("Click me", self.lang)
        self.addSeparator()
        self.addWebLink("Click me 2", "http://www.yahoo.com")
        self.addLabels(["a", "b", "c"])
        self.addButton('foo_button', None, 0, 1)
        self.stopLabelFrame()

def main(args):
    myapp = app()
    myapp.go()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
