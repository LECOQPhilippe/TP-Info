
try:
    n= int(input("Saisir une valeur de n entiere positive pour qu'on trouve sa factorielle : "))
except ValueError:
    print("La valeur n'est pas entiere positive ")

def factorielle(n):
    if n == 1:
        return 1
    else : 
        n = n*factorielle(n-1)
        return n


print("La factorielle du nombre n choisi : ",n," est : \n",factorielle(n),".")
    





