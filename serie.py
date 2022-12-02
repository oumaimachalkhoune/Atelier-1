#la somme de serie 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 :

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def serie():
    e=0
    for i in range(1,6):
        e=e+(fact(i)/i)
    return e

r=serie()
print("la somme de serie 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 est :",r)