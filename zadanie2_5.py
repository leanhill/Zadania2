"""5. Zaimplementuj funkcję która bedzie przyjmować string i będzie zwracać wszystkie litery
 które leżą pod nieparzystymi indeksami:)

teleturniej -> eeune
komputer -> optr"""
def get_odd_letters(word):
    odd_letters=word[1::2]
    return odd_letters
