
def almost_equals(first_num, sec_num):
    difference = abs(sec_num - first_num)
    
    if difference <= 0.000000001:
        return True
    else:
        return False

def test_almost_equals():
    print("Testing almost_equals...", end=" ")
    assert almost_equals(0.1 + 0.2, 0.3) is True
    assert almost_equals(2, 3) is False
    assert almost_equals(3, 2) is False
    print("OK")    

test_almost_equals()

