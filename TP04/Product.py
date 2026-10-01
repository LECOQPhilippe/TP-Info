


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

























