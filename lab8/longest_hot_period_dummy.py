def longest_hot_period(temperatures, threshold):
    start = -1
    end = -1

    longest_hot_period = 0
    current_start = -1

    for i in range(len(temperatures)):
        if temperatures[i] >= threshold:
            if current_start == -1:
                current_start = i

        else:
            if current_start != -1:
                length = i - current_start

                if length > longest_hot_period:
                    longest_hot_period = length
                    start = current_start
                    end = i

                current_start = -1

    if current_start != -1:
        length = len(temperatures) - current_start

        if length > longest_hot_period:
            start = current_start
            end = len(temperatures)

    return (start, end)


def test_longest_hot_period():
    print('Testing longest_hot_period... ', end='')
    temps = [25, 23, 19, 22, 24, 25, 21, 25, 26]

    threshold = 22
    expected_start, expected_end = 3, 6
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 23
    expected_start, expected_end = 0, 2
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 15
    expected_start, expected_end = 0, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 21
    expected_start, expected_end = 3, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 25
    expected_start, expected_end = 7, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 30
    expected_start, expected_end = -1, -1
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    print('OK')

if __name__ == '__main__':
    test_longest_hot_period()
