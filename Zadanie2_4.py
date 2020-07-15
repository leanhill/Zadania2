
"""4. Zaimplementuj sortowanie bąbelkowe. W programowaniu problem sortowań jest jednym z ważniejszych problemów,
ponieważ każdą daną da się przedstawić jako cyfrę
 (zerknij sobie tak w ramach świadomości na tablekę na tej stronie:
  http://www.asciitable.com/ ) i zauważ że litery mają swoje odpowiedniki w liczbach :D)
Załączam również link który opisuje jak ono działa:
 http://www.algorytm.edu.pl/algorytmy-maturalne/sortowanie-babelkowe.html"""
def bubble_sort(number_to_sort):
    number_bubbled = list(number_to_sort)
    for i in range (len(number_to_sort)):
        for i in range(len(number_to_sort) - 1):
            if number_bubbled[i] > number_bubbled[i + 1]:
                a = number_bubbled[i]
                number_bubbled[i] = number_bubbled[i + 1]
                number_bubbled[i + 1] = a
    return number_bubbled


