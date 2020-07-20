from Zadanie2_2 import to_weird_case
import pytest


@pytest.mark.parametrize("n, result", [("String", 'StRiNg'), ("python" , "PyThOn"),
                                       ("Jaś i Małgosia na wakacjach", "JaŚ i MaŁgOsIa Na WaKaCjAcH")])
def test_to_weird_case(n, result):
    assert to_weird_case(n) == result