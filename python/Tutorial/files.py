# Opening file
fhand = open("/Users/sejinchoi/Documents/Git/ml/python/mbox.txt")
#<_io.TextIOWrapper name='/Users/sejinchoi/Documents/Git/ml/python/mbox.txt' mode='r' encoding='UTF-8'>
print(fhand)
#fhand = open('stuff.txt')  #FileNotFoundError: [Errno 2]
# Adding newline as \n
stuff ='Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
len(stuff)
# File handle as a sequence
xfile = open("/Users/sejinchoi/Documents/Git/ml/python/mbox.txt")
for cheese in xfile:
    print #(cheese)
# Counting lines in a file
fhand = open("/Users/sejinchoi/Documents/Git/ml/python/mbox.txt")
count = 0
for line in fhand:
    count = count+1
print("Line count:", count)
# Reading the 'whole' file
fhand = open("/Users/sejinchoi/Documents/Git/ml/python/mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20]) # read only 20 chars
# Searching Through a File, using rstrip() to remove \n 
fhand = open("/Users/sejinchoi/Documents/Git/ml/python/mbox-short.txt")
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:'):
        print#(line)
# Using in to select lines
fhand = open("/Users/sejinchoi/Documents/Git/ml/python/mbox-short.txt")
for line in fhand :
    line = line.rstrip()
    if not '@uct.ac.nz' in line:
        continue
    print(line)
# Prompt for file name
fname = input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject lines in', fname)
