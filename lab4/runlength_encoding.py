def compress(raw_binary):
    num = 1
    digits = []

    if raw_binary[0] == "1":
        digits.append(0)

    for i in range(len(raw_binary) - 1):
        if raw_binary[i] == raw_binary[i + 1]:
            num += 1
        else:
            digits.append(num)
            num = 1

    digits.append(num)

    return digits   


def decompress(compressed_binary):
    binary = ""
        
    onezero = "0"

    i = 0
    if compressed_binary[0] == 0:
        onezero = "1"
        i = 1

    while i < len(compressed_binary):
        binary += onezero * compressed_binary[i]

        onezero = "0" if onezero == "1" else "1"
        i += 1

    return binary

def test_compress():
    print('Tester compress... ', end='')
    assert([2, 3, 4, 4] == compress('0011100001111'))
    assert([0, 2, 1, 8, 1] == compress('110111111110'))
    assert([4] == compress('0000'))
    print('OK')

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')

if __name__ == "__main__":
    test_compress()
    test_decompress()


