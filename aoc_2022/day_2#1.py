# DAT 2 PART 1

# opening file with all the elf calories
data = open('rps_guide.dat', 'r')

#defining variables
list_plays = []
counter = 0

# puts values in the guide inside a list of tuples
for line in data:
    line = line.strip().split(" ")
    list_plays.append((line[0], line[1]))

user_points = []

for elem in list_plays:
    if elem[0] == "A" and elem[1] == "X":
        user_points.append(4)
    elif elem[0] == "A" and elem[1] == "Y":
        user_points.append(8)
    elif elem[0] == "A" and elem[1] == "Z":
        user_points.append(3)
    elif elem[0] == "B" and elem[1] == "X":
        user_points.append(1)
    elif elem[0] == "B" and elem[1] == "Y":
        user_points.append(5)
    elif elem[0] == "B" and elem[1] == "Z":
        user_points.append(9)
    elif elem[0] == "C" and elem[1] == "X":
        user_points.append(7)
    elif elem[0] == "C" and elem[1] == "Y":
        user_points.append(2)
    elif elem[0] == "C" and elem[1] == "Z":
        user_points.append(6)


print(sum(user_points))
data.close()

"""
A = ROCK 1 
B = PAPER 2
C = SCISSORS 3 

X = ROCK 1 
Y = PAPER 2
Z = SCISSORS 3

0 IF LOST

3 DRAW

6 WON


"""