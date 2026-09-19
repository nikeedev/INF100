import copy

def duplicate(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

def duplicated(numbers):
    b = []
    for i in range(len(numbers)):
        b.append(numbers[i] * 2)
    return b


def duplicate_2d(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] *= 2

def duplicated_2d(grid):
    b = copy.deepcopy(grid)
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] *= 2
            
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

def test_duplicate_2d():
    print('Testing duplicate_2d...', end=' ', flush=True)

    # Test 1
    arg = [
        [2, 3, 4],
        [4, 1, 0]
    ]
    return_val = duplicate_2d(arg)
    expected = [
        [4, 6, 8],
        [8, 2, 0]
    ]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    duplicate_2d(arg)
    duplicate_2d(arg)
    expected = [[12, 8], [8, 4], [4, 0]]
    assert expected == arg

    print('OK')

def test_duplicated_2d():
    print('Testing duplicated_2d...', end=' ', flush=True)

    # Test 1
    arg = [
        [2, 3, 4],
        [4, 1, 0]
    ]
    return_val = duplicated_2d(arg)
    expected = [
        [4, 6, 8],
        [8, 2, 0]
    ]
    assert return_val == expected
    assert arg == [
        [2, 3, 4],
        [4, 1, 0]
    ]

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    return_val = duplicated_2d(duplicated_2d(arg))
    expected = [[12, 8], [8, 4], [4, 0]]
    assert return_val == expected
    assert arg == [[3, 2], [2, 1], [1, 0]]

    print('OK')

if __name__ == "__main__":
    test_duplicate()
    test_duplicated()
    test_duplicate_2d()
    test_duplicated_2d()
