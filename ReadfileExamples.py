# Read a text file and counts the unique numbers

import string

with open('documents.txt') as f:
    count = f.read()

def preprocess_text(text):
    text = ''.join([char if char not in string.punctuation else ' ' for char in text ])
    return text.lower()

count = preprocess_text(count)
print(count)