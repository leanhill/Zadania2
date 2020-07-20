from zadanie2_5 import get_odd_letters
import pytest


@pytest.mark.parametrize("n, result", [("teleturniej", "eeune"), ("komputer", "optr"),
                                       ("lawataka", "aaaa")])
def test_get_odd_letters(n, result):
    assert get_odd_letters(n) == result