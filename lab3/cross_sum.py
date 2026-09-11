def cross_sum(x):
    total = 0

    for num in str(x):
        total += int(num)

    return total

def test_cross_sum():
    print('Tester cross_sum... ', end='')
    assert 6 == cross_sum(123)
    assert 7 == cross_sum(34)
    assert 0 == cross_sum(0)
    assert 1 == cross_sum(100)
    print('OK')



def nth_cross_sum(n, x):
    count = 0
    num_to_test = 0

    while count < n:
        cross = cross_sum(num_to_test)
        if cross == x:
            count += 1
        num_to_test += 1

    return num_to_test - 1



def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print('OK')


if __name__ == "__main__":
    test_cross_sum()
    test_nth_cross_sum()


