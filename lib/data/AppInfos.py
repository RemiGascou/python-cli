# -*- coding: utf-8 -*-

def get_name() -> str:
    return "PyChat"

def get_version() -> str:
    return "v.0.8.1"

def get_credits() -> str:
    return "© Rémi GASCOU 2016-2018"

def get_helpmessage() -> str:
    helpmessage = """This is helpmessage :"""
    helpmessage += """\n    - help : Displays this message."""
    helpmessage += """\n    - ?    : Displays this message."""
    helpmessage += """\n    - exit : Exits the CLI."""
    return helpmessage

def get_motd() -> str:
    return """\n        ////////   //         ////////\n       //         //            //\n      //         //            //\n     //         //            //\n    ////////   ////////   ////////  """ + get_version() + """\n"""
