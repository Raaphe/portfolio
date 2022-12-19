# DAY 3 PART 1

# opens files containing rucksacks + variables
data = open('rucksack.dat', 'r')
sum = 0

# main loop
for line in data:
    line = line.strip()
    
    # splits line in halves
    half1 = line[0:((len(line))//2)]
    half2 = line[((len(line)//2)):] 
    
    # sorts through each character and adds to sum once it finds the right char
    for char in half1:
        if char in half2:
            if char.islower()== True:
                sum += ord(char)-96
                break;
            elif char.islower()== False:
                sum += ord(char)-38
                break;

# closes file
data.close()

# answer
print(sum)