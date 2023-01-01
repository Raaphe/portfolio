# DAY 10 PART 1

# Function to calculate signal strenght
def Signal_strenght( X, cycle_count ):
    return cycle_count * X


# Variables
x = 1
cycle_count = 0
li_commands = []
li_signal_strenghts = []
li_cycle_log = []


# Open file + Parsing
with open('day10.dat','r') as file:

    for line in file:
        line = line.strip().split()

        if line[0] == 'noop':
            li_commands.append('noop')
        elif line[0] == 'addx':
            li_commands.append(int(line[1]))


# Itering through commands -- for each cycle, it appends a tuple (x, cycle_count) to li_cycle_log
for comm in li_commands:

    if comm == "noop":
        cycle_count += 1
        li_cycle_log.append((x, cycle_count))

    elif comm != "noop":
        # Start first cycle of addx
        
        # Here it enters into its 2nd cycle
        cycle_count += 1
        li_cycle_log.append((x, cycle_count))

        # Here, addx is done execution
        cycle_count += 1
        x += comm
        
        li_cycle_log.append((x, cycle_count))


for x in li_cycle_log:

    # Here, if the counter ,(x[1]), is one less than the interesting signals, it calculates the signal strenght  
    if x[1] == 19 or x[1] == 59 or x[1] == 99 or x[1] == 139 or x[1] == 179 or x[1] == 219: 
        
        # here the second parameter of Signal_strenght() has a +1 because in li_cycle_log, the cycles are one less
        li_signal_strenghts.append(Signal_strenght(x[0], x[1]+1))

    
# Print answer
print(sum(li_signal_strenghts))