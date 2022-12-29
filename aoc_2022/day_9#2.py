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
    
# for each knot0 movement, in one loop, check if the other knots
# change positions using the movement function


# each knot here is represented by a loop

for ii in range(len(rope['knot0'])) :

   for ii in range(10):
       # knot 0 and knot 1 
       try:
          headx, heady = rope[f'knot{ii}'][ii]    
          tailx, taily = rope['knot{ii+1}'][-1]
       except IndexError:
          break; #I think
         
       new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

       if new_tail_pos == None:
           continue;
       else:
           li = list(rope['knot1'])
           li.append(new_tail_pos)
           rope.update({'knot1': li})
        
    

for ii in range(len(rope['knot1'])) :

    # knot 1 and knot 2 
    headx, heady = rope['knot1'][ii]    
    tailx, taily = rope['knot2'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot2'])
        li.append(new_tail_pos)
        rope.update({'knot2': li})



for ii in range(len(rope['knot2'])) :

    # knot 2 and knot 3 
    headx, heady = rope['knot2'][ii]    
    tailx, taily = rope['knot3'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot3'])
        li.append(new_tail_pos)
        rope.update({'knot3': li})
         


for ii in range(len(rope['knot3'])) :
    
    # knot 3 and knot 4 
    headx, heady = rope['knot3'][ii]    
    tailx, taily = rope['knot4'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot4'])
        li.append(new_tail_pos)
        rope.update({'knot4': li})
            

for ii in range(len(rope['knot4'])) :
    
    # knot 4 and knot 5 
    headx, heady = rope['knot4'][ii]    
    tailx, taily = rope['knot5'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot5'])
        li.append(new_tail_pos)
        rope.update({'knot5': li})
        

for ii in range(len(rope['knot5'])) :
    
    # knot 5 and knot 6 
    headx, heady = rope['knot5'][ii]    
    tailx, taily = rope['knot6'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot6'])
        li.append(new_tail_pos)
        rope.update({'knot6': li})
            

for ii in range(len(rope['knot6'])) :
    
    # knot 6 and knot 7 
    headx, heady = rope['knot6'][ii]    
    tailx, taily = rope['knot7'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot7'])
        li.append(new_tail_pos)
        rope.update({'knot7': li})
        

for ii in range(len(rope['knot7'])) :
    
    # knot 7 and knot 8 
    headx, heady = rope['knot7'][ii]    
    tailx, taily = rope['knot8'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot8'])
        li.append(new_tail_pos)
        rope.update({'knot8': li})
        

for ii in range(len(rope['knot8'])) :
        
    # knot 8 and knot 9 
    headx, heady = rope['knot8'][ii]    
    tailx, taily = rope['knot9'][-1]

    new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

    if new_tail_pos == None:
        continue;
    else:
        li = list(rope['knot9'])
        li.append(new_tail_pos)
        rope.update({'knot9': li})
        

print(rope)

# print(len(set(rope['knot9'])))

    
    











