# This code is incredibly repetitive but it works and its my way of doing it
# DAY 11 PART 2

def tomfoolery_calculator(top_Monkey1, Top_Monkey2):
    print( top_Monkey1 * Top_Monkey2 )

# starting objects
monkey_dict = {
    'monkey0':[56, 56, 92, 65, 71, 61, 79],
    'monkey1':[61, 85],
    'monkey2':[54, 96, 82, 78, 69],
    'monkey3':[57, 59, 65, 95],
    'monkey4':[62, 67, 80],
    'monkey5':[91],
    'monkey6':[79, 83, 64, 52, 77, 56, 63, 92],
    'monkey7':[50, 97, 76, 96, 80, 56]
    }  

# dict to save the amount of times a monkey has inspected an object
monkey_tomfoolery = {
    'monkey0':0,
    'monkey1':0,
    'monkey2':0,
    'monkey3':0,
    'monkey4':0,
    'monkey5':0,
    'monkey6':0,
    'monkey7':0
}

# for each round
for _ in range(10000):

    # each monkey
    for monkey in range(8):



        # == monkey 0 ==
        if monkey == 0:
            
            # makes a copy of a current list of items of a monkey
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]
                    
            # itters through the real list (the one in the dict)
            # I did this so that whenever I popped a value I wasnt 
            # forced out of the loop...
            for item in monkey_dict[f'monkey{str(monkey)}']:       
                monkey_tomfoolery['monkey0'] += 1
                worry = item * 7

                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                # true or false conditions to know which monkey was next
                if worry % 3 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey3'].append(worry)

                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey7'].append(worry)

            # resets live list in dict
            monkey_dict[f'monkey{str(monkey)}'] = []


        # == monkey 1 ==
        elif monkey == 1:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]


            for item in monkey_dict[f'monkey{str(monkey)}']:   
                monkey_tomfoolery['monkey1'] += 1
                worry = item + 5
            
                
                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 11 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey6'].append(worry)
                
                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey4'].append(worry)
            
            monkey_dict[f'monkey{str(monkey)}'] = []

        # == monkey 2 ==
        elif monkey == 2:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]

            for item in monkey_dict[f'monkey{str(monkey)}']:   
            
                monkey_tomfoolery['monkey2'] += 1
                worry = item ** 2
            

                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 7 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey0'].append(worry)
                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey7'].append(worry)

            monkey_dict[f'monkey{str(monkey)}'] = []

        # == monkey 3 ==
        elif monkey == 3:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]

            for item in monkey_dict[f'monkey{str(monkey)}']:                    
                monkey_tomfoolery['monkey3'] += 1
                worry = item + 4
            

                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 2 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey5'].append(worry)

                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey1'].append(worry)

            monkey_dict[f'monkey{str(monkey)}'] = []

        # == monkey 4 ==
        elif monkey == 4:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]
            
            for item in monkey_dict[f'monkey{str(monkey)}']:        
            
                monkey_tomfoolery['monkey4'] += 1
                worry = item  * 17
            

                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 19 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey2'].append(worry)

                else: 
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey6'].append(worry)
            
            monkey_dict[f'monkey{str(monkey)}'] = []

        # == monkey 5 ==
        elif monkey == 5:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]
            
            for item in monkey_dict[f'monkey{str(monkey)}']:     
                monkey_tomfoolery['monkey5'] += 1
                worry = item + 7


                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 5 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey1'].append(worry)
                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey4'].append(worry)

            monkey_dict[f'monkey{str(monkey)}'] = []
        
        
        # == monkey 6 ==
        elif monkey == 6:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]
    
            for item in monkey_dict[f'monkey{str(monkey)}']:     
                monkey_tomfoolery['monkey6'] += 1
                worry = item + 6


                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 17 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey2'].append(worry)
                else: 
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey0'].append(worry)

            monkey_dict[f'monkey{str(monkey)}'] = []

        # == monkey 7 ==
        elif monkey == 7:
            monkey_items = monkey_dict[f'monkey{str(monkey)}'][:]

            for item in monkey_dict[f'monkey{str(monkey)}']:      
                monkey_tomfoolery['monkey7'] += 1
                worry = item +3


                if _ % 250 == 0 and _ != 0:
                    worry = worry % 9_699_690

                if worry % 13 == 0:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey3'].append(worry)
                else:
                    try:monkey_items.pop(0)
                    except IndexError:
                        pass;
                    monkey_dict['monkey5'].append(worry)

            monkey_dict[f'monkey{str(monkey)}'] = []



# finds top 2 monkeys
li_tomfoolerage = list(monkey_tomfoolery.values())
topM1 = li_tomfoolerage.pop(li_tomfoolerage.index(max(li_tomfoolerage)))
topM2 = li_tomfoolerage.pop(li_tomfoolerage.index(max(li_tomfoolerage)))

print(li_tomfoolerage)
# prints answer
tomfoolery_calculator(topM1, topM2)
