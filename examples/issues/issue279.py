#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gui.py
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
import sys
sys.path.append("../../")
import gettext
import uuid
import traceback
import appJar
#import hs602

# Setup gettext.
gettext.install('Hs602util')


class Gui(appJar.gui):
    """Simple HS602 utility using appJar."""
    def __init__(self):
        super().__init__()

        # Some defaults.
        # Window title.
        self.setTitle(self.lang('default_title'))
        # Default widget padding.
        self.padx = 5
        self.pady = 5
        # Widget sticky setting.
        self.sticky = 'nesw'

        # The default window.
        self.manual_win()

    def lang(self, key):
        """Return string value of the requested key in values.

        :param key: key of the value you want.
        """
        value = None
        values = {
            'default_title': _('HS602 Utility'),
            'error_title': _('Something Went Wrong!'),
            'error_msg': _('Sorry, there\'s a problem. If it continues '
                           'please report it.'),
            'error_retry': _('\u2753 Try again'),
            'error_quit': _('\u274C Quit'),
            'scan_info': _('\u231B Scanning, please wait..'),
            'scan_failed_title': _('No Devices Found!'),
            'scan_failed_msg': _('No devices found!\nTry with an '
                                 'increased timeout (Yes)? Or connect '
                                 'manually (No)?'),
            'manual_title': _('HS602 Utility - Connect'),
            'manual_frm': _('Connect to Device'),
            'manual_info': _('The address is required, leave the rest '
                             'blank to use defaults.'),
            'manual_addr': _('Address'),
            'manual_tcp_lbl': _('TCP port'),
            'manual_udp_lbl': _('UDP port'),
            'manual_timeout_lbl': _('Timeout (in seconds)'),
            'manual_scan_again': _('\u2753 Scan'),
            'manual_connect': _('\u2713 Connect'),
            'device_addr_invalid': _('Address must be set!'),
        }
        try:
            value = values[key]
        except KeyError:
            pass
        return str(value or uuid.uuid4())

    def widget_defaults(self, inside_padding=False):
        """Set widget defaults.

        :param inside_padding: Set the padding inside the widget.
        """
        # Padding.
        func = self.setPadding
        if inside_padding:
            func = self.setInPadding
        func(self.padx, self.pady)
        # Sticky.
        self.setSticky(self.sticky)

    def error_win(self, exc, callback=None):
        """There was a problem, display the traceback.

        :param exc: Exception or error message.
        :param callback: Function to call if the user would like
        to try again.
        """
        # Window settings.
        self.removeAllWidgets()
        self.widget_defaults()

        # Widgets.
        self.addLabel('error_msg', self.lang('error_msg'))

        # If possible, get the backtrace.
        backtrace = ''
        try:
            backtrace = ''.join(traceback.format_tb(exc.__traceback__))
        except AttributeError:
            pass

        # Add a text area so the user can copy the error.
        self.addScrolledTextArea('backtrace')
        self.setTextArea('backtrace', "{}\n\n{}".format(exc, backtrace))

        if callable(callback):
            self.addButton(self.lang('error_retry'),
                           callback)
        else:
            self.addButton(self.lang('error_quit'),
                           self.stop)

    def scan_win(self, btn=None, timeout=5):
        """The scan window.

        :param: Button that triggered this method.
        :param: Timeout to pass to the scan thread.
        """
        # Window settings.
        self.removeAllWidgets()
        self.widget_defaults()
        self.addLabel('scan_info', self.lang('scan_info'))
        # Queue the scan!
        self.after(100, self.thread, self.scan_thread, timeout)

    def scan_thread(self, timeout=5):
        """The scan thread - must be ran in the background.

           :param timeout: The socket timeout (in seconds 5-120).
        """
        # Make sure the timeout is sane.
        try:
            timeout = int(timeout)
            if timeout not in range(4, 121):
                timeout = 5
        except ValueError:
            timeout = 5
        # OK try to probe!
        try:
            devices = hs602.Controller(timeout=timeout).discover()
        except OSError as exc:
            return self.queueFunction(self.error_win, exc)

        self.queueFunction(self.scan_finished_win, devices)

    def scan_again_win(self):
        """Ask the user to scan again or connect manually.

        This will in future allow the user to enter a timeout.
        """
        prompt = self.questionBox(self.lang('scan_failed_title'),
                                  self.lang('scan_failed_msg'))
        if prompt == 'yes':
            return self.scan_win(None, 60)
        self.manual_win()

    def scan_finished_win(self, devices):
        """The scan has finished, ask the user to select a device -
        usually called by scan_thread.

        :param devices: list of devices found.
        """
        if not isinstance(devices, list) or not len(devices) > 0:
            return self.scan_again_win()
        self.scan_again_win()

    def manual_win(self, btn=None):
        """Display manual connection form.

        :param btn: The button that called this method (not used).
        """
        # Window settings.
        self.removeAllWidgets()
        self.widget_defaults()

        def connect(btn=None):
            """Connect button method.
            This basically calls device_connect with the form
            values as keyword args.

            :param btn: Button that called the method (not used).
            """
            values = self.getAllEntries()
            self.queueFunction(self.device_connect, **values)

        # Connection input frame - this is before the above buttons.
        with self.labelFrame(self.lang('manual_frm'), 0, 0, 2):
            self.widget_defaults()

            # Frame widgets.
            self.addEntry('addr', 0, 1)
            self.addNumericEntry('tcp', 1, 1)
            self.addNumericEntry('timeout', 2, 1)

            self.addLabel('addr_lbl', self.lang('manual_addr'), 0, 0, 1)
            self.addLabel('tcp_lbl', self.lang('manual_tcp_lbl'), 1, 0)
            self.addLabel('to_lbl',  self.lang('manual_timeout_lbl'), 2, 0)
            self.addLabel('info_lbl', self.lang('manual_info'), 3, 0, 2)


            self.setEntryMaxLength('tcp', 5)
            self.setEntryMaxLength('timeout', 3)
            self.setLabelAlign('info_lbl', 'center')
            self.setLabelAlign('addr_lbl', 'center')
            self.setLabelAlign('tcp_lbl', 'center')
            self.setLabelAlign('to_lbl', 'center')

        # Widgets.
        self.addButton(self.lang('manual_scan_again'),
                       self.scan_win, 1, 0)
        self.addButton(self.lang('manual_connect'), connect, 1, 1)
        self.resize()


    def device_connect(self, **kwargs):
        """Try to connect using the values provided - this must be
        called in the background.

        :param kwargs: Connection info list - addr is required.
        """
        # Check addr, port and timeout.
        try:
            kwargs['tcp'] = int(kwargs.get('tcp') or -1)
            kwargs['timeout'] = int(kwargs.get('timeout') or 0)
            kwargs['addr'] = str(kwargs.get('addr') or '').strip()

            # Port and timeout
            if not kwargs['tcp'] >= 1:
                kwargs.pop('tcp')
            if not kwargs['timeout'] > 0:
                kwargs.pop('timeout')

            if not len(kwargs['addr']) > 0:
                raise ValueError(self.lang('device_addr_invalid'))
        except ValueError as exc:
            return self.queueFunction(self.error_win, exc,
                                      self.manual_win)

        print(kwargs)


def main(args):
    app = Gui()
    app.go()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
