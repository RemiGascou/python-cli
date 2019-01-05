# -*- coding: utf-8 -*-

from lib.data import AppInfos

class CommandManager(object):
    """docstring for CommandManager."""
    def __init__(self, parentcli):
        super(CommandManager, self).__init__()
        self.parentcli   = parentcli
        self.commands    = ["help", "?", "exit"]
        self.helpmessage = AppInfos.get_helpmessage()

    def isCommand(self, inputcommand):
        command = inputcommand.split(" ")[0]
        if command in self.commands:
            return True
        else:
            return False

    def process(self, command):
        command = command.lower()
        if command == "help" or command == "?":
            self.cmd_help()
        elif command == "?":
            self.cmd_help()

    # -------------------------------COMMANDS----------------------------------#

    def cmd_help(self):
        self.parentcli.cliprint(self.helpmessage)


    # -------------------------------GET  SET----------------------------------#

    def get_commands(self):
        return self.commands
