from Zadanie2_4 import bubble_sort
import pytest


@pytest.mark.parametrize("n, result", [("9876", ["6", "7", "8", "9"]), ("155849", ["1", "4", "5", "5", "8", "9"]),
                                       ("888881", ["1", "8", "8", "8", "8", "8"])])
def test_bubble_sort(n, result):
    assert bubble_sort(n) == result