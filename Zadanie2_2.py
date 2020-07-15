"""2. Napisz funkcję która przyjmuje stringa i zwraca go ze wszystkimi parzystymi znakami,
 napisanymi wielką literą, a nieparzystymi znakami małą literą. Przyjmij indeksowanie od zera.

to_weird_case('String') # => zwraca 'StRiNg'
to_weird_case('Algorytmy i struktury danych') # => zwraca 'AlGoRyTmY I StRuKtUrY DaNyCh"""
def to_weird_case(word):
    weird_word = str()
    a = 1
    for character in word:
        if character == " ":
            weird_word += character
            pass
        else:
            if a%2 == 0:
                weird_word += character.lower()
            else:
                weird_word += character.upper()
            a += 1
    return weird_word

