# la fréquence d’un caractère dans une chaîne :

def freq(a,b):
    c=0
    for i in a :
        if i == b :
            c=c+1
    return c


a=input("entrez votre texte : ")
b=input("entrez le caractere : ")
c=freq(a,b)
print("la frequence de\"",b,"\"dans\"",a,"\"est",c)

