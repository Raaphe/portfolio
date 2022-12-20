data = open('linux_comm.dat', 'r')
li_comm = [line.strip() for line in data]
li_sizes = []
li_under_100k = []



for com in li_comm:
    if com[0] == '$':
        
        # whenever 'cd ..' is called
        if com[2:4] == 'cd' and com[5:] == '..':


            cdnum = li_sizes.pop(-1)
            
            if cdnum <= 100_000:
                li_under_100k.append(cdnum)
                
            li_sizes = [num + cdnum for num in li_sizes]
        
        # when 'cd x' add 0 to li_sizes
        elif com[2:4] == 'cd' and com[5:] != '..':
            li_sizes.append(0)


    else:
        # do nothing if listing dirs
        if com[0] == 'd':
            pass;

        # if listing files, add all file sizes to latest dir
        else:
            file_num = int(com[:com.find(' ')])
            li_sizes[-1] += file_num
    


    print(li_sizes)

print(sum(li_under_100k))
print(li_under_100k)