import sys
sys.path.append("../../")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hs602util.py
#
#  Copyright 2017 Mark Clarkstone <git@markclarkstone.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import uuid
import gettext
import appJar
#import hs602

gettext.install('hs602util')


class app(appJar.gui):
    """HS602 utility app using appJar."""
    def __init__(self):
        # Init defaults and call main window.
        super().__init__(useTtk=True)
        self.useTtk()
        self.setTitle(self.lang('title'))
        self.main()

    def lang(self, key):
        """Returns string value associated with key or uuid4.

           :param key: Key to lookup.
        """
        strings = {
            'title': _('HS602 Utility'),
            'main_frame_title': _('Device Connection'),
            'main_addr_opt': _('Device: '),
            'main_cancel_btn': _('Cancel'),
            'main_disco_btn': _('Discover'),
            'main_addr_entry': _('IPv4'),
            'main_settings_frame_title': _('Connection Settings'),
            'main_settings_info': _('Leave blank to use defaults.'),
            'main_connect_btn': _('Connect'),
            'main_help_btn': _('About/Help'),
            'main_settings_udp': _('UDP port'),
            'main_settings_tcp': _('TCP port'),
            'main_settings_timeout': _('Timeout'),
            'main_discovering': _('Probing devices, please wait..'),
        }
        try:
            return str(strings[key])
        except KeyError:
            return str(uuid.uuid4())

    def main(self, devices=None):
        """This is the default window."""
        # Clear previous widgets (if any) & set some defaults.
        self.removeAllWidgets()
        self.setSticky('nesw')
        self.setPadding([2, 2])
        self.setBg("blue")

        # Begin a new frame & set some defaults (for inside the frame).
        self.startLabelFrame(self.lang('main_frame_title'))
        self.setPadding([2, 2])
        self.setStretch('both')
        self.setSticky('nesw')

        # Do we have a device list?
        try:
            #self.addLabelOptionBox(self.lang('main_addr_opt'), devices)
            self.addButton(self.lang('main_cancel_btn'),
                           self.main_btns, 0, 1)
        except TypeError:
            # No device list, just display entry & discovery button.
            self.addLabelEntry(self.lang('main_addr_entry'), 0, 0)
            self.addButton(self.lang('main_disco_btn'), self.main_btns,
                           0, 1)

        # Open a sub-label frame, set some defaults, then add widgets.
        self.startLabelFrame(self.lang('main_settings_frame_title'))
        self.setPadding([2, 2])
        self.setSticky('nes')
        self.addLabelNumericEntry(self.lang('main_settings_tcp'))
        self.addLabelNumericEntry(self.lang('main_settings_udp'))
        self.addLabelNumericEntry(self.lang('main_settings_timeout'))
        self.addLabel('main_connect_info',
                      self.lang('main_settings_info'))
        # End of _sub_ label frame.
        self.stopLabelFrame()

        self.addLabels(["a", "b", "c"])
        self.addGrip()
#        self.addWebLink("l1", "http://www.google.com")

        # Connect button.
        self.setSticky('nesw')
        self.setPadding([2, 2])
        self.addButton(self.lang('main_connect_btn'), self.main_btns,
                       1, 1)

        # End of _main_ label frame.
        self.stopLabelFrame()
        # About.
        self.addButton(self.lang('main_help_btn'), self.main_btns)

    def main_btns(self, btn=None):
        """Main button action.

           :param btn: Button used to trigger this method.
        """
        def get_values():
            """Returns required input values."""
            # Required values.
            values = {
                'addr': {
                    'name': self.lang('main_addr_entry'),
                    'default': None,
                },
                'tcp': {
                    'name': self.lang('main_settings_tcp'),
                    'default': 8087,
                },
                'udp': {
                    'name': self.lang('main_settings_udp'),
                    'default': 8086,
                },
                'timeout': {
                    'name': self.lang('main_settings_timeout'),
                    'default': 5,
                },
            }
            entries = self.getAllEntries()
            # Tack the optionbox value onto entries if set, This
            # won't be needed with appJar 0.08.
            try:
                option_name = self.lang('main_addr_opt')
                option_value = self.getOptionBox(option_name)
                entries[self.lang('main_addr_entry')] = option_value
            except appJar.appjar.ItemLookupError:
                pass
            # Here we're going through each of the required values,
            # updating the dictionary with _just_ the user-entered
            # value (from entries), or using the default - if not set.
            for key in values:
                name, value = [
                    values[key]['name'],
                    values[key]['default'], 
                ]
                user_value = entries[name]
                if not user_value:
                    user_value = value
                # Convert float to int.
                if isinstance(user_value, float):
                    user_value = int(user_value)
                # Update dictionary.
                values[key] = user_value
            return values

        values = get_values()
        # Discovery.
        if btn == self.lang('main_disco_btn'):
            # Clear all widgets and let the user know discovery is in
            # progress.
            self.removeAllWidgets()
            self.setSticky('nesw')
            self.addLabel('main_discovering', 
                          self.lang('main_discovering'), 0)
            return self.after(100, self.main_discovery(**values))
        # Connect.
        if btn == self.lang('main_connect_btn'):
            return self.main_connect(**values)
        # Cancel.
        if btn == self.lang('main_cancel_btn'):
            return self.main()
            
    def main_discovery(self, **kwargs):
        """Starts the discovery of devices."""
        # Remove addr & make sure that the rest aren't zero.
        # Zero values should not happen, but better to check anyway.
        kwargs.pop('addr')
        udp = int(kwargs.get('udp', 0))
        tcp = int(kwargs.get('tcp', 0))
        timeout = int(kwargs.get('timeout', 0))
        if 0 in [udp, tcp, timeout]:
            raise ValueError
        devices_found = hs602.Controller(**kwargs).discover()
        return self.main(devices_found)


    def main_connect(self, **kwargs):
        print(kwargs)

def main(args):
    application = app()
    application.go()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
