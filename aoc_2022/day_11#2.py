#DAY 11 PART 2
from functools import cache
import sys
import math
sys.set_int_max_str_digits(999999999)


@cache
def tomfoolery_calculator(top_Monkey1, Top_Monkey2):
    print( top_Monkey1 * Top_Monkey2 )


def monkey_parse():
    
    with open('day11input.dat','r') as file:
        data = file.readlines()[:]
        
    
    # variables attributed to current monkey      
    li_inspect = [0,0,0,0,0,0,0,0]
    monkey_key = ''
    monkey_inventory = []
    test = 0
    true_monkey = []
    false_monkey = []
    fmonkey = ''
    tmonkey = ''
    operand = ''
    mode = 0

    for line in data:
        line = line.strip().split()

    
        try:


            # Monkey key
            if line[0] == 'Monkey':
                monkey_key = f'{line[1][0]}'
                continue;

            # monkey inventory
            elif line[0] == "Starting":
                monkey_inventory = list(map(int, line[2:]))
                continue;

            # new object worry calculation
            elif line[0] == 'Operation:':
                operand = line[4]
                try:mode = int(line[5])
                except ValueError:
                    operand = '**'
                    mode = 0
                continue;
        
            # Monkey test
            elif line[0] == 'Test:':
                test = int(line[3])
                continue;

            # next monkey number
            elif line[1] == 'true:':
                tmonkey = line[5]
            elif line[1] == 'false:': 
                fmonkey = line[5]
        
        except IndexError:
            
            if operand == '*':
                true_monkey = [number * mode for number in monkey_inventory if (number * mode) % test == 0] 
                false_monkey = [number * mode for number in monkey_inventory if (number * mode) % test != 0]
                    
            elif operand == '+':
                true_monkey = [number + mode for number in monkey_inventory if (number + mode) % test == 0]
                false_monkey = [number + mode for number in monkey_inventory if (number + mode) % test != 0]
    
            elif operand == '**':
                true_monkey = [number * number for number in monkey_inventory if (number * number) % test == 0]
                false_monkey = [number * number for number in monkey_inventory if (number * number) % test != 0]
            
            true_monkey = list(map(str, true_monkey))
            false_monkey = list(map(str, false_monkey))

            if tmonkey == '0':
                data[1] = f"{data[1][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '1':
                data[8] = f"{data[8][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '2':
                data[15] = f"{data[15][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '3':
                data[22] = f"{data[22][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '4':
                data[29] = f"{data[29][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '5':
                data[36] = f"{data[36][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '6':
                data[43] = f"{data[43][:-1] + ' ' +' '.join(true_monkey)}\n"
            elif tmonkey == '7':
                data[50] = f"{data[50][:-1] + ' ' +' '.join(true_monkey)}\n"
            

            if fmonkey == '0':
                data[1] = f"{data[1][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '1':
                data[8] = f"{data[8][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '2':
                data[15] = f"{data[15][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '3':
                data[22] = f"{data[22][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '4':
                data[29] = f"{data[29][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '5':
                data[36] = f"{data[36][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '6':
                data[43] = f"{data[43][:-1] + ' ' + ' '.join(false_monkey)}\n"
            elif fmonkey == '7':
                data[50] = f"{data[50][:-1]  + ' ' + ' '.join(false_monkey)}\n"
            
            if monkey_key == '0':
                data[1] = f"  Starting items: \n"
                li_inspect[0] = len(true_monkey) + len(false_monkey) + li_inspect[0]
            elif monkey_key == '1':
                data[8] = f"  Starting items: \n"
                li_inspect[1] = len(true_monkey) + len(false_monkey) + li_inspect[1]
            elif monkey_key == '2':
                data[15] = f"  Starting items: \n"
                li_inspect[2] = len(true_monkey) + len(false_monkey) + li_inspect[2]
            elif monkey_key == '3':
                data[22] = f"  Starting items: \n"
                li_inspect[3] = len(true_monkey) + len(false_monkey) + li_inspect[3]
            elif monkey_key == '4':
                data[29] = f"  Starting items: \n"
                li_inspect[4] = len(true_monkey) + len(false_monkey) + li_inspect[4]
            elif monkey_key == '5':
                data[36] = f"  Starting items: \n"
                li_inspect[5] = len(true_monkey) + len(false_monkey) + li_inspect[5]
            elif monkey_key == '6':
                data[43] = f"  Starting items: \n"
                li_inspect[6] = len(true_monkey) + len(false_monkey) + li_inspect[6]
            elif monkey_key == '7':
                data[50] = f"  Starting items: \n"
                li_inspect[7] = len(true_monkey) + len(false_monkey) + li_inspect[7]

            with open('day11input.dat', 'w') as wfile:
                wfile.writelines(data)
    
    return li_inspect




li_inspect = [0,0,0,0,0,0,0,0]

for _ in range(10_000):
    print(_)
    dummy = monkey_parse() 
    print(dummy)
    li_inspect[0] += dummy[0]
    li_inspect[1] += dummy[1]
    li_inspect[2] += dummy[2]
    li_inspect[3] += dummy[3]
    li_inspect[4] += dummy[4]
    li_inspect[5] += dummy[5]
    li_inspect[6] += dummy[6]
    li_inspect[7] += dummy[7]

# finds top 2 monkeys
print(li_inspect)
topM1 = li_inspect.pop(li_inspect.index(max(li_inspect)))
topM2 = li_inspect.pop(li_inspect.index(max(li_inspect)))


# prints answer
tomfoolery_calculator(topM1, topM2)

