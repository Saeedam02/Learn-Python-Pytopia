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