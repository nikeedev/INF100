from pathlib import Path
import csv, io

def sum_of_column(path, col):
    data = Path(path).read_text(encoding="utf-8")
    reader = csv.reader(io.StringIO(data), delimiter=',', quotechar="\"")
    
    table = list(reader)

    total = 0
    for i in table:
        try:
            num = i[col]
            if not "." in num:
                total += int(num)
        except:
            total += 0
    return total
    

def test_sum_of_column():
    print('Tester sum_of_column... ', end='')
    assert(42.0 == sum_of_column('foo.csv', 0))
    assert(95.0 == sum_of_column('foo.csv', 1))
    assert(0.0 == sum_of_column('foo.csv', 2))
    assert(76363.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 1))
    assert(46007.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 2))
    assert(5024518.0 == sum_of_column('airport-codes.csv', 3))
    print('OK')

if __name__ == '__main__':
    test_sum_of_column()
