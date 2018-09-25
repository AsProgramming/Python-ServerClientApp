#! /usr/bin/python3
#  -*-coding:Utf-8 -*

import os

tube = os.pipe()
ecrivain = os.fdopen(tube[1], 'w')
lecteur = os.fdopen(tube[0])

print("Message qui passe par un tube.", file=ecrivain, end="")
ecrivain.close()


ligne = lecteur.readline()
lecteur.close()

print (ligne)
 



