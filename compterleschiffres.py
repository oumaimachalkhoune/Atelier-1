#compter les chiffres d'un nombre donné :

def chiffre(n):
 
    if n==0 :
        return 1
    c=0
    if n<0 :
        n=n*(-1) 
    while n!=0 :
        n=n//10 
        c=c+1
    return c


x=int(input("entez la valeur de n : "))
c=chiffre(x)
print("les chiffres de nombre",x,"est",c)
    