from Zadanie2_3 import decode_morse
def test_decode_morse():
    assert decode_morse('...   ---   ...') == "SOS"