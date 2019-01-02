# -*- coding: utf-8 -*-

class CommandManager(object):
    """docstring for CommandManager."""
    def __init__(self, parentcli):
        super(CommandManager, self).__init__()
        self.parentcli   = parentcli
        self.commands    = ["help", "exit"]
        self.helpmessage = """This is helpmessage :\n    - help : Displays this message.\n    - exit : Exits the CLI."""

    def cmd_help(self):
        self.parentcli.cliprint(self.helpmessage)

    def isCommand(self, inputcommand):
        command = inputcommand.split(" ")[0]
        if command in self.commands:
            return True
        else:
            return False

    def process(self, command):
        if command == "help":
            self.cmd_help()
