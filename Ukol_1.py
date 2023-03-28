"""jmeno = "david"
print(jmeno+"@czechitas.cz")"""

jmenoAPrijmeni = input("Napiš své jméno: ")
inicialy = jmenoAPrijmeni.split()
first = inicialy[0].upper()
second = inicialy[1].upper()
print(first[0]+".",second[0]+".")
print(jmenoAPrijmeni.upper())
print(jmenoAPrijmeni.lower())
print(jmenoAPrijmeni.title())

if len(first) <= 5:
    print(jmenoAPrijmeni.title())
else:
    print(first[0]+".",second.title())

