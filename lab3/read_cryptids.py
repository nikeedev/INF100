from pathlib import Path
import json

content = Path("cryptids.json").read_text(encoding="utf-8")
data = json.loads(content)


highest_i = 0
for i in range(len(data["kryptider"])):
    if data["kryptider"][highest_i]["siste_rapport"]["år"] < data["kryptider"][i]["siste_rapport"]["år"]: 
        highest_i = i

print(data["kryptider"][highest_i]["navn"])

for i in range(len(data["kryptider"])):
    print(f"{i+1}. {data["kryptider"][i]["navn"]}: {data["kryptider"][i]["kjennetegn"]}")

print()

for key in data["kryptider"][0].keys():
    print(f"{key} : {data["kryptider"][0][key]}")

"""
print(f"navn : {data["kryptider"][0]["navn"]}")
print(f"sted : {data["kryptider"][0]["sted"]}")
print(f"observasjoner : {data["kryptider"][0]["observasjoner"]}")
print(f"farlig : {data["kryptider"][0]["farlig"]}")
print(f"lengde_m : {data["kryptider"][0]["lengde_m"]}")
print(f"kjennetegn : {data["kryptider"][0]["kjennetegn"]}")
print(f"siste_rapport : {data["kryptider"][0]["siste_rapport"]}")


total = 0
for kryptid in data["kryptider"]:
    total = total + kryptid["observasjoner"]
"""

