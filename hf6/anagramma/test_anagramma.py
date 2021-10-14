from anagramma import is_anagramma1, is_anagramma2


def test_is_anagramma1():
    assert is_anagramma1('silent', 'listen')
    assert is_anagramma1('Elegant man', 'A gentleman')
    assert is_anagramma1('Old west action', 'Clint Eastwood')
    assert is_anagramma1('dormitory', 'dirty room')


def test_is_anagramma2():
    assert is_anagramma2('silent', 'listen')
    assert is_anagramma2('Elegant man', 'A gentleman')
    assert is_anagramma2('Old west action', 'Clint Eastwood')
    assert is_anagramma2('dormitory', 'dirty room')
