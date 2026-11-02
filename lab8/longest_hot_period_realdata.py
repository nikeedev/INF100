from pathlib import Path
from datetime import datetime, timedelta
import requests
import json

def longest_hot_period_dummy(temperatures, threshold):
    start = -1
    end = -1

    longest_hot_period = 0
    current_start = -1

    for i in range(len(temperatures)):
        if temperatures[i] >= threshold:
            if current_start == -1:
                current_start = i

        else:
            if current_start != -1:
                length = i - current_start

                if length >= longest_hot_period:
                    longest_hot_period = length
                    start = current_start
                    end = i

                current_start = -1

    if current_start != -1:
        length = len(temperatures) - current_start

        if length >= longest_hot_period:
            start = current_start
            end = len(temperatures)

    return (start, end)


def longest_hot_period(client_id, source_id, start_date, end_date, threshold):
    api_endpoint = 'https://frost.met.no/observations/v0.jsonld'
    
    response = requests.get(
        api_endpoint,
        params = {
            'sources': source_id,
            'referencetime': f'{start_date.date().isoformat()}/{end_date.date().isoformat()}',
            'elements': 'mean(air_temperature P1D)',
            'levels': 'default',
            'timeoffsets': 'default',
        },
        headers = {'User-Agent': 'inf100.ii.uib.no nigon5433'},
        auth = (client_id, '')
    )

    json_data = response.json()
    #print(json_data)
    temps = []
    dates = []

    for date in json_data["data"]:
        temps.append(float(date["observations"][0]["value"]))
        dates.append(datetime.fromisoformat(date["referenceTime"][:10]))

    start, end = longest_hot_period_dummy(temps, threshold)

    # print(dates)
    """
    for i in range(start - 2, end + 3):
        print(dates[i], temps[i])    
    """
    if start == -1:
        return (None, None)
    """
    print(
        dates[start],
        dates[end - 1]
    )
    """


    return (
        dates[start],
        dates[end]
    )


def test_longest_hot_period():
    client_id = Path('client_id.txt').read_text(encoding='utf-8').strip()
    start_date = datetime(year=2000, month=1, day=1)
    end_date = datetime(year=2024, month=1, day=1)
    threshold = 20
    source_id = 'SN50540' # Florida målestasjon i Bergen

    actual_start, actual_end = longest_hot_period(
        client_id, source_id, start_date, end_date, threshold
    )
    actual_start = actual_start.replace(tzinfo=None) # Fjerner tidssone
    actual_end = actual_end.replace(tzinfo=None) # Fjerner tidssone
    expected_start = datetime(year=2009, month=6, day=25)
    expected_end = datetime(year=2009, month=7, day=5)

    assert actual_start == expected_start
    assert actual_end == expected_end

if __name__ == '__main__':
    test_longest_hot_period()

