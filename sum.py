#Le calcul de somme des nombres de 1 à n:

def somme(n):
    s=0
    for i in range (1,n+1):
        s=s+i
    return s


n=int(input("entrez la valeur de n : "))
r=somme(n)
print("la somme de 1 jusqu'à",n,"est",r)