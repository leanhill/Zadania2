from Zadanie2_2 import to_weird_case


def test_to_weird_case():
    assert to_weird_case("String") == "StRiNg"
    assert to_weird_case("Mama i tata") == "MaMa I tAtA"
