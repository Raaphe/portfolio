# DAY 7 PART 1


# I was very stuck on this day and did not know how to properly use dictionaries.
# I spoiled myself and much of this code was taken from Jeffery Frederick's advent of code python solution video 
# though i didnt complete day 7 part 1 on my own, I learned much from trying to crack it


# parsing
data = open('linux_comm.dat', 'r')
li_comm = [line.strip() for line in data]



# variables
dirs = {'/home':0}
path = "/home"


# main for loop
for com in li_comm:
    
    # if the line is a command 'cd' or 'ls'
    if com[0] == '$':
        
        # do nothing if its 'ls'
        if com[2:4] == "ls":
            pass;

        # if its 'cd'
        elif com[2:4] == 'cd' :
            
            # return to home
            if com[5:] == '/':
                path = "/home"

            # go back to parent directory
            elif com[5:] == '..':
                path = path[:path.rfind('/')]

            # if not 'cd /' or 'cd ..', change to new dir
            elif com[5:] != '..' or com[5:] != '/':
                new_dir = com[5:]
                path = path + '/' + new_dir
                dirs.update({path:0})
    
    # does nothing when a dir is listed
    elif com[0:3] == 'dir':
        pass;

    # get file size
    elif com[0:3] != 'dir':
        file_size = int(com[:com.find(' ')])

        dir = path
        for ii in range(path.count('/')):
            dirs[dir] += file_size
            dir = dir[:dir.rfind('/')]

# list of all the dirs that are at most 100k in size
li_under_100k = []

# adds all the file sizes under 100k in list``
for dir in dirs:
    print(dir, dirs[dir])
    if dirs[dir] <= 100000:
        li_under_100k.append(dirs[dir])

# prints answer
print(sum(li_under_100k))

#close file
data.close()