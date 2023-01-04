# DAY 10 PART 2

# Function to calculate signal strenght
def Signal_strenght( X, cycle_count ):
    return cycle_count * X


# Variables
x = 1
cycle_count = 1
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
    if x[1] == 20 or x[1] == 60 or x[1] == 100 or x[1] == 140 or x[1] == 180 or x[1] == 220: 
        
        # here the second parameter of Signal_strenght() has a +1 because in li_cycle_log, the cycles are one less
        li_signal_strenghts.append(Signal_strenght(x[0], x[1]))

    
# Print answer
print(sum(li_signal_strenghts))


# === PART 2 === 

def Display_Screen(display):
    print(display[:40])
    print(display[40:80])
    print(display[80:120])
    print(display[120:160])
    print(display[160:200])
    print(display[200:])


# Variable
display = '.' * 240



for x_register, cycle in li_cycle_log:
    
    cycle -= 1
    
    # if x_register != 
    sprite_pos = (x_register-1, x_register, x_register + 1)

    # first row
    if cycle < 41:
        if cycle in sprite_pos:
            
            li_display = list(display)
            li_display[cycle] = '#'
            display = ''.join(li_display)

    

    # second row
    elif cycle > 40 and cycle < 81:

        cycle -= 40
        if cycle in sprite_pos:
            
            li_display = list(display)
            li_display[cycle + 40] = '#'
            display = ''.join(li_display)


    # third row
    elif cycle > 80 and cycle < 121:
        cycle -= 80
        if cycle in sprite_pos:
            
            li_display = list(display)
            li_display[cycle + 80] = '#'
            display = ''.join(li_display)


    # fourth row
    elif cycle > 120 and cycle < 161:
        cycle -= 120
        if cycle in sprite_pos:
            
            li_display = list(display)
            li_display[cycle + 120] = '#'
            display = ''.join(li_display)


    # fifth row
    elif cycle > 160 and cycle < 201:
        cycle -= 160
        if cycle in sprite_pos:

            li_display = list(display)
            li_display[cycle + 160] = '#'
            display = ''.join(li_display)


    # sixth row
    elif cycle > 200:
        cycle -= 200
        if cycle in sprite_pos:

            li_display = list(display)
            li_display[cycle + 200] = '#'
            display = ''.join(li_display)


# Answer is printed
Display_Screen(display)
    




