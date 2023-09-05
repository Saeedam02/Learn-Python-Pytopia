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

char_freq = {}

for char in my_str:
    char_freq[char] = char_freq.get(char, 0) +1 # 0 in define for char_freq[char] when char isn't in char_freq

print(char_freq)
