"""3. Napisz funkcję która przyjmie jako argument kod morse'a. Czyli ciąg kropek i kresek, np.:

A = ‘·−‘
Q = ‘−−·−‘
1 = ‘·−−−−‘
czyli w kodzie morse'a SOS wyglądałoby:

SOS = ‘···−−−···’
Iii ta nowa funkcja powinna zwrócić zakodowany tekst, czyli np.:

decode_morse('...   ---   ...') # => 'S O S'"""
def decode_morse(txt_in_morse):

    morse_code = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
                  "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
                  "..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","-----":"0",".----":"1","..---":"2",
                  "...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",".-.-":"Ą",
                  "-.-..":"Ć","..-..":"Ę",".-..-":"Ł","--.--":"Ń","---.":"Ó","...-...":"Ś","--..-.":"Ż","--..-":"Ź",
                  }
    txt_decoded = txt_in_morse.split("   ")
    txt_translated = ""
    for i in txt_decoded:
        txt_translated += morse_code[i]
    return txt_translated
print(decode_morse('-.-..   ---   ...'))

