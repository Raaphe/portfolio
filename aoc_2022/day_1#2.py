# opening file with all the elf calories
data = open('elf_cals.dat', 'r')

# variables, umbrella list, calorie counter and a list for the top 3 highest calorie counts
biglist = []
elf_cal = 0
top3_list = []

# loop for sorting calories
for line in data:
    try: elf_cal += int(line.strip())
    except ValueError:
        biglist.append(elf_cal)
        elf_cal = 0

# this loop adds the 3 highest calorie counts to our top three list while removing them from the other counts
for ii in range(1,4):
    top = biglist.pop(biglist.index(max(biglist)))
    top3_list.append(top)

# answer display
print(sum(top3_list))

# closes file
data.close()