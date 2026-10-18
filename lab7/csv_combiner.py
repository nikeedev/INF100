from pathlib import Path
import csv, io, os

def merge_table_into(master_table, new_table):
    table = new_table[1:]
    
    #print(new_table[0])
    if len(master_table) == 0:
        master_table.append(new_table[0])
   
    for i in range(len(table)):
        master_table.append(table[i])
   
def combine_csv_in_dir(dirpath, result_path):
    out = []
    for root, dirnames, filenames in os.walk(dirpath):
        for name in filenames:
            if name.endswith(".csv"):
                data = Path(root+"/"+name).read_text(encoding="utf-8")    
                reader = csv.reader(io.StringIO(data), delimiter=',', quotechar="\"")

                merge_table_into(out, list(reader))

    # print(out)
    
    string = io.StringIO()
    write = csv.writer(string, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    
    for elem in out:
        write.writerow(elem)
    
    Path(result_path).write_text(string.getvalue(), encoding="utf-8")

    #print(Path(result_path).read_text(encoding="utf-8"))


