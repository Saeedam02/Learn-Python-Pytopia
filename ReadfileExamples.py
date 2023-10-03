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
           line = preprocess_text(line)
           line_count = count_word(line)

           for word, word_freq in line_count.items():
                counter[word] = counter.get(word,0) + word_freq

print(counter)

# Efficent way to do this:
from collections import Counter # Counter is a object which is created for counting and updting such things
Counter([1,1,1,3,2,5]) + Counter([1,1,1,2,3,6])

def word_counter(text):
     return Counter(text.split())

counter = Counter()
with open('documents.txt') as f:
    for line in f:
           line = preprocess_text(line)
           line_count = word_counter(line)
           counter += line_count
# Finding most common word using Counter:
counter.most_common()[0]

# Finding most common word using max:
max(counter) # in this way, ot works on thongs that it itterates on
max(counter, key=counter.get) # it compares the values and return the key related the max value

# Finding longest word using len:
max(counter, key=len)

# Finding shortest word using len:
min(counter, key=len)
