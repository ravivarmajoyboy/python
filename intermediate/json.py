import json

data = {"name": "law", "skills": ["python", "ctf"], "year": 3, "active": True, "x": None}

text = json.dumps(data)
print(text)
print(json.dumps(data, indent=2, sort_keys=True))

back = json.loads(text)
print(back["skills"])
print(type(back))

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)
print(loaded)

try:
    json.loads("{bad json}")
except json.JSONDecodeError as e:
    print("invalid json:", e)

raw = '[{"id": 1}, {"id": 2}]'
for item in json.loads(raw):
    print(item["id"])
