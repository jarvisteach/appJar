# import the library
from appJar import gui

def slide(scale):
      red = '%02x' % win.getScale("Red")
      green = '%02x' % win.getScale("Green")
      blue = '%02x' % win.getScale("Blue")

      rgb = '#' + red+green+blue

      win.setLabel ( 'code', rgb )
      win.setBg(rgb )

# create the GUI and start it
win = gui("Hexadecimal Colours")

win.setFont(16)

win.addScale("Red")
win.addScale("Green")
win.addScale("Blue")

win.setScaleRange("Red", 0, 255)
win.setScaleRange("Green", 0, 255)
win.setScaleRange("Blue", 0, 255)

win.showScaleValue("Red")
win.showScaleValue("Green")
win.showScaleValue("Blue")

win.setScaleFunction("Red", slide)
win.setScaleFunction("Green", slide)
win.setScaleFunction("Blue", slide)

win.addLabel('code', 'xxxxxx')

win.go()
