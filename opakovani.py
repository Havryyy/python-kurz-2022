"""nazevHry = "Romeo a Julie"
cenaListku = 150
zlevnenaCena = 150 * 0.9

vek = int(input("zadej vek"))

if vek >= 13:
    pocetListku = int(input("zadej pocet listku"))
    celkovaCena = cenaListku * pocetListku
    celkovaCenaSleva = celkovaCena - cenaListku
    if pocetListku <= 3:
        print(f"celkova cena je po sleve {celkovaCenaSleva}")
    else:
        print(f"celkova cena je {celkovaCena}")
exit()"""

"""venecky = [1, 2, 1, 2, 6, 3, 2]

print(venecky[0])

print(venecky[0:5]) #(venecky[zcatek:konec+1])"""

pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])
print(pohyby[2:])
print(sum(pohyby))
print(max(pohyby))
print(min(pohyby))
print(len(pohyby))
