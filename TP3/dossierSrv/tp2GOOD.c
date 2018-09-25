#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define DONNEES "etudiants.dba"
#define VIDER system("clear")
#define LEMENU "\t     Menu\nAjouter un etudiant..........1\nAfficher un etudiant par DA..2\nAfficher tous les etudiants..3\nQuitter......................4\nEntrez votre choix..........."
#define MENU_AJOUT "\tAjout d'etudiant\nEntrez le DA de l'etudiant: "
#define MENU_PRENOM "\nEntrez le prenom de l'etudiant: "
#define MENU_NOM "\nEntrez le nom de l'etudiant: "
#define MENU_AGE "\nEntrez l'age de l'etudiant: "
#define ERREUR "Le fichier est vide"
#define ERREUR_CHOIX "\n\tChoix incorrect\nVeuillez faire un choix entre 1 et 4\n"
#define LIGNEMAX 55
#define DA_MAX 9
#define MAX_P 21
#define MAX_N 31
#define MAX_A 4

struct Etudiants{
	int DA;
	char prenom[MAX_P];
	char nom[MAX_N];
	int age;
	struct Etudiants *suivant;
};
struct Etudiants *premier = NULL;

struct Etudiants* nouveau(int leDA, char lePrenom[], char leNom[], int lAge) {
	struct Etudiants *ptr;
	ptr=(struct Etudiants*)malloc(sizeof(struct Etudiants));
	if (ptr == NULL)
		exit(0);
	ptr->DA = leDA;
	strcpy(ptr->prenom, lePrenom);
	strcpy(ptr->nom, leNom);
	ptr->age = lAge;
	ptr->suivant = NULL;
	return ptr;
}

void ajoutEnTete(int leDA, char lePrenom[], char leNom[], int lAge) {
	struct Etudiants *courant;
	courant = nouveau(leDA, lePrenom, leNom, lAge);
	if (premier == NULL) 
		premier = courant;
	else {
		courant->suivant=premier;
		premier=courant;
	}	
}

void afficheListe() {
	struct Etudiants *ptr = premier;
	if(ptr!=NULL){
		while(ptr != NULL) {
		printf("%d %s %s %d\n",ptr->DA, ptr->prenom, ptr->nom, ptr->age);
		ptr = ptr->suivant;
		}
	}else{
		printf("Il n'y a pas d'etudiant\n");
	}

}

void libererListe() {
	struct Etudiants *ptr = premier;
	struct Etudiants *tmp;
	printf("\nLiberer la liste en memoire:\n");
	while(ptr != NULL) {
		tmp = ptr;
		ptr = ptr->suivant;
		free(tmp);
	}
	premier = NULL;
}

void chargement(){
		int nouveauDA;
		char lePrenom[21];
		char leNom[31];
		int lAge;
		FILE * pfichier;
		pfichier = fopen(DONNEES, "r");
		if(pfichier != NULL){
			while(fscanf(pfichier, "%8d %20s %30s %3d", &nouveauDA, lePrenom, leNom, &lAge)!=EOF){
				ajoutEnTete(nouveauDA, lePrenom, leNom, lAge);
			}fclose(pfichier);
		}else{
			printf("ERREUR, le fichier ne peut etre ouvert\n");
		}
}

void impression(int leDA, char lePrenom[], char leNom[], int lAge){
		FILE * pfichier;
		pfichier = fopen(DONNEES, "a+");
		fprintf(pfichier, "%d %s %s %d", leDA, lePrenom, leNom, lAge);
}

void nouvelAjout(){
	struct Etudiants *ajouter, *pointe;
	////////////////////
	///////A ajuster pour la verification////////
	//////////////////////
	ajouter = nouveau(3,"jonny", "legros", 25);
	//impression(3,"jonny","legros",25);
		pointe = premier;
		while(pointe->suivant != NULL){
			pointe = pointe -> suivant;
		}
		pointe->suivant = ajouter;
		ajouter->suivant = NULL;
}

int menu(){
	char debut[LIGNEMAX];
	int vrai = 0;
	VIDER;
		while(!vrai){
		printf("%s", LEMENU);
		fgets(debut, LIGNEMAX, stdin);

		int taille = strlen(debut);
		if(taille == 1){
			VIDER;
			printf("%s\n", ERREUR_CHOIX);
			 vrai = 0;
		}else if(taille == 2 && (debut[0] == '1' || debut[0] == '2' || debut[0] == '3' || debut[0] == '4')){
			vrai = 1;
		}
		else{
			VIDER;
			printf("%s\n", ERREUR_CHOIX);
			 vrai = 0;
		}
	}

	int leChoix = atoi(debut);

return leChoix;
}


int main() {
	chargement();
	//int debut = menu();
	nouvelAjout();
	afficheListe();
	//impression();
	libererListe();
	afficheListe();
return 0;
}