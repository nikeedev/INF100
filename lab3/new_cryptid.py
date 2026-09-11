from pathlib import Path
import json

content = Path("cryptids.json").read_text(encoding="utf-8")
data = json.loads(content)

my_cryptid = {
    "navn": "Bergness",
    "sted": "Festplassen",
    "observasjoner": 504,
    "farlig": False,
    "kjennetegn": ["regnjakke", "spiser boller", "liker regn"]
}

data["kryptider"].append(my_cryptid)
data["versjon"] += 1
data["sist_oppdatert"] = "2026-09-11"

content = json.dumps(data, indent=2, ensure_ascii=False)
Path("new_cryptids.json").write_text(content, encoding="utf-8")
