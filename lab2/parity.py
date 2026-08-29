def parity(x):
    return "Partall" if x % 2 == 0 else "Oddetall"


print('Tester parity... ', end='')
assert 'Partall' == parity(0)
assert 'Oddetall' == parity(1) 
assert 'Partall' == parity(42)
assert 'Oddetall' == parity(99)
print('OK')
