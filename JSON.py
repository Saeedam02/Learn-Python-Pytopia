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

# decode, deserialization
decoded = json.loads(output) # decoded's type is dic.
