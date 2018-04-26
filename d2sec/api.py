#!/usr/bin/env python3
# Part of vFeed Professional Services

import sys
import requests
import subprocess

from .conf import D2SEC_PATH, VERSION


class api(object):
    def __init__(self):
        """ init """

        try:
            self.session = requests.Session()
            self.req = self.session.get('http://127.0.0.1:8080/')
        except:
            print("You need to start the plugin with start()")

        self.cmd = str.join('', (D2SEC_PATH, "elliot_start.py"))

    def test(self):
        print("Checking plugin:", __name__, __file__)
        print("Version:", VERSION)

    def start(self):
        """start the framework """

        try:
            subprocess.Popen(['python3', self.cmd])
        except Exception as e:
            sys.exit("Error", str(e))

    def version(self):
        """chec the API version"""

        self.req = requests.get('http://127.0.0.1:8080/api/control/status')
        return self.req.text

    def get_exploits(self):
        """retrieve lisf of available exploits"""

        self.req = self.session.get('http://127.0.0.1:8080/api/exploits/')
        return self.req.text

    def get_sessions(self):
        """retrieve the sessions"""

        self.req = self.session.get('http://127.0.0.1:8080/api/sessions')
        return self.req.text

    def set_target(self, target):
        """Set the target and return the list"""

        data = '{"url":target}'
        headers = {'Content-type': 'application/json'}

        self.req = self.session.post('http://127.0.0.1:8080/api/kb/websites/new', data=data, headers=headers)
        self.req = self.session.get("http://127.0.0.1:8080/api/kb/websites/")

        return self.req.text
