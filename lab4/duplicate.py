# my_list = [3, 2, 5, 10]

def duplicate(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

def duplicated(numbers):
    b = []
    for i in range(len(numbers)):
        b.append(numbers[i] * 2)
    return b


def test_duplicate():
    print('Testing duplicate...', end=' ', flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicate(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [3, 2]
    duplicate(arg)
    duplicate(arg)
    expected = [12, 8]
    assert expected == arg

    print('OK')


def test_duplicated():
    print('Testing duplicated...', end=' ', flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicated(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val == expected
    assert arg == [2, 3, 10, 3, 4]

    # Test 2
    arg = [3, 2]
    return_val = duplicated(duplicated(arg))
    expected = [12, 8]
    assert return_val == expected
    assert arg == [3, 2]

    print('OK')

if __name__ == "__main__":
    test_duplicate()
    test_duplicated()
