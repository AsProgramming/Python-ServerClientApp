#!/usr/bin/env python3.5
#  -*-coding:Utf-8 -*
'''					TP3					
	Simple client FTP qui permet de telecharger 
	des fichiers du serveur ainsi qu'enregistrer
	des fichiers au besoin sur le serveur
			Programmeur: Edwin Andino			'''

import sys, socket, threading, os
from liaison import *

def main():

	ip, port = verificationInit(sys.argv);
	HOST = ip
	PORT = port
	client = socket.socket()

	client.connect((HOST, PORT))
	l = Liaison(client)
	os.system('clear')
	print('	Bienvenue \n   au serveur BdB-TP3')
	while True:
		entrer = input('%> ')
		message = entrer.split(' ')
		taille = len(message)
		'''Si l'utilisateur ecrit quitter on termine '''
		if message[0] == 'quitter':
			client.close()
			break
		'''On telecharge le fichier si present '''
		if message[0] == 'get' and taille == 2:
			client.send(str.encode(entrer))
			l.recevoirDonnees(message[1], 1)
		'''On upload au serveur le fichier si present '''			
		if message[0] == 'put' and taille == 2:
			chemin = './' + message[1]
			valider = verifierFichier(chemin)
			if valider:
				client.send(str.encode(entrer))
				reponse = client.recv(1024).decode('UTF-8')
				l.envoyerDonnees(chemin, 1)
			else:
				print('Fichier inexistant')
		'''On affiche les fichiers du serveur '''		
		if message[0] == 'liste' and taille == 1:
			client.send(str.encode(entrer))
			info = client.recv(10240).decode('UTF-8')
			afficher(info)
	print("Deconnection...")
	client.close()

'''Methode qui verifie si le IP et le PORT sont entrer des le debut
	@rgs les arguments de la ligne de commande'''
def verificationInit(args):
	if len(args) != 3:
		print("Usage: client_serveur.py <IP> <PORT>", file=sys.stderr)
		sys.exit(1)
	else:
		port = int(args[2])
		return args[1], port

'''Methode qui verifie si le fichier existe ou non
	@rgs le nom du fichier recu'''
def verifierFichier(nom):
	if os.path.isfile(nom):
		return True
	else:
		return False

'''Methode qui affiche les infos recu du serveur
	@rgs les infos recues '''
def afficher(info):
	liste = info.split(' ')
	for i in range(len(liste)):
		if i == len(liste) - 1:
			print(liste[i], end='', flush=True)
		elif liste[i] != '':
			print(liste[i])

if __name__ == "__main__":
	main()