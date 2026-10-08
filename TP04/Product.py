from __future__ import annotations #Permet d'utiliser la classe Fraction dans les annotations de type avant sa définition
import math

"""

class Product:
    flat_tax = 0.2
    def __init__(self,code,nom,prixHT):
        self.code = code
        self.nom = nom
        self.prixHT = prixHT

    def get_price_TTC(self, tax):
        TTC = self.prixHT * ( 1 + tax )
        return TTC
    
    def get_price_TTC_normal(self):
        TTC = self.prixHT * ( 1 + Product.flat_tax )
        return TTC
        
p = Product("AAAAA","Andouillette",8)
print(p.get_price_TTC(0.055))
print(p.get_price_TTC_normal())

print("Le produit proposé est : ",p,". Son prix TTC est de : ",p.get_price_TTC(0.055))

"""


class Fraction:
    def __init__(self, num: int, den: int):
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        
        self.num = num
        self.den = den 

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__ (self,other: Fraction) -> Fraction:
        A = self.num*other.den
        B = self.den*other.den
        C = other.num*self.den
        return Fraction(A+C, B)
    

    def __sub__ (self,other : Fraction) -> Fraction:
        A = self.num*other.den
        B = self.den*other.den
        C = other.num*self.den
        return Fraction(A-C, B)
    
    def __mul__(self,other : Fraction) -> Fraction:
        A = self.num*other.num
        B = self.den*other.den
        return Fraction(A,B)
    
    def __truediv__(self,other : Fraction) -> Fraction:
        return (self.num*other.den) / (self.den*other.num)

f1 = Fraction(2,3)
f2 = Fraction(3,4)

print (f1/f2)






















