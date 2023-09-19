
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
    def __init__(self, casing='lower'):
        self.casing = casing
    
        
    def transform(self, text):
        if self.casing == 'lower':
            return  text.lower()
        elif self.casing == 'upper':
            return text.upper()
        elif self.casing == 'title':
            return self.title()
    
class RemoveDigit:
    def transform(self, text):
        return ''.join(filter(lambda char: not char.isdigit(), text))
    
class RemoveSpace:
    def transform(self, text):
        return ''.join(text.split())
    
class RemovePunkt:
    def transform(self, text):
        return ''.join(filter(lambda char: char not in string.punctuation, text))
    
class TextPipline:
    def __init__(self, *args):
        self.transformers = args

    def transform(self, text):
        for tf in self.transformers:
            text = tf.trannsform(text)
        return text
    
pipe = TextPipline(
    ConvertCase('upper'),
    RemoveDigit(),
    RemovePunkt(),
    RemoveSpace(),
)

text = ' Woman, Life, Freedom(1401)'
print(pipe.transform(text))

# Better approach for this processing is using ABC library
from abc import ABC, abstractmethod

class TextProcessor(ABC):
    @abstractmethod
    def transform(self, text):
        pass

class ConvertCase(TextProcessor):
    def __init__(self, casing='lower'):
        self.casing = casing
    
        
    def transform(self, text):
        if self.casing == 'lower':
            return  text.lower()
        elif self.casing == 'upper':
            return text.upper()
        elif self.casing == 'title':
            return self.title()
    
class RemoveDigit(TextProcessor):
    def transform(self, text):
        return ''.join(filter(lambda char: not char.isdigit(), text))
    
class RemoveSpace(TextProcessor):
    def transform(self, text):
        return ''.join(text.split())
    
class RemovePunkt(TextProcessor):
    def __init__(self, replace_char=' '):
        self.replace_char = replace_char

    def transform(self, text):
        return ''.join(char if not char in string.punctuation else self.replace_char for char in text)
    
class StripAccent(TextProcessor):
    def transform(self, text):
        return unidecode(text)
class TextPipline(TextProcessor):
    def __init__(self, *args):
        self.transformers = args

    def transform(self, text):
        for tf in self.transformers:
            text = tf.trannsform(text)
        return text
    
    
