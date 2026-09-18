def g(x):
    return (1/8)*x**2 - 2*x + 10


def approx_area_under_g(x_lo, x_hi):
    diff = x_hi - x_lo
    
    total = 0
    for i in range(diff):
        total += g(i + x_lo)
    
    return total

##########################################
def get_endpoints(i, n, x_lo, x_hi):
    diff = x_hi - x_lo
    one_length = diff/n
    start = x_lo + (one_length * i)    
    end = start + one_length

    return (start, end)
##########################################

def riemann_sum_g(x_lo, x_hi, n):
    b = (x_hi - x_lo) / n
    
    tot_areal = 0

    for i in range(0, n):
        x_i = x_lo + b * i
        
        tot_areal += g(x_i) * b
    
    return tot_areal


def riemann_sum(f, x_lo, x_hi, n):
    b = (x_hi - x_lo) / n
    
    tot_areal = 0

    for i in range(0, n):
        x_i = x_lo + b * i
        
        tot_areal += f(x_i) * b
    
    return tot_areal   

def almost_equals(a, b):
    return abs(a - b) < 0.0000001

def test_g():
    print('Tester g... ', end='')
    # Første test
    x = 8.0
    actual = g(x)
    expected = 2.0
    assert almost_equals(expected, actual)

    # Flere tester
    assert almost_equals(4.0, g(4.0))
    assert almost_equals(10.0, g(0.0))
    print('OK')

def test_approx_area_under_g():
    print('Tester approx_area_under_g... ', end='')
    # Første test
    x_lo = 4
    x_hi = 5
    actual = approx_area_under_g(x_lo, x_hi) 
    expected = 4.0  # skal gi oss kun g(4), som altså er 4.0
    assert almost_equals(expected, actual)

    # Flere tester
    assert almost_equals(3.125, approx_area_under_g(5, 6)) # g(5)
    assert almost_equals(7.125, approx_area_under_g(4, 6)) # g(4)+g(5)
    assert almost_equals(23.75, approx_area_under_g(1, 5)) # g(1)+g(2)+g(3)+g(4)
    print('OK')

def test_riemann_sum_g():
    print('Tester riemann_sum_g... ', end='')
    assert almost_equals(7.125, riemann_sum_g(4, 6, 2))
    assert almost_equals(6.71875, riemann_sum_g(4, 6, 4))
    assert almost_equals(6.3348335, riemann_sum_g(4, 6, 1000))

    assert almost_equals(23.75, riemann_sum_g(1, 5, 4))
    assert almost_equals(22.4375, riemann_sum_g(1, 5, 8))
    assert almost_equals(21.166676666, riemann_sum_g(1, 5, 1_000_000))
    print('OK')


def test_riemann_sum():
    test_riemann_sum_using_g()
    test_riemann_sum_using_square()
    test_riemann_sum_using_linear()

def test_riemann_sum_using_g():
    print('Tester riemann_sum med funksjonen g... ', end='')
    assert almost_equals(7.125, riemann_sum(g, 4, 6, 2))
    assert almost_equals(6.71875, riemann_sum(g, 4, 6, 4))
    assert almost_equals(6.3348335, riemann_sum(g, 4, 6, 1000))

    assert almost_equals(23.75, riemann_sum(g, 1, 5, 4))
    assert almost_equals(22.4375, riemann_sum(g, 1, 5, 8))
    assert almost_equals(21.166676666, riemann_sum(g, 1, 5, 1_000_000))
    print('OK')

def test_riemann_sum_using_square():
    def square(x):
        return x**2

    ## Arealet under grafen square(x) = x**2 mellom 1 og 3
    ## Eksakt svar  er 8 + 2/3, altså 8.66666666....
    ## Merk at vi kommer gradvis nærmere eksakt svar ved å øke n
    print('Tester riemann_sum med funksjonen square... ', end='')
    assert almost_equals(5.0, riemann_sum(square, 1, 3, 2))
    assert almost_equals(7.88, riemann_sum(square, 1, 3, 10))
    assert almost_equals(8.5868, riemann_sum(square, 1, 3, 100))
    print('OK')

def test_riemann_sum_using_linear():
    def linear(x):
        return x

    ## Arealet under grafen for funksjonen f(x) = x mellom 2 og 4
    ## Eksakt svar er 6.
    ## Merk at vi kommer gradvis nærmere riktig svar ved å øke n
    print('Tester riemann_sum med funksjonen linear... ', end='')
    assert almost_equals(5.0, riemann_sum(linear, 2, 4, 2))
    assert almost_equals(5.5, riemann_sum(linear, 2, 4, 4))
    assert almost_equals(5.998046875, riemann_sum(linear, 2, 4, 1024))
    print('OK')

if __name__ == '__main__':  
    # Del A
    test_g()
    
    # Del B
    test_approx_area_under_g()

    # Del C
    test_riemann_sum_g()
    test_riemann_sum()


