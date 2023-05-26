import json
with open('body.json', encoding='utf-8') as file:
    body = json.load(file)

for 

prospech = {}

for name, points in body.items():
    if points >= 60:
        prospech[name] = "true"
    else:
        prospech[name] = "false"

with open('prospech.json', 'w', encoding='utf-8') as file:
    json.dump(prospech, file, ensure_ascii=False, indent=4)