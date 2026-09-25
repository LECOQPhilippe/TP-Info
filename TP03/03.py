a = int(input("Saissisez un nombre positif n : "))
while a < 0 :
    a = int(input("Saissisez un nombre POSITIF n : "))

#EXO 1 TRKL
""""
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
    

print("La factorielle de : ",a," est : ",factorielle(a),".")
"""
    
#EXO 2 LE BOSS DES BOSS

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



'''''
import sys

def main():
    try:
        # Vérification du nombre d'arguments
        if len(sys.argv) != 4:
            raise ValueError("Utilisation : ./HeadTail.py <head|tail> <nb_lignes> <chemin_fichier>")

        mode = sys.argv[1].lower()
        nb_lignes_str = sys.argv[2]
        fichier_path = sys.argv[3]

        # 1. Validation du mode (head ou tail)
        if mode not in ["head", "tail"]:
            raise ValueError("Le premier paramètre doit être 'head' ou 'tail'.")

        # 2. Validation du nombre de lignes (entier positif)
        if not nb_lignes_str.isdigit() or int(nb_lignes_str) <= 0:
            raise ValueError("Le deuxième paramètre doit être un nombre entier positif.")
        
        nb_lignes = int(nb_lignes_str)

        # 3. Lecture du fichier (Gestion de l'IOError / FileNotFoundError)
        with open(fichier_path, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        # Affichage selon le mode
        if mode == "head":
            resultat = lignes[:nb_lignes]
        else:
            resultat = lignes[-nb_lignes:] if nb_lignes <= len(lignes) else lignes

        # Formatage et affichage des lignes
        print("".join(resultat), end="")

    # Attrape les erreurs de paramètres personnalisées
    except ValueError as e:
        print(f"Erreur de paramètre : {e}")
    # Attrape les erreurs de lecture/fichier non trouvé
    except OSError as e:  # En Python 3, IOError est un alias de OSError
        print(f"Erreur d'E/S : Impossible de trouver ou lire le fichier '{sys.argv[3] if len(sys.argv) > 3 else ''}'.")
    # Attrape toute autre exception imprévue sans faire planter le script
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()
'''












































































