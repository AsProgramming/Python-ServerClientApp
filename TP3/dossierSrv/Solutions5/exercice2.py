#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os
import sys
import io

tube = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(tube[1])
    lecture = os.fdopen(tube[0], "r")
    termine = False
    while not termine:
        message = lecture.readline()
        if len(message) > 0:
            print ("Message entré: {0}".format(message), end="")
        else:
            termine = True

    lecture.close()
    sys.exit(0)
            
elif pid > 0:
    os.close(tube[0])
    nombre_message = 0
    termine = False
    ecriture = os.fdopen(tube[1], 'w')
    while not termine:
        message = input("Entrez votre message: ")
        if len(message) > 0:
            print(message, file=ecriture)
            ecriture.flush()
            nombre_message += 1
        else:
            termine = True
    ecriture.close()
    os.wait()
    print ("Je suis le père... {0:d} messages ont été entrés".format(nombre_message))

else:
    print("Impossible de créer le processus", file=sys.stderr)
    system.exit(1)

