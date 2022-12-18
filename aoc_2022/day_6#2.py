# DAY 6 PART 2

# Open file + variable
data = open('transmission.dat', 'r').read()

# puts each character in the string in a list I can iterate through
char_li = [char for char in data]

# main loop, iterates through each string
for ii in range(len(data)-13):
   
    # puts into a set strings, 14 at a time
    char_set = {char for char in char_li[ii:ii+14]}

    # if the set is 14 (sets can only have on of the same value), the code breaks after having printed the answer
    if len(char_set) == 14:
        print(ii+14)
        break;
