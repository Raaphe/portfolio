# DAY 4 PART 2

# opens file + variable
data = open('day4_input.dat', 'r')
li_pairs = []
set_counter = 0


for line in data:
    # line split and strip + variables of main loop 
    line = line.strip().split(",")
    first_num = line[0].split("-")
    second_num = line[1].split("-")
    
    # first pair vars
    num_1_pair_1 = int(first_num[0])
    num_2_pair_1 = int(first_num[1])
    # second pair vars
    num_1_pair_2 = int(second_num[0])
    num_2_pair_2 = int(second_num[1])

    # main list with all the organized values of the pairs
    li_pairs.append([num_1_pair_1, num_2_pair_1, num_1_pair_2, num_2_pair_2])


for pairs in li_pairs:
    # organizes ranges
    list1 = list(range(pairs[0],pairs[1]+1))
    list2 = list(range(pairs[2],pairs[3]+1))

    # if number is found in the list it adds 1 and breaks
    for num in list1:
        if num in list2:
            set_counter += 1 
            break;
            



# prints answer + closes file
print(set_counter)
data.close()



