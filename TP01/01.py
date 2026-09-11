
"""
masse = eval(input("Saisir votre masse en Kilogramme : "))
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

#exo 4
somme = 0
for i in range(1,15,1):
    itération = -((-1)**i) * (4/((i*2)+(i*2+1)+(i*2+2)))
    somme += itération
    approx = 3 + somme
    print(f"Approximation de pi au terme {approx}")


