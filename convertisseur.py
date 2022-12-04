#convertisseur d'un nombre décimal en un nombre binaire :

def convert (n) :
    inv = []
    while n != 0 :
        c= n%2
        n=n//2
        inv.append(c)
    inv.reverse()
    x = len(inv)
    for i in range(0,x):
        print(inv[i],end=" ")
      

n=int(input("entrez la valeur de nombre decimal :"))
convert(n)

