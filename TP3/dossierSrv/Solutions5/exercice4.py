#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys


if len(sys.argv) < 2:
    print("Usage: exercice4.py <programme> [arguments] [...]", file=sys.stderr)
    sys.exit(1)

arguments = sys.argv[1:]

tube = os.pipe()
pid = os.fork()


if pid == 0:
    os.close(tube[0])
    os.dup2(tube[1], 1)
    os.execvp(sys.argv[1], arguments)

elif pid > 0:
    os.close(tube[1])
    lecture = os.fdopen(tube[0])
    nombreLignes = 0
    os.wait()        
    for ligne in lecture:
        nombreLignes = nombreLignes = nombreLignes + 1
    print ("Le programme aurait affiché {0} ligne(s).".format(nombreLignes))

else:
    print("Impossible de créer le processus", file=sys.stderr)
    system.exit(1)

