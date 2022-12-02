# la factorielle d’un nombre n :

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("entrez la valeur de n : "))
r=fact(n)
print("la factorielle de",n,"est :",r)