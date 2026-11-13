


n = int(input("saisir le nombre d'approx voulu : "))

def approx(n):

    pi = 3

    for i in range (2,n+2):

        pi += (4/((i)*(i+1)*(i+2)))*((-1)**i)
        print("L'approximation de rang",i," de pi est : ",pi," .")

    return pi

print("L'approximation de rang  1  de pi est : 3.")  

print(approx(n))


print (__name__)