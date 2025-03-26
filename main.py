"""Fichier contenant le code central du projet"""
from rectangles_diag_entière import liste_rect
from circles import verif_inter_3_4, check_intersections
from time import time
from csv_manage import add_rows

def calcul_sol(cote_lim, N,E):
    """
    Renvoie le nombres de rectangles répondant aux conditions données, ainsi que le nombre de rectangles total avec comme longueur maximale cote_lim.
    
    entree : cote_lim:int, N:int, E:str
    sortie : tuple:(float, int, int)
    """
    
    assert cote_lim > 1 and type(cote_lim) == int and E in ("exactement", "au moins")
    start=time()
    values = [["Largeur","Longueur","Nombres de points"]]
    l_solution = []
    l_rectangle = liste_rect(cote_lim)
    nbr_solution = 0
    
    if E == "exactement":
        for i in range (len(l_rectangle)):
            
            a,b = l_rectangle[i][0],l_rectangle[i][1]
            l_solution = verif_inter_3_4(check_intersections(a,b), (a,b))
            
            values.append([a,b,len(l_solution)])
            
            if len(l_solution) == N:
                nbr_solution += 1
    else :
        for i in range (len(l_rectangle)):
            
            a,b = l_rectangle[i][0],l_rectangle[i][1]
            l_solution = verif_inter_3_4(check_intersections(a,b), (a,b))
            
            values.append([a,b,len(l_solution)])
            
            if len(l_solution) >= N:
                nbr_solution += 1   
                  
    add_rows(values,"rectangles.csv")    
    duree = round(time()-start,2)
            
    return (duree, nbr_solution, len(l_rectangle))

lim = int(input("Entrez la longueur maximale entière souhaitée : "))
sol_min = int(input("\nCombien de solutions entières souhaitez-vous obtenir pour les rectangles?"))
categorie = input("\nSouhaitez-vous trouver les rectangles avec au moins ou exactement ce nombre de solutions?").lower()
solutions = calcul_sol(lim,sol_min,categorie)

print("\n*******************START*******************")
print(f"\nDuree de traitement : {solutions[0]}")
print(f"Dans le cas de rectangles a cote maximum de {lim}, on a trouve {solutions[1]} rectangles parmi les  {solutions[2]} disponibles qui avaient {categorie} {sol_min} solutions")
print("\n********************END********************")


