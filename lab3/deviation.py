from pathlib import Path
import json

def load_emission_data(filename):
    file_content = Path(filename).read_text(encoding='utf-8')
    data = json.loads(file_content)

    return data

def get_deviations(data):
    values = data["data"]
    
    deviation = []

    for value in values:
        value = value["intensity"]
        if not (value["actual"] == None or value["forecast"] == None):
            deviation.append(abs(value["forecast"] - value["actual"]))

    return deviation

def count_values_larger_than(values, threshold):
    too_large = 0

    for value in values:
        if value > threshold:
            too_large += 1

    return too_large


def main():
    filename = input()
    threshold = int(input())

    data = load_emission_data(filename)
    deviation = get_deviations(data)
    count = count_values_larger_than(deviation, threshold)

    print(f"Antall avvik større enn {threshold}: {count}")
    
if __name__ == "__main__":
    main()


