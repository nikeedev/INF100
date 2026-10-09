from pathlib import Path

def try_to_convert(s):
    try:
        return int(s)
    except:
        return 0

def get_stringsum(s):
    splited = s.split(" ")

    tot = 0

    for i in splited:
        tot += try_to_convert(i) 
    return tot

def get_line_with_highest_stringsum(s):
    splited = s.splitlines()
    
    highest_tot = 0
    highest_i = 0
    highest_line = ""

    for i in range(len(splited)):
        tot = get_stringsum(splited[i])
        if tot > highest_tot:
            highest_tot = tot
            highest_i = i + 1
            highest_line = splited[i]

    return (highest_i, highest_tot, highest_line)
    

def test_get_line_with_highest_stringsum():
    print('Testing get_line_with_highest_stringsum... ', end='')

    arg = '4 2\n3 3\n6 6 6 6 12 6\n'
    assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

    arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
    assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

    arg = '4 2\n3 3\n'
    assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

    print('OK')

def test_get_stringsum():
    print('Testing get_stringsum... ', end='')
    assert 6 == get_stringsum('4 2')
    assert 9 == get_stringsum('5 -1 3 +2')
    assert 11 == get_stringsum('5 - 1 3 + 2')
    assert 42 == get_stringsum('42')
    assert 42 == get_stringsum('forty-one 42 førtitre')
    assert 42 == get_stringsum('foo2 42 2qux 3x1')
    assert 0 == get_stringsum('')
    assert 0 == get_stringsum('foo bar qux')
    assert 0 == get_stringsum('-9- 3+2')
    print('OK')

if __name__ == "__main__":
    # test_get_stringsum()
    # test_get_line_with_highest_stringsum()
    filename = input("Filnavn: ")
    
    highest_i, highest_tot, highest_line = get_line_with_highest_stringsum(Path(filename).read_text(encoding='utf-8'))

    print(f"Høyeste strengsum er {highest_tot}, funnet først på linje {highest_i}: \"{highest_line}\"")
