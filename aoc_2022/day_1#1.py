# opening file with all the elf calories
data = open('elf_cals.dat', 'r')

# defining a umbrella list and a variable to hold the calories of one single elf
li_cals = []
elf_cal = 0

# for loop that sorts the calories of the elfs, adds up all elf snacks, once empty line, resets the 
# <elf_cals> variable
for line in data:
    try: elf_cal += int(line.strip())
    except ValueError:
        li_cals.append(elf_cal)
        elf_cal = 0

# prints answer once all operations are made
print(li_cals)
print(max(li_cals))

# closes file
data.close()

    