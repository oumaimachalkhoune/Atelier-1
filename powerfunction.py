#Une fonction qui renvoie la puissance d’un nombre X^n :

def puissance(base,exposant):
    if exposant == 0 :
        return 1
    elif exposant > 0 :
        b=base
        for i in range (1,exposant):
            base = base * b 
        return base
    else :
        base = 1 / base
        b = base
        exposant= exposant*(-1)
        for i in range (1,exposant):
            base = base * b 
        return base


x=int(input("entrez la valeur de la base : "))
n=int(input("entrez la valeur de lexposant : "))
r=puissance(x,n)
print("la puissance de X est : ",r)