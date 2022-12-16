# Open file + variable
data = open('transmission.dat', 'r')
transm = ''
char_li = []

# reads the string in file
for line in data:
    transm = line

# puts each character in the string in a list I can iterate through
for char in transm:
    char_li.append(char)


for ii in range(len(char_li)):
    # groups characters in four, this method would'nt work if the correct answer was at the end of the string (IndexError), I assumed it wasnt    
    char1 = char_li[ii]
    char2 = char_li[ii + 1]
    char3 = char_li[ii + 2]
    char4 = char_li[ii + 3]

    # makes sure all of the 4 characters are different and then prints the position of char 4
    if char1 != char2 and char1 != char3 and char1 != char4 and char2 != char3 and char2 != char4 and char3 != char4:
        print(ii+4)
        break;

# close file
data.close()