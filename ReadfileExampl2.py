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