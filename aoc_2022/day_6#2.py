# Open file + variable
data = open('transmission.dat', 'r').read()
transm = ''
char_li = []

# puts each character in the string in a list I can iterate through
for char in data:
    char_li.append(char)

print(char_li)

