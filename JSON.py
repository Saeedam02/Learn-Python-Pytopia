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
# in dump+s and load+s, s is related to dumping strings

# decode, deserialization
decoded = json.loads(output) # decoded's type is dic.

# Dumping a File:
# encode, serialization
with open("data_file.json", "w") as f:
    json.dump(data, f)

# decode, deserialization
with open("data_file.json") as f:
    data = json.load(f)

# Useful Keyword Arguments
print(json.dumps(data, indent=2)) # indent =2 is good for long datasets. for shorter ones we can even use indent = 4.