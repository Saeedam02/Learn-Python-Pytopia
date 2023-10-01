
# First approach
reader = open('documents.txt')
try:
    # Further file processing goes here
    pass
finally:
    reader.close()

# Remember that closing a file after opening and processing is one of the most important things.

# Second approach
with open('documents.txt') as reader: 
    print(reader.read())

# when we come out of the index of 'with', it closes the file automatically
# there are three approach for reading a file:
# LINE BY LINE: 
for line in reader:
    print(line , end='')

# especified charact ers:
reader.read(1000)

# reading line by line with command:
reader.readline()

reader.readlines() # read all lines 
# Best way:
with open('documents.txt') as reader:
    for lline in reader:
        print(line , end='')

# there are some other input parameters in open func like mode( is automatically on write mode )
reader = open('documents.txt', mode='r')

#################################### Writing in a file ########################################
# Note that when you openn a file for writing something, it's like overwriting and it will clear all data.

writer=open("documents.txt", "w")   ## w means writing, if you want to append then use r+ instead of just +
writer.write('') # output of this command is len of the text which we wrote

# when we write data in a file, because of interaction between the memoey and hard disk, it dosen't transfer information immediatlly and we must use the following command:
writer.flush()
# if we close the file, it will automatically flush the file.

# All this command are better be used by "with"
with open('myfile.txt', 'w') as file:
    file.writelines(['line one','line two'])

################################### Appending to a file #########################################

with open('myfile.txt','a') as file:
    file.write('\nThis is new appended content.')