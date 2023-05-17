class Auto():
    def __init__(self,registracni_znacka,typ_vozidla,najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def get_info(self):
        return f"Registrační značka vozidla je {self.registracni_znacka} a typ je {self.typ_vozidla}"

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            print(f"Potvrzuji zapůjčení vozidla")
        else:
            print(f"Vozidlo není k dispozici")
    
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.najete_km = stav_tachometru
        self.pocet_dni = pocet_dni
        self.dostupne = True
        platba = 0
        if pocet_dni <= 7:
            platba = pocet_dni * 400
        else:
            platba = pocet_dni * 300 
        print(f"Děkujeme za vrácení auta a jste dlužný {platba}Kč")

auto_1 = Auto("4A2 3020","Peugeot 403 Cabrio",47534)

auto_2 = Auto("1P3 4747","Škoda Octavia",41253)

auto_1.pujc_auto()
print(auto_1.get_info())
auto_1.pujc_auto()
auto_1.vrat_auto(int(input("Kolik kilometrů je na tachometru?")), int(input("Kolik dni jste měl auto?")))
auto_1.pujc_auto()
