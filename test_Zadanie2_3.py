from Zadanie2_3 import decode_morse
import pytest


@pytest.mark.parametrize("n, result", [('...   ---   ...', "SOS"), ("-.-..   --   .-", "ĆMA")])
def test_decode_morse(n, result):
    assert decode_morse(n) == result