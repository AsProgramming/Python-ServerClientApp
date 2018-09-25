#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys

tube = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(tube[1])
    os.dup2(tube[0], 0)
    os.execl("./perroquet.py", "perroquet.py")
elif pid > 0:
    os.close(tube[0])
    ecriture = os.fdopen(tube[1], 'w')
    print("Bonjour", file=ecriture)
    ecriture.close()
    os.wait()
else:
    print("Impossible de créer le processus", file=sys.stderr)
    system.exit(1)
