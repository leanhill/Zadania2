from Zadanie2_1 import create_phone_number


def test_create_phone_number():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) == "(+12) 345-678-901"