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

########################################################
##### Encoding and Decoding Custom Python Objects ######
########################################################

class CustomType:
    pass
data = {
    'custom_type': CustomType()
}

json.dumps(data) #->TypeError: Object of type CustomType is not JSON serializable

###############################
##### Encoding Custom Types####
###############################
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

json.dumps(3 + 4j, default=encode_complex) #-> '[3.0, 4.0]'