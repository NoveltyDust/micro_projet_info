"""
Fichier contenant les fonctions secondaires du projet.

On a regroupé les fonctions qui sont complémentaires à létude de cercles, 
ainsi qu'une fonction offrant une interactivité pour la suite du projet (add_rows)

"""

# On importe les méthodes et fonctions
from csv import writer
from math import sqrt

def liste_rect(N):
    """
    Renvoie une liste de tuple contenant les dimensions d'un rectangle de cotes entiers <= N et de diagonales entieres.
    
    entree: N:int
    sortie: rect:list
    """
    
    # On définit la liste
    rect = []  
    
    # Boucle de la fonction
    for a in range(1,N):
        for b in range(a,N+1):
            
            e = sqrt(a**2+b**2) # On calcule la diagonale
            
            if int(e)==e: # On vérifie que la diagonale est entière
                
                rect.append((a,b)) # On met à jour la liste
    
    return rect # On retourne la liste de rectangles

def repere(b,a):
    """
    Renvoie une liste contenant les coordonnées de chaque sommet d'un rectangle donné.
    
    entree : b:int, a:int
    sortie : coordonnees:tuple
    """
    
    return (0, 0), (a, 0), (a, b), (0, b) # On retourne les coordonnées

def add_rows(values, csvfile):
    """
    Ecrit des lignes dans un fichier csv donné.
    
    Entree : values:list, csvfile:str
    Sortie : None
    """
    
    with open(csvfile,'w',newline='') as file: # On ouvre les fichier en mode "écriture"
        add = writer(file,delimiter=';')
        add.writerows(values) # On écrit les valeurs dans le fichier