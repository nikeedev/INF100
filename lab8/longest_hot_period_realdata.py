from pathlib import Path
from datetime import datetime
import requests
import json
import longest_hot_period_dummy as lh 

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
    # data = json.dumps(json_data, indent=2)
    temps = []
    for date in json_data["data"]:
        temps.append(float(date["observations"][0]["value"]))

    start, end = lh.longest_hot_period(temps, threshold)

    return (
        datetime.fromisoformat(json_data["data"][start]["referenceTime"]),
        datetime.fromisoformat(json_data["data"][end]["referenceTime"])
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

