import json
with open('body.json', encoding='utf-8') as file:
    dictionary = json.load(file)

prospech = {}

for name, points in dictionary.items():
    if points >= 60:
        prospech[name] = "true"
    else:
        prospech[name] = "false"

with open('prospech.json', 'w', encoding='utf-8') as file:
    json.dump(prospech, file, ensure_ascii=False, indent=4)