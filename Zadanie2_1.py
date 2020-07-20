"""1. Napisz funkcję, która przyjmuje listę 11 liczb całkowitych i zwraca stringa w formacie numeru telefonu.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) # => returns "(+12) 345-678-901"""

def create_phone_number(phone_number_digits):
    phone_number = f"(+{phone_number_digits[0]}{phone_number_digits[1]}) {phone_number_digits[2]}{phone_number_digits[3]}" \
                   f"{phone_number_digits[4]}-{phone_number_digits[5]}{phone_number_digits[6]}{phone_number_digits[7]}" \
                   f"-{phone_number_digits[8]}{phone_number_digits[9]}{phone_number_digits[10]}"
    return phone_number


