# DAY 7 PART 1


system = [('/')]
# eg ; [('/'),  [('dir1'), ][('dir2')], [('dir3'), ('file1', 'size1'), [('subdir')]]]
currentdir = ""

# parsing
data = open('linux_comm.dat', 'r')
li_comm = [line.strip() for line in data]
tree = []
tree_level = 0






for comm in li_comm:
    if comm[0] == '$':
        if comm[2:4] == 'cd' and comm[5:] != '..':
            tree_level += 1
            tree.append((comm[5:], tree_level)) 
        elif comm[2:4] == 'cd' and comm[5:] == '..':
            tree_level -= 1


print(tree)

data.close()