

def polygone():
    cote = list(range(100))
    liste_poly = []
    for a in range(len(cote)):  
        for b in range(a, len(cote)):  
            for c in range(b, len(cote)):  
                for d in range(c, len(cote)):  
                    liste_poly.append((cote[a], cote[b], cote[c], cote[d]))

    return(liste_poly)

list=polygone()
poly = (17,1,78,98)

def verif(L,poly): 
    if poly in L:
        print("Trouvé !")
    else:
        print("Pas trouvé.")

verif(list,poly)
print(len(list))