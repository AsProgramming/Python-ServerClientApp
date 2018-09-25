#!/usr/bin/env python3.5
#  -*-coding:Utf-8 -*
'''					TP3					
	Simple serveur FTP qui permet d'envoyer 
	des fichiers a des clients ainsi qu'enregistrer
	des fichiers au besoin des clients 
			Programmeur: Edwin Andino			'''

import socket, threading, os, sys
from liaison import *
def main():

	dossier, port = verificationInit(sys.argv);

	s = creer(port)

	while True:
		ip, conn = s.accept()
		connections = threading.Thread(target=gererConnection, args=(ip, conn, dossier))
		connections.daemon = True
		connections.start()

'''Methode qui initialise le serveur
	@arg le port entrer par le user '''
def creer(port):
	HOST = '0.0.0.0'
	PORT = port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.bind((HOST, PORT))
	s.listen(5)
	os.system('clear')
	return s

'''Methode qui permet de gerer les demandent des clients
	@arg le dossier entrer par le user '''
def gererConnection(connection, ip, dossierServeur):#a modfier
	t = Liaison(connection)
	while True:
		data = connection.recv(1024).decode('UTF-8')
		ligne = data.split(" ")
		cmd = ligne[0]
		if cmd == 'get':
			chemin = dossierServeur + '/' + ligne[1]
			t.envoyerDonnees(chemin, 2)
		elif cmd == 'put':
			connection.send(str.encode('O'))
			t.recevoirDonnees(ligne[1], 2)
			os.rename("./"+ligne[1], "./"+dossierServeur+'/'+ligne[1])
		elif cmd == 'liste':
			afficherDossier(connection, dossierServeur)
		elif cmd == 'quitter' or not cmd:
			connection.close()
			break

'''Methode qui envoi au client les fichiers present
	@arg la connection
	@arg le dossier du serveur'''
def afficherDossier(connection, dossierServeur):
	liste = ' '
	fichiers = os.listdir(dossierServeur)
	for f in fichiers:
		chemin = dossierServeur + '/' + f
		if os.path.isfile(chemin):
			liste += f + ' '
	connection.send(str.encode(liste))

'''Methode qui verifie les arguments passer en ligne de commande
	@arg les arguments entrer par le user '''
def verificationInit(args):
	if len(args) != 3:
		print("Usage: ftp_serveur.py <Dossier> <PORT>", file=sys.stderr)
		sys.exit(1)
	else:
		fich = verifierDossier(args[1])
		if fich == "":
			print("Dossier inexistant!", file=sys.stderr)
			sys.exit(1)
		else:
			port = int(args[2])
			return fich, port
'''Methode qui verifie si le dossier entrer est valide
	@arg le dossier entrer par le user '''
def verifierDossier(chemin):
	if os.path.isdir(chemin):
		return chemin
	else:
		return ""

if __name__ == "__main__":
	main()