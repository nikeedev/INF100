from matplotlib import pyplot as plt
from pathlib import Path
import csv, io

file = Path('Akvakulturregisteret.csv').read_text(encoding="cp1252")

# splited = file.splitlines()    
reader = csv.reader(io.StringIO(file), delimiter=';', quotechar="\"")
    
table = list(reader)

land_x_values = []
land_y_values = []

sea_x_values = []
sea_y_values = []

for i in range(2, len(table)):
    if table[i][19] == "LAND":
        land_x_values.append(float(table[i][24]))
        land_y_values.append(float(table[i][23]))
    else:
        sea_x_values.append(float(table[i][24]))
        sea_y_values.append(float(table[i][23]))


plt.scatter(land_x_values, land_y_values, c = "darkgreen", alpha=0.3, label="Land")

plt.scatter(sea_x_values, sea_y_values, c = "lightblue",  alpha=0.15, label="Sjø")

plt.xlabel('Nord i grader')
plt.ylabel('Øst i grader')

plt.title('Oppdrettsanlegg i sjø eller på land')

plt.legend(
    title='Oppdrettsanlegg',
    loc='upper right',
    fontsize='small',
)
plt.show()



