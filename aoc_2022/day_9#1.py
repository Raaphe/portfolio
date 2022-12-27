#DAY 9 PART 1

# Variables
head_pos = (0,0)
li_head_pos = []
set_tail_pos = set()
tail_pos = (0,0)


with open('day9_input.dat','r') as file:

    # Parsing
    for line in file:
        line = line.strip().split()
        line[1] = int(line[1])


        # gets all the positions and changes in positions of the 'H' of the rope
        for ii in range(1,line[1]+1):

            if line[0] == 'U':
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif line[0] == 'D':
                head_pos = (head_pos[0], head_pos[1] - 1)
            elif line[0] == 'L':
                head_pos = (head_pos[0] - 1, head_pos[1])
            elif line[0] == 'R':
                head_pos = (head_pos[0] + 1, head_pos[1])

            li_head_pos.append(head_pos)
        


for ii in range(len(li_head_pos)):
    
    headx, heady = li_head_pos[ii]
    
    if ii != 0:
        last_coord = li_head_pos[ii-1]
    

    # === Diagonal cases === 
    # (Going up or down)
    
    # Bottom left
    if tail_pos == (headx + 1, heady + 2):
        tail_pos = (headx, heady + 1)
        set_tail_pos.add(tail_pos)
        continue;

    # Bottom right
    elif tail_pos == (headx - 1, heady + 2):
        tail_pos = (headx, heady + 1)
        set_tail_pos.add(tail_pos)
        continue;

    # Top left
    elif tail_pos == (headx + 1, heady - 2):
        tail_pos = (headx, heady - 1)
        set_tail_pos.add(tail_pos)
        continue;

    # Top right
    elif tail_pos == (headx - 1, heady - 2):
        tail_pos = (headx, heady - 1)
        set_tail_pos.add(tail_pos)
        continue;
    
    # (Going left or right)

    # Left - Up
    elif tail_pos == (headx + 2, heady - 1):
        tail_pos = (headx + 1, heady)
        set_tail_pos.add(tail_pos)
        continue;

    # Left - Down
    elif tail_pos == (headx + 2, heady + 1):
        tail_pos = (headx + 1, heady)
        set_tail_pos.add(tail_pos)
        continue;

    # Right - Down
    elif tail_pos == (headx - 2, heady + 1):
        tail_pos = (headx - 1, heady)
        set_tail_pos.add(tail_pos)
        continue;

    # Right - Up
    elif tail_pos == (headx - 2, heady - 1):
        tail_pos = (headx - 1, heady)
        set_tail_pos.add(tail_pos)
        continue;


    # === Same axis cases ===

    # Up
    elif tail_pos == (headx, heady - 2):
        tail_pos = (headx, heady - 1)
        set_tail_pos.add(tail_pos)
        continue;

    # Left
    elif tail_pos == (headx + 2, heady):
        tail_pos = (headx + 1, heady)
        set_tail_pos.add(tail_pos)
        continue;

    # Down
    elif tail_pos == (headx, heady + 2):
        tail_pos = (headx, heady + 1)
        set_tail_pos.add(tail_pos)
        continue;

    # Right
    elif tail_pos == (headx - 2, heady):
        tail_pos = (headx - 1, heady)
        set_tail_pos.add(tail_pos)
        continue;





print(len(set_tail_pos))