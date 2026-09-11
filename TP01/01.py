
"""
masse = 'eval'(input("Saisir votre masse en Kilogramme : "))
taille = eval(input("Saisir votre taille en mètre : "))

IMC = masse/(taille**2)

print(f"Votre IMC est de : {IMC} \n ")
"""
"""
n = 0
list = []
while n >= 0:
    n = eval(input("Saississez un nombre : "))
    list.append(n)
    
print(f"voici la liste de base : {list}")
list.sort()
print(f"voici la liste trié : {list}")
print(f"voici le plus petit nombre de la liste : {min(list)}")
print(f"voici le plus grand nombre de la liste : {max(list)}") 

moyenne = (sum(list)/len(list))
print (f"Voici la moyenne de la liste : {moyenne}")
"""
""""
#exo 3
age=-1
while age < 0:
    age = eval(input("entrez un age du chien positif: "))

if age <= 2:
    chien = age * 10.5
    print(f"age en années canines : {round(chien)}")
else:
    chien = 2 * 10.5 + (age - 2) * 4
    print(f"age en années canine : {round(chien)}")
"""
""""
#exo 4

def approximation(n):

    pi_approx = 3
    k = 2
    signe = 1
    for i in range(n) : 
        terme = signe * 4 / (k * (k + 1) * (k + 2))
        pi_approx += terme
        k += 2
        signe = -signe
    return pi_approx
M = eval(input("Choisir un nombre positif n pour définir la précision de l'approximation de pi : \n"))    
while M < 0 : 
     M = eval(input("Choisir un nombre positif n pour définir la précision de l'approximation de pi : \n"))    
print (approximation(M))
"""
""""
#exo 5

q = eval(input("Saisir un nombre entier : "))
while q != round(q) :
    q = eval(input("Saisir un nombre entier : "))

r = -1
resultat = ""
while q != 0 :
    r = q%2
    q = q//2
    resultat += f"{r}"
    if q == 1 and r == 1 :
        resultat += f"{r}"
        break

        
print(f"Le résultat est de : \n {resultat}")
"""

#exo 7 correction

from string import ascii_uppercase
import random

def get_plaque():
    plaque = ""
    good_char = [x for x in ascii_uppercase if x not in ['U','I','O'] ]
    for i in range(9):
        if i in [2,6]:
            plaque = f"{plaque}-"
        elif i in [3,4,5]:
            plaque = f"{plaque}{random.randint(0,9)}"
        else:
            plaque = f"{plaque}{random.choice(good_char)}"

    # Façon récursive de traiter le SS, si on en trouve un, on regen la plaque
    if 'SS' in plaque:
        plaque = get_plaque()
    return plaque

if __name__ == '__main__':
    for i in range(20):
        print(get_plaque())
















