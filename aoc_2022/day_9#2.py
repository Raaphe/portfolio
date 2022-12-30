#DAY 9 PART 2

def next_tail_pos(headx, heady, tailx, taily):

    tail_pos = (tailx, taily)
   
    # === Diagonal cases === 
    # (Going up or down)
    
    # Bottom left
    if tail_pos == (headx + 1, heady + 2):
        return (headx, heady + 1);

    # Bottom right
    elif tail_pos == (headx - 1, heady + 2):
        return (headx, heady + 1);

    # Top left
    elif tail_pos == (headx + 1, heady - 2):
        return (headx, heady - 1);
        
    # Top right
    elif tail_pos == (headx - 1, heady - 2):
        return (headx, heady - 1);
        
        
    
    # (Going left or right)

    # Left - Up
    elif tail_pos == (headx + 2, heady - 1):
        return (headx + 1, heady);

    # Left - Down
    elif tail_pos == (headx + 2, heady + 1):
        return (headx + 1, heady);

    # Right - Down
    elif tail_pos == (headx - 2, heady + 1):
        return (headx - 1, heady);   

    # Right - Up
    elif tail_pos == (headx - 2, heady - 1):
        return (headx - 1, heady);
        

    # === Same axis cases ===


    # Up
    elif tail_pos == (headx, heady - 2):
        return (headx, heady - 1);
        

    # Left
    elif tail_pos == (headx + 2, heady):
        return (headx + 1, heady);
        
    # Down
    elif tail_pos == (headx, heady + 2):
        return (headx, heady + 1);        

    # Right
    elif tail_pos == (headx - 2, heady):
        return (headx - 1, heady);

    # Part 2 new movement cases


    # === Diagonal cases ===


    # Right
    elif tail_pos == (headx - 2, heady - 2):
        return (headx - 1,heady - 1)
        
    # Left 
    elif tail_pos == (headx + 2, heady - 2):
        return (headx + 1,heady - 1)
    
    # Down Right
    elif tail_pos == (headx - 2, heady + 2):
        return (headx - 1,heady + 1)

    # Down Left
    elif tail_pos == (headx + 2, heady + 2):
        return (headx + 1,heady + 1)

# Variables
head_pos = (0,0)
rope =  {
'knot0':[(0,0)],
'knot1':[(0,0)],
'knot2':[(0,0)],
'knot3':[(0,0)],
'knot4':[(0,0)],
'knot5':[(0,0)],
'knot6':[(0,0)],
'knot7':[(0,0)],
'knot8':[(0,0)],
'knot9':[(0,0)],
}


with open('day9_input.dat','r') as file:

    # Parsing
    for line in file:
        line = line.strip().split()
        line[1] = int(line[1])

        # finds all positions of the first knot
        for ii in range(1,line[1]+1):

            if line[0] == 'U':
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif line[0] == 'D':
                head_pos = (head_pos[0], head_pos[1] - 1)
            elif line[0] == 'L':
                head_pos = (head_pos[0] - 1, head_pos[1])
            elif line[0] == 'R':
                head_pos = (head_pos[0] + 1, head_pos[1])

            li = list(rope['knot0'])
            li.append((head_pos))
            rope.update({'knot0':li})




# Main umbrella loop for all the rope knot position changes
for ii in rope['knot0'] :

    # kicks off the head of the rope before finding the other 7 knots
    headx, heady = ii
    tailx, taily = rope['knot1'][-1]
         
    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot1'])
        li.append(new_tail_pos)
        rope.update({'knot1': li})
        

    # loop here finds and updates the other 7 knots each iteration
    for jj in range(1,9):
       
       
        headx, heady = rope[f'knot{str(jj)}'][-1]    
        tailx, taily = rope[f'knot{str(jj+1)}'][-1]
         
        new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

        if new_tail_pos == None:
            continue;
        else:
            li = list(rope[f'knot{str(jj+1)}'])
            li.append(new_tail_pos)
            rope.update({f'knot{str(jj+1)}': li})
        
    
#prints answer
print(len(set(rope['knot9'])))
