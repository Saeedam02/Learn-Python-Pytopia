
text = ' Woman, Life, Freedom(1401)'
import string
def Preprocess(text: str)->str:
    """
    A python  program that given a string, performing the following processing:
    1)Converting all letters to lower case
    2)Removes numbers
    3)Removes punctuations, accent marks and other diacritics
    4)Removes white spaces and duble spaces
    """
    #Lower case
    text = text.lower()

    #Remove Numbers
    text = ''.join(filter(lambda char: not char.isdigit(), text))
    
    #Remove Punctuations
    text = ''.join(filter(lambda char: char not in string.punctuation, text))
    
    #Remove extra spaces
    text = ''.join(text.split())
    
    return text
# by using unidecode library, we can change accents in python
from unidecode import unidecode

#########################################
######## Text processing with OOP########
#########################################

class ConvertCase:
    def transform(self, text):
        return  text.lower()
    
class RemoveDigit:
    def transform(self, text):
        return ''.join(filter(lambda char: not char.isdigit(), text))
    
class RemoveSpace:
    def transform(self, text):
        return ''.join(text.split())
    
class RemovePunkt:
    def transform(self, text):
        return ''.join(filter(lambda char: char not in string.punctuation, text))
    
