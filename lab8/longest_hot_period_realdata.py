from pathlib import Path
from datetime import datetime

def longest_hot_period(client_id, source_id, start_date, end_date, threshold):

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


