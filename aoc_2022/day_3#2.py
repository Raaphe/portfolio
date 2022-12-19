# DAY 3 PART 2

# all variables 
data = open('rucksack.dat', 'r')
li_elves = []
li_groups = []
li_chars = []
ii=0
sum = 0

# organizes data in tuples inside of a list
for line in data:
    
    line = line.strip()
    li_elves.append(line)
    
    ii += 1
    
    if ii == 3:
        li_groups.append((li_elves[0],li_elves[1],li_elves[2]))
        ii = 0
        li_elves.clear()
        


# loop that itters through the chars of elf1 to see if it is also inside of elf2 and elf3
for groups in li_groups:
    elf1, elf2, elf3 = groups
    for char in elf1:
        if char in elf2 and char in elf3 and char in elf1:
            # once it finds the good char, it adds it to li_char
            li_chars.append(char)
            break;
        
    
# adds the according values for each letter in char
for char in li_chars:
    if char.islower() == True:
        sum += ord(char) - 96
    elif char.islower() == False:
        sum += ord(char) - 38
    
# closes file
data.close()

# answer
print(sum)
        