# chercher un élément dans une matrice puis renvoi sa position :

def position(a,n):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if n==a[i][j]:
                print("la position de",n,"est (",i,") (",j,")")



n=int(input("entrez l'element que vous cherchez : "))
a = [[1,2,1],[4,5,6],[7,8,9],[3,5,1]]
position(a,n)