import random
import statistics



"""listku = 3
for _ in range(listku):

    print(random.randint(1,1000))"""
"""
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]


nova_cisla = [cislo * 2 for cislo in cisla] 
zaporna = [-cislo for cislo in cisla]
mocniny = [cislo ** 2 for cislo in cisla]
string = [str(cislo) for cislo in cisla]
print(nova_cisla)
print(zaporna)
print(mocniny)
print(string)

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

delka_jmen = [len(jmeno) for jmeno in jmena]

print(delka_jmen)"""

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [statistics.mean(teplota) for teplota in teploty]
ranni = [teplota[0] for teplota in teploty]
nocni = [teplota[3] for teplota in teploty]
poledni_nocni = [[teplota[3], teplota[3]] for teplota in teploty]

print(prumer)
print(ranni)
print(nocni)
print(poledni_nocni)
