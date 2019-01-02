# -*- coding: utf-8 -*-

from lib import *

class CLI(object):
    """docstring for CLI."""
    def __init__(self):
        super(CLI, self).__init__()
        self.cm   = CommandManager(self)
        self.motd = AppInfos.get_motd()
        
    def cliprint(self, s, sep=" ", end="\n"):
        print("\r"+s, sep=sep, end=end)
        print("> ", end="")

    def start(self):
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
