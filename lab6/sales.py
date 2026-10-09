from pathlib import Path

def total_income(path):
    # name,production_cost,price,sold
    sales = Path(path).read_text(encoding='utf-8').splitlines()[1:]
    
    income = 0

    for sale in sales:
        splited = sale.split(",")
        
        income += int(splited[2]) * int(splited[3]) - (int(splited[1]) * int(splited[3])) 

    return income
        


def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')

if __name__ == "__main__":
    test_total_income()
