from math import sqrt


def liste_rect(N):
    rect = []
    
    for a in range(1,N):
        for b in range(a,N+1):
            e = sqrt(a**2+b**2)
            if int(e)==e :
                rect.append((a,b))

    return rect
                

print(liste_rect(200))
