'''def eur_to_czk(pocet_eur):
    kurz = 25 #lok8ln9 prom2nn8
    pocet_czk = pocet_eur * kurz
    return pocet_czk


eura_uzivatel = int(input("kolik"))
print(eur_to_czk(eura_uzivatel))
'''
'''
def mult(a, b):
    
    return a * b

a = int(input("napis A"))
b = int(input("napis B"))
vysledek = mult()
print(vysledek)
'''

def total_price(people, breakfast=False):
    cena_noc = 850
    cena_snidane = 125

    celkem = cena_noc * people
    
    if breakfast:
        celkem += cena_snidane * people
    return celkem

print(f'cena za tri lidi{total_price(3)}')
print(f'Cena za se snidani {total_price(2, True)}')
