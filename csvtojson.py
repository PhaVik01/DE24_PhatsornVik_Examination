import csv
import json

csv_file = "profiles1.csv"
json_file = "data.json"

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f , indent=2, ensure_ascii=False)


