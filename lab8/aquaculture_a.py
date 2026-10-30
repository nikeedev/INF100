from pathlib import Path
import csv, io

def count_facilities_by_species(path):
    file = Path(path).read_text(encoding="cp1252")

    splited = file.splitlines()[1:]
    data = "\n".join(splited)

    reader = csv.reader(io.StringIO(data), delimiter=';', quotechar="\"")
    table = list(reader)
    
    fish = {}
    for i in range(1, len(table)):
        if table[i][12] not in fish:
            fish[table[i][12]] = 1
        else:
            fish[table[i][12]] += 1
    
    # listed_fish = listed_fish[2:]
    fishkeys = sorted(fish.keys())
    
    for fish_key in fishkeys:
        print(f"{fish_key}: {fish[fish_key]}")
   
   
if __name__ == '__main__':
    count_facilities_by_species('Akvakulturregisteret.csv')
