#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys


if len(sys.argv) < 2:
    print("Usage: exercice3.py <programme> [arguments] [...]", file=sys.stderr)
    sys.exit(1)

arguments = sys.argv[1:]

os.system("touch text.txt")
fichier = open("text.txt", "w")

tube = os.pipe()
pid = os.fork()


if pid == 0:
    os.close(tube[0])
    os.dup2(tube[1], 2)
    os.execvp(sys.argv[1], arguments)

elif pid > 0:
	os.close(tube[1])
	lecture = os.fdopen(tube[0])
	(pid, status) = os.wait()
	if status != 0:
		erreur = lecture.read()
		fichier.write("Erreur: {0} \nhfvbjef".format(erreur))
		print("")

else:
    print("Impossible de créer le processus", file=sys.stderr)
    system.exit(1)

