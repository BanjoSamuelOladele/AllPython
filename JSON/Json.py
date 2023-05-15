"""Serializing data"""
import json

# json = javascript object oriented notation

records = {
    "Student record": [
        {"id": 1, "name": "Ebuka", "age": 41},
        {"id": 2, "name": "Ebuk", "age": 44},
        {"id": 3, "name": "Ebua", "age": 42}
    ]
}

with open("records.json", mode="w") as record:
    json.dump(records, record)

with open("records.json", mode="r") as record2:
    print(json.dumps(json.load(record2), indent=4))
