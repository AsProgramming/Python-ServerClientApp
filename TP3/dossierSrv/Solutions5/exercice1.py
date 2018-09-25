#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys

if len(sys.argv) != 3:
    print("Usage: ./exercice1.py <nom> <age>", file=sys.stderr)
    sys.exit(1)


tube = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(tube[1])
    lecture = os.fdopen(tube[0])
    ligne = lecture.read()
    print(ligne)
    lecture.close()
    sys.exit(0)
elif pid > 0:
    os.close(tube[0])
    ecriture = os.fdopen(tube[1], 'w')
    message = "Bonjour {0} !!, vous avez {1} ans.".format(sys.argv[1], sys.argv[2])
    print(message, file=ecriture, end="")
    ecriture.close()
    os.wait()
else:
    print("Impossible de créer le processus", file=sys.stderr)
    system.exit(1)
