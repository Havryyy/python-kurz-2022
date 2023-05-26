def verify_phone_number(number):
    if len(number) == 9:
        return number.isnumeric() 
    elif len(number) == 13: 
        if number[:4] == "+420" and number[4:].isnumeric():
            return True
    return False 

def calculate_message_cost(message):
    message_length = len(message)
    if message_length % 180 == 0:
        return int(message_length / 180) * 3
    else:
        return (int(message_length / 180) + 1) * 3

phone_number = input("Zadej telefonní číslo: ")
if verify_phone_number(phone_number):
    message_text = input("Zadej text zprávy: ")
    message_cost = calculate_message_cost(message_text)
    print(f"Cena zprávy je {message_cost} Kč.")
else:
    print("Zadané číslo není platné.")
