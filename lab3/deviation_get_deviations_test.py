from deviation import get_deviations


def main():
    test_get_deviations()


def test_get_deviations():
    print('Testing get_deviations...', end=' ')

    # Test A
    arg = {
        'data': [
            {
                'from': '2025-09-13T23:00Z',
                'to': '2025-09-13T23:30Z',
                'intensity': {'forecast': 100, 'actual': 80, 'index': 'low'},
            },
            {
                'from': '2025-09-13T23:30Z',
                'to': '2025-09-14T00:00Z',
                'intensity': {'forecast': 90, 'actual': 94, 'index': 'low'},
            },
            {
                'from': '2025-09-14T00:00Z',
                'to': '2025-09-14T00:30Z',
                'intensity': {'forecast': 93, 'actual': None, 'index': 'low'},
            },
        ]
    }
    expected = [20, 4]
    actual = get_deviations(arg)
    assert expected == actual

    # Test B
    arg = {
        'data': [
            {
                'from': '2025-09-13T23:00Z',
                'to': '2025-09-13T23:30Z',
                'intensity': {'forecast': None, 'actual': 80, 'index': 'low'},
            },
            {
                'from': '2025-09-13T23:30Z',
                'to': '2025-09-14T00:00Z',
                'intensity': {'forecast': 90, 'actual': 94, 'index': 'low'},
            },
            {
                'from': '2025-09-14T00:00Z',
                'to': '2025-09-14T00:30Z',
                'intensity': {'forecast': 93, 'actual': 90, 'index': 'low'},
            },
            {
                'from': '2025-09-14T00:30Z',
                'to': '2025-09-14T01:00Z',
                'intensity': {'forecast': 100, 'actual': 100, 'index': 'low'},
            }
        ]
    }
    expected = [4, 3, 0]
    actual = get_deviations(arg)
    assert expected == actual

    print('OK')


if __name__ == '__main__':
    main()
