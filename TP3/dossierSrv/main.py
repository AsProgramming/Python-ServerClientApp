#!/usr/bin/env python3.5	
import os
from personne import *	
import sys

def main():

if(len(sys.argv) != 3):
	print("Usage: ex.py <fichier commande> <fichier sortie>", file=sys.stderr)
    sys.exit(1)

fichier = open(sys,argv[1], "r")
contenu = fichier.read().split("_")
print(contenu)



if __name__ == "__main__":
	main()