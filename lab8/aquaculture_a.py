from pathlib import Path
import csv, io

def count_facilities_by_species(path):
    file = Path(path).read_text(encoding="cp1252")
    splited = file.splitlines()
    data = "\n".join(sorted(splited))

    reader = csv.reader(io.StringIO(data), delimiter=';', quotechar="\"")
   
    table = list(reader)
    
    fish = {}

    for i in range(2, len(table)):
        if not table[i][12] in fish:
            fish[table[i][12]] = 1
        else:
            fish[table[i][12]] += 1
    
    listed_fish = []
    for key in fish.keys():
        listed_fish.append([key, fish[key]])

    listed_fish.sort()
    listed_fish = listed_fish[2:]
    
    for fih in listed_fish:
        print(f"{fih[0]}: {fih[1]}")
   
   
if __name__ == '__main__':
    count_facilities_by_species('Akvakulturregisteret.csv')
