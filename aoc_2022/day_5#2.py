
# Variables + open file
# line 1 to 20 makes the first instance of the crates and is what I have them organized as for data manipulation
# line 23 to 29 I clean up each line of the opened file
data = open('crates.dat' , 'r')
li_of_commands = []
final_str = ''

row0 =  []
row1= [["D"],["T"],["R"],["B"],["J"],["L"],["W"],["G"]]
row2= [["S"],["W"],["C"]]
row3= [["R"],["Z"],["T"],["M"]]
row4= [["D"],["T"],["C"],["H"],["S"],["P"],["V"]]
row5= [["G"],["P"],["T"],["L"],["D"],["Z"]]
row6= [["F"],["B"],["R"],["Z"],["J"],["Q"],["C"],["D"]]
row7= [["S"],["B"],["D"],["J"],["M"],["F"],["T"],["R"]]
row8= [["L"],["H"],["R"],["B"],["T"],["V"],["M"]]
row9= [["Q"],["P"],["D"],["S"],["V"],]

list_rows = [row0,row1, row2, row3, row4, row5 , row6, row7, row8, row9]

for line in data:
    line = line.strip().split()
    line.pop(0)
    line.pop(1)
    line.pop(2)

    li_of_commands.append(list(map(int,line)))


# This loop takes care of moving crates
for com in li_of_commands:
    # variables from the command
    num, fromm, to = com

    
    list_rows[to].extend(list_rows[fromm][-num:])
    del list_rows[fromm][-num:]


# row0 was used so that there wouldnt be any issues with indexes, here we remove this row
del list_rows[0]

# gives us the result
for row in list_rows:
    print(row)
    final_str += row[-1][0]


# prints us the result
print(final_str)

# closes file
data.close()