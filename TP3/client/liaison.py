'''					TP3					
	Simple classe qui enleve la duplication
	de code dans le serveur ainsi que dans le client
			Programmeur: Edwin Andino			'''
import os
class Liaison:
	def __init__(self, c):
		self.connection = c
	'''Methode qui envoi les informations au destinataire
		@rgs le chemin du fichier envoyer
		@rgs l'indice pour afficher ou non a l'ecran'''
	def envoyerDonnees(self, chemin, indice):
		if os.path.isfile(chemin):
			info = str(os.path.getsize(chemin)).encode()
			self.connection.send(info)
			reponse = self.connection.recv(1024).decode('UTF-8')
			if reponse == 'O' or reponse == 'o':
				with open(chemin, 'rb') as f:
					fichierVoulu = f.read(1024)
					self.connection.send(fichierVoulu)
					while fichierVoulu:
						fichierVoulu = f.read(1024)
						self.connection.send(fichierVoulu)
					f.close()
					if indice == 1:
						print('Televersement reussi!')
		else:
			invalide = 'ERR'
			self.connection.send(str.encode(invalide))
	'''Methode qui recoi les informations envoyer
		@rgs le nom du fichier recu
		@rgs l'indice pour afficher ou non a l'ecran'''
	def recevoirDonnees(self, nomFichier, indice):
		data = self.connection.recv(1024).decode('UTF-8')
		if data != 'ERR':
			data = int(data)
			fich = open(nomFichier, 'wb')
			self.connection.send(str.encode('O'))
			portion = self.connection.recv(1024)
			total = len(portion)
			fich.write(portion)
			debut = 0
			while total < data:
				portion = self.connection.recv(1024)
				total += len(portion)
				fich.write(portion)
				affichage = int((total/data)*100)
				if affichage >= debut or affichage < debut and debut <= 100:
					if indice == 1:
						print('{}% '.format(debut), end='')
						debut += 5
			fich.close()	
			if indice == 1:
				print('\nSauvegarde du fichier...terminee!')	
		elif indice == 1:
			print('Fichier inexistant')