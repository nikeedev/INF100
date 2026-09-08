def get_endpoints(i, n, x_lo, x_hi):
    diff = x_hi - x_lo
    
    one_length = diff/n
    
    start = x_lo + (one_length * i)
    
    end = start + one_length

    return (start, end)
    
def main():
    x_lo = float(input("x_lo = "))  
    x_hi = float(input("x_hi = "))
    n = int(input("n = "))
    
    for i in range(n):
        start, end = get_endpoints(i, n, x_lo, x_hi)
        print(start, end)

def almost_equals(a, b):
    return abs(a - b) < 0.000000001

def test_get_endpoints():
    print('Testing get_endpoints... ', end='')
    start, end = get_endpoints(1, 4, 50.0, 150.0)
    assert almost_equals(75, start)
    assert almost_equals(100, end)

    start, end = get_endpoints(3, 4, 50.0, 150.0)
    assert almost_equals(125, start)
    assert almost_equals(150, end)

    start, end = get_endpoints(0, 3, -30, 60)
    assert almost_equals(-30, start)
    assert almost_equals(0, end)
    print('OK')

# test_get_endpoints()

if __name__ == "__main__":
    main()
