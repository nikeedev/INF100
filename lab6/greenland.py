from pathlib import Path
import csv
import io

def total_volume(path):
    text_file = Path(path).read_text(encoding='utf-8')
    
    reader = csv.reader(io.StringIO(text_file), delimiter=',', quotechar="'")

    table = list(reader)
    headers = table[0]
    regions = table[1:]
    
    tot = 0

    # region,area_km2,mean_thickness_m
    for region in regions:
        tot += int(float(region[1]) * float(region[2])) / 1000
    
    #print(f"tot: {tot}\nregions: {regions}")
    return tot

def sea_level_rise(path):
    # print(f"{total_volume(path) / 395000}, rounded: {round(total_volume(path) / 395000, 1)}")
    return round(total_volume(path) / 395000, 1)

def test_total_volume():
    print('Tester total_volume... ', end='')
    assert round(total_volume('greenland.csv')) == 2829200
    print('OK')

def test_sea_level_rise():
    print('Tester sea_level_rise... ', end='')
    assert sea_level_rise('greenland.csv') == 7.2
    print('OK')

if __name__ == '__main__':
    # test_total_volume()
    # test_sea_level_rise()
    print(f"I Antarktis vil havet øke med {sea_level_rise('antarctica.csv')}m")

