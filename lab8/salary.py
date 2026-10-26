def weekly_pay(hourly_rate, hours):
    if hourly_rate < 200:
        return 'Minstelønnskravet er ikke oppfylt'
    if hours > 60:
        return 'En ansatt jobber mer enn 60 timer'
    
    if hours > 40:
        rest = hours - 40

        current = hourly_rate * 40
        current += hourly_rate*1.5 * rest

        return current
    else:
        current = hourly_rate * hours
        return current

def test_weekly_pay():
    print('Tester weekly_pay... ', end='')
    assert 2_000 == weekly_pay(200, 10)
    assert 40_000 == weekly_pay(1000, 40)
    assert 20_000 == weekly_pay(500, 40)
    assert 41_500 == weekly_pay(1000, 41)
    assert 70_000 == weekly_pay(1000, 60)
    assert 'En ansatt jobber mer enn 60 timer' == weekly_pay(1000, 61)
    assert 'Minstelønnskravet er ikke oppfylt' == weekly_pay(199, 40)
    assert 'Minstelønnskravet er ikke oppfylt' == weekly_pay(100, 100)
    print('OK')

if __name__ == '__main__':
    test_weekly_pay()
