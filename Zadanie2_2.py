"""2. Napisz funkcję która przyjmuje stringa i zwraca go ze wszystkimi parzystymi znakami,
 napisanymi wielką literą, a nieparzystymi znakami małą literą. Przyjmij indeksowanie od zera.

to_weird_case('String') # => zwraca 'StRiNg'
to_weird_case('Algorytmy i struktury danych') # => zwraca 'AlGoRyTmY I StRuKtUrY DaNyCh"""
def to_weird_case(word_toget_weird):
    weird_word = str()
    for i in range (len(word_toget_weird)):
        if i%2 == 0:
            weird_word += word_toget_weird[i].upper()
        else:
            weird_word += word_toget_weird[i].lower()
    return weird_word
