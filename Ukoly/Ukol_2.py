'''
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

produkt = input("Zadejte kód součástky: ")
if produkt in sklad:
  pocet = int(input("Zadejte množství: "))
  if pocet < sklad[produkt]:
    sklad[produkt] = sklad[produkt] - pocet
    print(f"Poptávku lze uspokojit v plné výši.")
  elif pocet > sklad[produkt]:
    print(f"Součástky {produkt} lze prodat jen omezené množství {sklad[produkt]}.")
    sklad.pop(produkt)
else:
  print(f"Součástka {produkt} není skladem.")
'''
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

text = ([*input("co by jsi rád napsal")])
if text in morse_code:
    
