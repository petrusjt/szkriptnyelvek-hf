from anagramma import is_anagramma1, is_anagramma2, is_anagramma3, normalize


def test_normalize():
    assert normalize('Clint Eastwood') == 'clinteastwood'
    assert normalize(' \t\n\r') == ''
    assert normalize('ABCDEF') == 'abcdef'
    assert normalize(' S ch oolm a\nst er ') == 'schoolmaster'


def test_is_anagramma1():
    assert is_anagramma1('silent', 'listen')
    assert is_anagramma1('Elegant man', 'A gentleman')
    assert is_anagramma1('Old west action', 'Clint Eastwood')
    assert is_anagramma1('dormitory', 'dirty room')
    assert not is_anagramma1('a', 'aaaaaaaaaaaaaa')
    assert not is_anagramma1('alma', 'körte')
    assert not is_anagramma1('óra', 'apró')


def test_is_anagramma2():
    assert is_anagramma2('silent', 'listen')
    assert is_anagramma2('Elegant man', 'A gentleman')
    assert is_anagramma2('Old west action', 'Clint Eastwood')
    assert is_anagramma2('dormitory', 'dirty room')
    assert not is_anagramma2('ab', 'abababababababababa')
    assert not is_anagramma2('alma', 'körte')
    assert not is_anagramma2('óra', 'apró')


def test_is_anagramma3():
    assert is_anagramma3('silent', 'listen')
    assert is_anagramma3('Elegant man', 'A gentleman')
    assert is_anagramma3('Old west action', 'Clint Eastwood')
    assert is_anagramma3('dormitory', 'dirty room')
    assert not is_anagramma3('ab', 'abababababababababa')
    assert not is_anagramma3('alma', 'körte')
    assert not is_anagramma3('óra', 'apró')
