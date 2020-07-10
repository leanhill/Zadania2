"""1. Napisz funkcję, która przyjmuje listę 11 liczb całkowitych i zwraca stringa w formacie numeru telefonu.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) # => returns "(+12) 345-678-901"""

def create_phone_number(phone_number_digits):
    phone_number_digits = str(phone_number_digits).strip("[]")
    phone_number_digits = phone_number_digits.replace(", ","")
    phone_number = f"(+{phone_number_digits[:2]}) {phone_number_digits[2:5]}-{phone_number_digits[5:8]}-{phone_number_digits[8:11]}"
    return phone_number


