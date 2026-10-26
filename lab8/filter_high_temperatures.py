from pathlib import Path

def filter_high_temperatures(path_input, path_output, threshold_temp):
    temps = Path(path_input).read_text(encoding="utf-8").splitlines()

    over_threshold = []
    
    for temp in temps:
        split_temp = temp.split(" ")
        
        if float(split_temp[1]) >= threshold_temp:
            over_threshold.append(temp)
    
    Path(path_output).write_text("\n".join(over_threshold), encoding="utf-8")

def test_filter_high_temperatures():
    print('Tester filter_high_temperatures... ', end='')
    filter_high_temperatures('temperatures.txt', 'high_temps.txt', 23.5)
    expected = (
        'Monday 23.5\n'
        'Wednesday 24.0\n'
        'Thursday 23.9\n'
        'Sunday 23.9\n'
    )
    with open('high_temps.txt', 'rt', encoding='utf-8') as file:
        actual = file.read()
    assert expected.strip() == actual.strip()
    print('OK')

if __name__ == '__main__':
    test_filter_high_temperatures()


