# First example: get Frequency of unique elements in an iterable

my_str = 'abdjcnkdakmdnkp'
char_freq = {}
# approach 1 
for char in my_str:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print(char_freq)

# approach 2


def char_counter(s:str) ->dict:
    """
    get Frequency of unique elements in an iterable
    :param s: INput string
    :returns: A dictionary of characters frequency.
    Example:
    >>>char_count('abc)
    {'a': 1, 'b': 1, 'c': 1}
    """
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) +1 # 0 in define for char_freq[char] when char isn't in char_freq

    return char_freq

my_str = 'abdjcnkdakmdnkp'
char_counter(my_str)

# approach 3

from collections import Counter
print(Counter(my_str))

###### Second example: make sentence

# approach 1
subjects = ['I', 'You']
verbs = ['Play' , 'Love']
objects = ['Hochey' , 'Football']
sentences=[]
for s in subjects:
    for v in verbs:
        for o in objects:
           sent = f'{s} {v} {o}'
           sentences.append(sent)
print(sentences)

#approach 2
from typing import Iterable
def make_sentense(subjects: Iterable[str], verbs: Iterable[str], objects:Iterable[str]) ->list:
    """
    Generate all possible sentences from inputs
    :param subjests: Input sentences subjects
    :param verbs: Input sentences verbs
    :param objects: Input sentences objects
    :returns: List of all possible sentences
    """
    import itertools # This library is used to write all Permutations of some lists

    sentences_2 = itertools.product(subjects, verbs, objects)
    sentences_2 = list(map(lambda sentence: ''.join(sentence), sentences))
    return sentences_2

make_sentense(subjects,verbs,objects)

#### Third example : Find Distance

# approach 1

moves = []
while True:
    move = input(' Enter robot move: ').upper()
    if move == 'END':
        break

    direction , displace = move.split(' ')
    displace = float(displace)
    if direction not in ['RIGHT', 'LEFT', 'UP', 'DOWN']:
        print('Invalid direction, please try again.options are RIGHT, LEFT, UP and DOWN')
        
    moves.append(move)

from typing import List
def robot_movment(moves: List[str]) ->float :
    """
    Calculate the distance having robot moves in UP, DOWN, RIGHT and LEFT directions.
    :param moves: List of robot direction.
    :returns: Final robot distance from origin.
    """
    # initial rbot position
    X , Y = 0, 0
    for move in moves :
       
        if direction == 'UP':
            Y += displace
        elif direction == 'DOWN':
            Y -= displace
        elif direction == 'RIGHT':
            X += displace
        else:
            X -= displace
    dist = (X ** 2 + Y ** 2 ) ** 0.5
    return dist
robot_movment(moves)

############## Fourth Example: cheack validation

def is_valid_pass(password: str) -> bool 
    """
    Check if a password is valid based on rules.
    Rules:
    - Password length must be greater than.
    - Password can't be just numbers.
    - Password can't be all in lower case.

    :param password: User password
    :returns: Returs True if password is a valid one.
    Example:
    >>> is_valid_pass('abc')
    False
    >>> is_valid_pass('Abcd1254')
    True
    """
    
    if (
        len(password) < 6 
        or password.isdigit() 
        or password.lower() == password
    ) : 
        return False

    return True

def is_valid_username(username: str) :
    return len(username) >= 4 # it returns True if the len of username is greater or equal to 4

def cheack_validation(**kwargs) ->List:
    """"
    Check if pairs of username and passwords are valid.

    :param kwargs: Dictionary of username password pairs.
    :returns: Valid usernames

    """
    valid_usernames=[]
    for username, password in kwargs.items() :
        if is_valid_username(username) and is_valid_pass(password):
            valid_usernames.append(username)

    return valid_usernames



#### Fifth : Find pangram

import string

def is_pangram(sentence: str) -> bool :
    """
    Check if a sentence is a pangram.
    A pangram is a sentence that contains all the letters of English Alphabets.

    :param sentence: Input sentence to check.
    :returns: If sentence is a pangram.
    
    Example:
    >>> is_pangram('The bigger you dream, the richer you become.')
    False
    """

    alphabets = set(string.ascii_lowercase)
    for char in alphabets:
        if char.lower() in alphabets:
            alphabets.remove(char.lower())

    if len(alphabets) !=0 :
        return False
    else:
        return True    
    

######### Sixth Example: Find Shortest and Longest words

sentence = ' Python, which was initially developed by Guidi van Rossum and made available to the public in 1991 is currently one of the most widely used general-purpose programming languages.'
sentence = ''.join(filter(lambda char: char not in string.punctuation, sentence))
words = sentence.split()

#approach 1

smallest_word = words[0]
longest_word = words[0]
for word in words :
    if len(word) < len(smallest_word) :
        smallest_word = word
    if len(word) > len(longest_word) :
        longest_word = word

# approach 2

length = list(map(len , words))
smallest = min(length)
longest = max(length)
smallest_word = words[smallest]
longest_word = words[longest]

# approach 3
def shortest_longest_words(sentence : str) -> tuple:
    """
    Find Shortest and Longest words from a sentence

    :param sentence: Input sentence to find its shortest and longest words.
    :returns: Shortest and Longest words.
    """
    words = sentence.split()
    longest_word = max(words , key = lambda w: len(w))
    smallest_word = min(words , key = lambda w: len(w)) 
    return shortest_longest_words, longest_word