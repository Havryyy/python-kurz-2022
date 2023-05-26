'''Vysvedceni = {
    "cesky jazyk" : 1,
    "matematika" :2,
    "dejepis" :3
}
print(Vysvedceni["cesky jazyk"])

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100


tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo = int(input("jaké je tvé číslo"))


if cislo in tombola:
    print({tombola[cislo]})
else:
    print("Bohuzel")
    
cislo = tombola.pop(cislo)

'''
passwords = {
    "Jiří": "tajne-heslo", 
    "Natálie": "jeste-tajnejsi-heslo", 
    "Klára": "nejtajnejsi-heslo"
}
'''
jmeno = input("Rekni jmeno")

if jmeno in passwords:
    heslo = input("Jaké je tvé heslo:")
    
    if heslo in {passwords[heslo]}:

        print("Smíš vstoupit.")
    else:
        print("nemuzes vstoupit")
else:
    print("nemuzes")

'''
'''
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

znamky = school_report.values()

prumer = sum(znamky)/len(school_report)
print(prumer)


for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)
'''
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

pocet_stran = 0
for kniha in books:
    pocet_stran += kniha["pages"]
