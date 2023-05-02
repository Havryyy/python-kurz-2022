def calculate_message_cost(message):
    message_length = len(message)
    if message_length % 180 == 0:
        return int(message_length / 180) * 3
    else:
        return (int(message_length / 180) + 1) * 3

calculate_message_cost(63)    
print(calculate_message_cost())