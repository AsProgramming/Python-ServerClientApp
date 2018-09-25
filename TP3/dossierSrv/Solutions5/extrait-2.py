#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys

tube = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(tube[0])
    ecrivain = os.fdopen(tube[1], 'w')
    message = input("Entrez votre message: ")
    print(message, file=ecrivain, end="")
    ecrivain.close()
    sys.exit(0)

elif pid > 0:
    os.close(tube[1])
    lecteur = os.fdopen(tube[0])
    ligne = lecteur.read()
    print("Voici le message de mon fils: {0}".format(ligne))
    lecteur.close()
    os.wait()

else:
    print("Impossible de créer le processus", file=sys.stderr)
    sys.exit(1)


