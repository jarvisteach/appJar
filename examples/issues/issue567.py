import imp, sys
keys = imp.load_source('keys', 'issue567.keys')
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.map('a', mapKey=keys.MAP_KEY)
    app.setGoogleMapKey('a', keys.MAP_KEY)
    app.setGoogleMapLocationKey('a', ipinfo=keys.IP_INFO)
