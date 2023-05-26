
"""class Balik ():
    
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
    def __str__(self):
        if self.doruceno:
            return f"Balik byl doruceny na {self.adresa} a ma hmotnost {self.hmotnost} kg"
        return f"Balik nebyl doruceny."
    
    def doruc(self):
        self.doruceno = True


moj_balik = Balik("Trenčín 3", 3)
print(moj_balik.adresa)

moj_balik.doruc()
print(moj_balik)"""

class Balik():
    def __init__(self, adresa, hmotnost):
        self.adresa  = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def __str__(self):
        if self.doruceno:
            return f"Balik bol doruceny na {self.adresa} a ma hmotnost {self.hmotnost} kg"
        return f"Balik nebol doruceny"
    
    def doruc(self):
        self.doruceno = True

class CennyBalik (Balik):
    def __init__(self, hodnota):
        super().__init__()
        self.hodnota = hodnota

moj_balik = Balik("Trencin 3", 3,)

print(moj_balik.adresa)
print(moj_balik)
moj_balik.doruc()
print(moj_balik)