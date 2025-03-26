"""
Fichier principal du projet.

Centre du projet : En lançant le programme on peut obtenir le résultat souhaité (sauf visualisation).

"""

# On importe les méthodes et fonctions nécessaires
from circles import verif_inter_3_4, check_intersections
from fonctions_rectangle import liste_rect, add_rows
from time import time

def calcul_sol(cote_lim=int, N=int, E=str):
    """
    Renvoie le nombres de rectangles répondant aux conditions données, ainsi que le nombre de rectangles total avec comme longueur maximale cote_lim.
    
    entree : cote_lim:int, N:int, E:str
    sortie : (duree:float, nbr_solution:int, len(l_rectangle):int):tuple
    """
    
    # On vérifie que les entrées fonctionnent
    assert cote_lim > 1 and type(cote_lim) == int and E in ("exactement", "au moins")
    
    # On définit les variables nécessaires
    start=time()
    values = [["Largeur","Longueur","Nombres de points"]]
    l_solution = []
    l_rectangle = liste_rect(cote_lim)
    nbr_solution = 0
    
    # Boucle de la fonction
    for i in range (len(l_rectangle)):
        
        a,b = l_rectangle[i][0],l_rectangle[i][1] # On récupère la longueur et la largeur du rectangle
        l_solution = verif_inter_3_4(check_intersections(b), a, b) # On récupère les intersections entre les 4 cercles
        
        # On met à jour les valeurs pour le csv
        values.append([a,b,len(l_solution)])
        
        if E=="exactement": # On détermine la méthode à utiliser
            if len(l_solution) == N:
                
                nbr_solution += 1 # On met à jour le nombre de rectangles qui respectent la condition     
        else:
            if len(l_solution) >= N:
                
                nbr_solution += 1 # On met à jour le nombre de rectangles qui respectent la condition
                  
    add_rows(values,"rectangles.csv") # On met à jour le csv (ou on le crée au besoin)
    duree = round(time()-start,2) # On détermine la durée qu'il a fallu pour exécuter le programme
            
    return (duree, nbr_solution, len(l_rectangle)) # On retourne les variables utiles

# Phase de paramètrage des entrées
print()
lim = int(input("Entrez la \033[1m longueur maximale entiere \033[0m souhaitee : "))
print()
sol_min = int(input("Combien de \033[1m solutions entieres \033[0m souhaitez-vous obtenir pour les rectangles? "))
print()
categorie = input("Souhaitez-vous trouver les rectangles avec \033[1m au moins \033[0m ou \033[1m exactement \033[0m ce nombre de solutions? ").lower()

solutions = calcul_sol(lim,sol_min,categorie) # On lance la fonction principale

# On affiche le résultat
print("\n\n*******************START*******************")
print(f"\n \033[1m Duree de traitement : \033[0m {solutions[0]} secondes.")
print(f"Dans le cas de rectangles a cote maximum de {lim}, on a trouve {solutions[1]} rectangles parmi les  {solutions[2]} disponibles qui avaient {categorie} {sol_min} solutions.")
print("\n********************END********************\n")


