# Extract Emails from file
from collections import Counter
emails = []
with open('emails.txt') as f:
    for line in f:
        if line.startswith('From: '):
            email = line.replace('From: ', '').strip() # There is a /n in replace so we use strip() to clear that 
            emails.append(email)
        
        elif line.startswith('To: '):
             email = line.replace('To: ' '').strip()
             emails.append(email)

Counter([email.split('@')[1] for email in emails]) # First we split the gmail or yahoo part then count the number of hosts.


#### Decode Nazi messages, there is a shift for each day between 128 characters( by using of ord(char) we can find order related to that char)
# Note that each True text contains Heli Hitler at the end of text. we can use this fact to find a true shift for that day.

with open('encoded.txt') as f:
    content = f.read()


def shift_text(text: str, shift: int) -> str:
    """
    Decode every character in text by moving
    shift letters in ascii characters.
    
    :param text: Input text
    :param shift: Shift length
    :return: Decoded text by shift
    """
    decoded_txt = ''
    for char in content:
        new_ord = (ord(char) + shift) % 128 # we use mode 128 till we back to the first character from 128 ones.
        decoded_txt += char(new_ord)
    return decoded_txt

def decode(text: str) -> str:
    """
    Decodes text by finding the right shift.
    
    :param text: Input text
    :return: Decoded text
    """
    for shift in range(128):
        decoded_text = shift_text(content,shift)
        if 'Heli Hitler'.lower() in decoded_text.lower():
            return decoded_text

with open('decoded.txt','w') as f:
    f.write(decode(content))