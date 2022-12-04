#fonction qui envoi la valeur moyenne d’une liste :

def moyenne (n):
    c=0
    for i in n:
        c=c+i
    m=len(n)
    r=c/m
    return r
    
#fonction qui renvoi le min et le max selon l'utilisateur :

def minmax(a,b):
    c=a[0]
    if b == "min" :
        for i in a :
            if i < c :
                c=i
        return c
    elif b=="max" :
        for i in a :
            if i > c :
                c=i
        return c
    else :
        print("svp entrez le choix correcte ")


###########################################################################


# t = int(input("quelle est la taille de votre liste : "))

# a=[]

# for i in range(t):
#     print("entrez la valeur de composant",i+1,"de la liste : ")
#     x=int(input("- "))
#     a.append(x)

# r=moyenne(a)
# print("la moyenne de serie",a,"est",r)

###########################################################################

# t = int(input("quelle est la taille de votre liste : "))

# a=[]

# for i in range(t):
#     print("entrez la valeur de composant",i+1,"de la liste :")
#     x=int(input("- "))
#     a.append(x)

# b =input("entrez votre choix (min) ou (max) : ")
# r=minmax(a,b)
# if b == "min" :
#     print("le minimum de la serie",a,"est",r) 
# elif b=="max" :
#     print("le maximum de serie",a,"est",r)

###########################################################################


