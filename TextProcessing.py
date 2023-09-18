# Write a python  program that given a string, performing the following processing:
# Converting all letters to lower case
# Removes numbers
# Removes punctuations, accent marks and other diacritics
# Removes white spaces and duble spaces

text = ' Woman, Life, Freedom(1401)'
import string
def Preprocess(text: str)->str:
    text = text.lower()
    text = ''.join(filter(lambda char: not char.isdigit(), text))
    text = ''.join(filter(lambda char: char not in string.punctuation, text))
    text = ''.join(text.split())
    
    return text
# by using unidecode library, we can change accents in python
from unidecode import unidecode
