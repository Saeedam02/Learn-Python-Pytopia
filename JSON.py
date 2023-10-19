# Serializing JSON
import json

data = {
    "students": [
        {
            "Name": "Ali Hejazizo",
            "Grade": (14.0, 20),
        },
        {
            "Name": "Masoud Zarepoor",
            "Grade": None,
            "is_in_class": True
        }
    ]
}

# encode, serialization
output = json.dumps(data) # output's type is string.
# dump+s is related to dumping strings

# decode, deserialization
decoded = json.loads(output) # decoded's type is dic.

# Dumping a File:
# encode, serialization
with open("data_file.json", "w") as f:
    json.dump(data, f)

# decode, deserialization
with open("data_file.json") as f:
    data = json.load(f)