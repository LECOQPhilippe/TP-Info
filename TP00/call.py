lst = []
n = int(input("Ajouter un nombre (-1 pour quitter) : "))
while(n >= 0):
    lst.append(n)
    n = int(input("Ajouter un nombre (-1 pour quitter) : "))

print(lst)
    
print(lst.sort())
print(sum(lst)/len(lst))


