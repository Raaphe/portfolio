#DAY 8 PART 1

# open file + variables
data = open('tree_grid.dat', 'r')
dummy_row = []
grid = []
li_coords = []
counter = 0



# function used to verify if a target number is visible
def isVisible(grid, y, x):
    """
    returns True if visible otherwise returns false 
    """
    # variables
    target = grid[y][x]
    row_right = grid[y][x+1:]
    row_left = grid[y][:x]
    collumn_up = []
    collumn_down = []
    false_counter = 0

    # above target
    for row_index in range(0, y):
        collumn_up.append(grid[row_index][x])



    # below target
    for row_index in range(y+1, len(grid)):
        collumn_down.append(grid[row_index][x])


    # each for loop verifies if the trees are taller or not in specified row or collumn
    for tree_height in row_left:
        if target <= tree_height:
            false_counter += 1
            break;

    for tree_height in row_right:
        if target <= tree_height:
            false_counter += 1
            break;

    for tree_height in collumn_down:
        if target <= tree_height:
            false_counter += 1
            break;

    for tree_height in collumn_up:
        if target <= tree_height:
            false_counter += 1
            break;

    if false_counter == 4:
        return False;
    else:
        return True;




for line in data:

    # Strips lines
    line = line.strip()
    


    # Create next row
    dummy_row = []

    # turns each character of a line into an int and then adds to row list 
    for char in line:
        dummy_row.append(int(char))
    
    grid.append(dummy_row)





# gets the coordinates of all the trees inside the 4 walls of trees
for y in range(1,len(grid)-1):
    

    # puts them in tuples inside of a list
    for x in range(1,len(grid)-1):
        li_coords.append((y,x))


# verifies if a tree is visible, if so, counter is upped by one
for coord in li_coords:
    y, x = coord    
    if isVisible(grid, y, x) == True:
        counter += 1

# print answer
print(counter + ((len(grid) * 4) - 4))

# close file
data.close()
