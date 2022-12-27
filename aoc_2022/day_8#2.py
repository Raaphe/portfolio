#DAY 8 PART 2

# open file + variables
data = open('tree_grid.dat', 'r')
dummy_row = []
grid = []
li_coords = []
counter = 0
li_scenic_scores = []


# function used to verify if a target number is visible
def Scenic_score_counter(grid, y, x):
    """
    returns True if visible otherwise returns false 
    """


    # variables
    target = grid[y][x]
    row_right = grid[y][x+1:]
    row_left = grid[y][:x]
    collumn_up = []
    collumn_down = []


    # below target
    for row_index in range(y+1, len(grid)):
        collumn_down.append(grid[row_index][x])

    # above target
    for row_index in range(0, y):
        collumn_up.append(grid[row_index][x])
    
    up_trees = 0
    down_trees = 0
    left_trees = 0
    right_trees = 0





    # each for loop verifies if the trees are taller or not in specified row or collumn
    for tree_height in reversed(collumn_up):
        up_trees += 1
        if target < tree_height:
            break;
        elif tree_height == target:
            break;

    for tree_height in reversed(row_left):
        left_trees += 1
        if target < tree_height:
            break;
        elif tree_height == target:
            break;

    for tree_height in collumn_down:
        down_trees += 1
        if target < tree_height:
            break;
        elif tree_height == target:
            break;
            
    for tree_height in row_right:
        right_trees += 1
        if target < tree_height:
            break;
        elif tree_height == target:
            break;

    # returns scenic score
    return up_trees * down_trees * left_trees * right_trees 


# parsing file
for line in data:
    line = line.strip()

    # Create next row
    dummy_row = []

    # turns each character of a line into an int and then adds to row list 
    for char in line:
        dummy_row.append(int(char))
    
    grid.append(dummy_row)



# gets the coordinates of all the trees 
for y in range(1,len(grid)-1):
    

    # puts them in tuples inside of a list
    for x in range(1, len(grid)-1):
        li_coords.append((y,x))


# Collects the scenic score of each tree and puts them inside a list
for coord in li_coords:
    y, x = coord    
    li_scenic_scores.append(Scenic_score_counter(grid,y,x))

# print answer
print(max(li_scenic_scores))

# close file
data.close()
