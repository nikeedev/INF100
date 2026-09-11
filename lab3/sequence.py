def sequence_for(n):
    text = ""
    for i in range(0, n + 1):
        text += str(i) + " "
    # print(text)
    return text

def test_sequence_for():
    print("Tester sequence_for... ", end="")
    assert "0 1 2 3 4 5 " == sequence_for(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
    assert "0 " == sequence_for(0)
    print("OK")

test_sequence_for()

def sequence_while(n):
    text = ""
    i = 0

    while i <= n:
        text += str(i) + " "
        i += 1

    # print(text)
    return text

def test_sequence_while():
    print("Tester sequence_while... ", end="")
    assert "0 1 2 3 4 5 " == sequence_while(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
    assert "0 " == sequence_while(0)
    print("OK")

test_sequence_while()


