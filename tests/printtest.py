# -*- coding: utf-8 -*-

def println(s, sep=" ", end="\n"):
    print("\r"+s, sep=sep, end=end)
    print("> ", end="")

print("> ", end="")
running = True
while running:
    inc = input("")
    if inc == "exit":
        running = False
    else:
        println("Unknown command")
