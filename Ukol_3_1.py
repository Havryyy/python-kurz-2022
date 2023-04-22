import json
with open('seznam.json', encoding='utf-8') as file:
    dictionary = json.load(file)

new_dictionary = {}

for name, points in dictionary.items():
    if points >= 60:
        new_dictionary[name] = "true"
    else:
        new_dictionary[name] = "false"

print(new_dictionary)