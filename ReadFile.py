
# First approach
reader = open('documents.txt')
try:
    # Further file processing goes here
    pass
finally:
    reader.close()

# Remember that closing a file after opening and processing is one of the most important things.

# Second approach
with open('documents.txt') as reader:
    print(reader.read())

# when we come out of the index of 'with', it closes the file automatically
