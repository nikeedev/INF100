def find_treasure(grid, target_sum):
    treasures = []
    col = len(grid)
    row = len(grid[0])

    for i in range(col):
        for j in range(row):
            if i + j + grid[i][j] == target_sum:
                treasures.append([i, j])

    return treasures

def test_find_treasure():
    print('Testing find_treasure... ', end='')
    # Test 1
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    target_value = 5
    actual = find_treasure(grid, target_value)
    expected = [[0, 2], [1, 0]]
    assert expected == actual

    # Test 2
    actual = find_treasure([[1, 2], [3, 4]], 3)
    expected = [[0, 1]]
    assert expected == actual

    # Test 3
    actual = find_treasure([[1, 2], [3, 4]], 1)
    expected = [[0, 0]]
    assert expected == actual

    # Test 4
    actual = find_treasure([[1, 2], [3, 4]], 1000)
    expected = []
    assert expected == actual

    print('OK')

if __name__ == "__main__":
    test_find_treasure()
