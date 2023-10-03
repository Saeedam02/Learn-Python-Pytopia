# Read a text file and counts the unique numbers

import string

with open('documents.txt') as f:
    content = f.read()

def preprocess_text(text):
    text = ''.join([char if char not in string.punctuation else ' ' for char in text ])
    return text.lower()

text = preprocess_text(content)
print(text)

def count_word(text):
    """
    Counting the number of each word
    :param text: Input
    :returns: Count dictionary which is contains number of each words
    """
    count = {}
    for word in text.split():
        count[word] = count.get(word,0) + 1

    return count
