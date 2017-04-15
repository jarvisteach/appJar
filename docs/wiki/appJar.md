{{lowercase|title=appJar}}
{{Infobox software
| logo                   = 
| screenshot             = 
| caption                = appJar
| developer              = Richard Jarvis
| released               = {{Start date and age|2015|df=yes}}<ref name=1streleased>{{cite web|title=First released|url=https://github.com/jarvisteach/appJar/commit/6cde09000b1cf0164234ecfe9faa2d6e49f4b491|accessdate=2017-04-08}}</ref>
| latest release version = 0.052
| latest release date    = {{Start date and age|2017|03|12}}
| operating system       = [[Cross-platform]]
| programming language   = [[Python (programming language)|Python]]
| genre                  =
| status                 = Active
| license                = [[GPL License]]
| website                = {{URL|http://appJar.info/}}
}}
'''appJar''' is a cross-platform, open source [[Python (programming language)|Python]] library for developing GUIs (graphical user interfaces).<ref>{{cite web|title=GUI programming in Python|url=https://wiki.python.org/moin/GuiProgramming|accessdate=2017-04-09}}</ref> It can run on [[Linux]], [[OS X]], and [[Microsoft Windows|Windows]]. It was conceived, and continues to be developed with educational use as its focus,<ref>{{cite web|title=Educational intentions|url=http://appjar.info|accessdate=2017-04-09}}</ref> so is accompanied by comprehensive documentation, as well as easy-to-follow lessons.<ref>{{cite web|title=Lessons|url=http://appjar.info/pythonLessons/|accessdate=2017-04-09}}</ref>

==License==
appJar is licensed under the GNU General Public License v3.0,<ref>{{cite web|title=Copyright notice|url=https://github.com/jarvisteach/appJar/blob/appJar/LICENSE.txt|accessdate=2017-04-09}}</ref> as approved by the [[Free Software Foundation]].

==History==
appJar was originally envisaged as a simple wrapper around tkinter, to allow secondary school pupils to develop simple graphical user interfaces in Python. It was meant to hide away the complexity, so that pupils could focus on writing algorithms, without having to worry about how to position widgets and link to functions. It was started out in the winter of 2014, as a simple in-house project, but soon started to grow. It was published to GitHub on July 31, 2015,<ref name=1streleased /> and first added to the PyPi repository on 20 December 2016.<ref>{{cite web|title=PyPi created|url=https://pypi.python.org/pypi/appJar/0.01|accessdate=2017-04-08}}</ref>

==Example==
This is a simple "[[Hello world program|Hello world]]" example:

<source lang="python">
#!/usr/bin/env python
from appJar import gui

app = gui("Demo")
app.addLabel("l1", "Hello World")
app.go()
</source>

==References==
;Notes
{{Reflist}}

==External links==
* {{Official website|http://appJar.info/}}
* {{GitHub|https://github.com/jarvisteach/appJar}}
* [https://pypi.python.org/pypi/appJar/ PyPi]

[[Category:Python libraries]]
[[Category:Widget toolkits]]
