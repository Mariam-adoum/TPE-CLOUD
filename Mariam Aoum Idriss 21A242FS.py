def nombre_premier(n):#definition de la fonction
    premier = [] #tableau qui va contenir les nombres premiers
    for i in range(2, n+1): #parcourir de 2-N
        est_premier = True #variable pour verifier si c'est un nombre premier
        for num in range(2, int(i/2)+1): # parcourir de 2-i
            if i % num == 0: #si un nombre peut diviser i.
                est_premier = False # si oui, ce n'est pas un nombre premier
                break #et on sort de la boucle
        if est_premier: #si c'est un nombre premier
            premier.append(i) #mettre i dans le tableau
    return premier #renvoi le tableau


nombre = 14
print(nombre_premier(nombre)) # imprime le tableau
