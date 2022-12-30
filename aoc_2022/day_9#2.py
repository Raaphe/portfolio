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

   for jj in range(9):
       
       
      headx, heady = rope[f'knot{str(jj)}'][ii]    
      tailx, taily = rope[f'knot{str(jj+1)}'][-1]
         
      new_tail_pos = next_tail_pos(headx, heady, tailx, taily)

      if new_tail_pos == None:
          continue;
      else:
          li = list(rope['knot1'])
          li.append(new_tail_pos)
          rope.update({'knot1': li})
        
    
#on paper this code works
print(len(set(rope['knot9'])))
