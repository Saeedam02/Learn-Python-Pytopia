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

# This way takes huge space from memory so instead of that, we can use the following method:
counter = {}
with open('documents.txt') as f:
    for line in f:
           line_count = count_word(line)

           for word, word_freq in line_count.items():
                counter[word] = counter.get(word,0) + word_freq

print(counter)