data = open('linux_comm.dat', 'r')
li_comm = [line.strip() for line in data]

tree = []
tree_level = 0
cd = ''
tree2 = []
str1 = ''

for com in li_comm:
    if com[0] == '$':
        if com[2:4] == 'cd' and com[5:] != '..':
            tree_level += 1
            cd = com[5:]
            tree.append((com[5:], tree_level)) 
        elif com[2:4] == 'cd' and com[5:] == '..':
            tree_level -= 1 

    if com[0] != '$':
        if com[:3] != 'dir':
            str1 += f"/{com.strip()}/"

print(str1)


class Node:
    def __init__(self, file, dir ):
        pass

data.close()

