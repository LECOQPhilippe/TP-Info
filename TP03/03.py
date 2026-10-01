a = int(input("Saissisez un nombre positif n : "))
while a < 0 :
    a = int(input("Saissisez un nombre POSITIF n : "))


""""
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
    

print("La factorielle de : ",a," est : ",factorielle(a),".")
"""
    


def Syraccus(n):
    if n%2 == 0:
        n = n/2
        print ("La valeur actuelle de n dans la suite de Syraccus est de : ",n,".")
        return Syraccus(n)
    elif n == 1 :
        return n
    else:
        n = n*3 +1
        print ("La valeur actuelle de n dans la suite de Syraccus est de : ",n,".")
        return Syraccus(n)


print ("La suite de Syraccus de nombre ",a," est : ",Syraccus(a),".")



















































































