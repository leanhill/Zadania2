from Zadanie2_1 import create_phone_number
import pytest



@pytest.mark.parametrize("n, result", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1], "(+12) 345-678-901"),
                                       ([1, 0, 3, 4, 5, 6, 7, 8, 9, 0, 1], "(+10) 345-678-901"),
                                       ([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], "(+00) 111-222-333")])
def test_create_phone_number(n, result):
    assert create_phone_number(n) == result