"""
Fichier contenant les fonctions secondaires du projet.

On a regroupé les fonctions qui sont complémentaires à létude de cercles, 
ainsi qu'une fonction offrant une interactivité pour la suite du projet (add_rows)

"""


# On importe les méthodes et fonctions
from csv import writer
from math import sqrt


def liste_rect(N,p):
    """
    Renvoie une liste de tuple contenant les dimensions d'un rectangle de cotes entiers <= N et de diagonales entieres.
    
    entree: N:int
    sortie: rect:list
    """
    
    # On définit la liste
    rect = []  
    if p == "non":
        # Boucle de la fonction
        for a in range(1,N):
            for b in range(a,N+1):
                
                e = sqrt(a**2+b**2) # On calcule la diagonale
                
                if int(e)==e: # On vérifie que la diagonale est entière
                    
                    rect.append((a,b)) # On met à jour la liste
        
        return rect # On retourne la liste de rectangles
    else:
        return rect_premier(N)
    



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

def PGCD(a, b): 
    b,a = sorted((a,b))
  
    # si b=0 
    if (b==0): 
        # renvoi de a 
        return a 
    else: # sinon 
        # calcul du reste r de la division de a par b 
        r = a % b 
  
        # appel de la fonction PGCD pour a=b et b=r 
        return PGCD(b, r)

def rect_premier(N):
    return [rect for rect in liste_rect(N,"non") if PGCD(rect[0],rect[1]) == 1 ]
            
           