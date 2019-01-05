# -*- coding: utf-8 -*-

from lib.core.CommandManager import *
from lib.core.Completer import *
from lib.data import AppInfos

import os, readline

class CLI(object):
    """docstring for CLI."""
    def __init__(self):
        super(CLI, self).__init__()
        self.cm         = CommandManager(self)
        self.completer  = Completer(self.cm)
        self.motd       = AppInfos.get_motd()

    def cliprint(self, s, sep=" ", end="\n"):
        print("\r"+s, sep=sep, end=end)
        print("> ", end="")

    def start(self):
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer.complete)
        print(self.motd)
        print("> ", end="")
        self.running = True
        while self.running:
            inc = input("")
            if inc == "exit":
                self.running = False
            elif self.cm.isCommand(inc):
                self.cm.process(inc)
            else:
                self.cliprint("Unknown command")
