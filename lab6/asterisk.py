
def add_asterisks(s):
    words = s.split(";")
    
    asterisked = ""
    
    for i in range(len(words)):
        asterisked += f"*{words[i]}*"
        if not i == len(words) - 1:
            asterisked += ";"

    return asterisked


def test_add_asterisks():
    print('Testing add_asterisks...', end='')

    # Test 1
    arg = 'foo;bar;qux'
    actual = add_asterisks(arg)
    expected = '*foo*;*bar*;*qux*'
    assert expected == actual

    # Test 2
    arg = 'honey;mustard'
    actual = add_asterisks(arg)
    expected = '*honey*;*mustard*'
    assert expected == actual

    print('OK')

if __name__ == "__main__":
    test_add_asterisks()

